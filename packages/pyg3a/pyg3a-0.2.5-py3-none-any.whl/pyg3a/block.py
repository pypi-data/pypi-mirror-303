#!/usr/bin/env python3
from typing import Final, Optional, Sequence, Never

import libcst as cst

import pyg3a
from .logging import logger
from .node import node_to_code, node_type, node_to_c_str, CST_TO_C_EQV
from .py_consts import node_to_py_const
from .scope import Scope
from .type_utils import cst_annotation_to_type
from .types import Types


class Block:
    statements: Final[list[cst.CSTNode]]
    "The statements contained within this block of code."

    scope: Final[Scope]
    "The inner scope of this block of code."

    tab_count: int
    "The number of tabs this block is indented by."

    nested_if: bool
    "True if this block is inside an if statement."

    __slots__ = "statements", "scope", "tab_count", "nested_if"

    def __init__(
        self,
        statements: Sequence[cst.BaseStatement] | Sequence[cst.BaseSmallStatement],
        tabs: int,
        scope: Optional[Scope] = None,
        nested_if: bool = False,
    ) -> None:
        """
        Create a :py:class:`Block` containing a list of statements, indented by a certain number of tabs and with an
        optional initial scope.

        :param statements: CSequence of statements inside the block of code.
        :param tabs: The number of tabs this code is indented by.
        :param scope: The scope outside the block of code.
        """

        # Set attributes from params
        self.statements = list(statements)
        self.tab_count = tabs
        self.scope = Scope() if scope is None else scope.inner()
        self.nested_if = nested_if

        # Expand statements separated by semicolons into their own statements inside :py:attr:`statements`
        for i, node in enumerate(self.statements):
            if isinstance(node, cst.SimpleStatementLine):
                del self.statements[i]
                for j, statement in enumerate(node.body):
                    self.statements.insert(i + j, statement)

    @property
    def tabs(self) -> str:
        """
        Generate a string representing the tabs at the start of each line of this block's code.

        :returns: :py:attr:`tab_count` tabs.
        """

        return self.tab_count * "\t"

    def construct(self) -> str:
        """
        Construct this block of code into C.

        :returns: A string containing the converted C block delimited with '\\n's.
        :raises SyntaxError: If unsupported syntax is used.
        """

        lines: list[str] = []
        for expr in self.statements:
            match expr:
                case cst.Expr(
                    value=cst.Call(func=cst.Name(func_name), args=[cst.Arg(value=(cst.BaseString() as c_code))])
                ) if func_name == "raw_c":
                    lines.append(f"{self.tabs}{node_to_py_const(c_code)};")

                case cst.Expr(value=expression):
                    lines.append(f"{self.tabs}{node_to_c_str(expression, self.scope)};")

                case (cst.Assign() | cst.AnnAssign(target=cst.Name())) as assign:
                    self._assignment_to_c_str(assign, lines)

                case cst.AugAssign(target=cst.Name(var_name)) if var_name not in self.scope:
                    raise SyntaxError(f"variable '{var_name}' must be defined in scope")

                case cst.AugAssign(target=cst.Subscript(value=cst.Name(var_name))) if var_name not in self.scope:
                    raise SyntaxError(f"variable '{var_name}' must be defined in scope")

                case cst.AugAssign(target, operator=cst.FloorDivideAssign(), value=value):
                    lines.append(
                        f"{self.tabs}{node_to_c_str(target, self.scope)} = {node_to_c_str(
                            cst.BinaryOperation(left=target, operator=cst.FloorDivide(), right=value), self.scope)};"
                    )

                case cst.AugAssign(target, operator, value):
                    lines.append(
                        f"{self.tabs}{node_to_c_str(target, self.scope)} {CST_TO_C_EQV[type(operator)]} {
                        (
                            node_to_c_str(value, self.scope)
                        )};"
                    )

                case cst.If(test, body, orelse=or_else):
                    if not self.nested_if:
                        lines.append(f"{self.tabs}if ({node_to_c_str(test, self.scope)}) {{")

                    expressions: Block = Block(body.body, self.tab_count + 1, self.scope)
                    lines.append(expressions.construct())

                    while or_else is not None:
                        if isinstance(or_else, cst.If):
                            lines.append(f"{self.tabs}}} else if ({node_to_c_str(or_else.test, self.scope)}) {{")
                            expressions = Block(or_else.body.body, self.tab_count + 1, self.scope)
                            lines.append(expressions.construct())

                            or_else = or_else.orelse
                        else:
                            lines.append(f"{self.tabs}}} else {{")
                            expressions = Block(or_else.body.body, self.tab_count + 1, self.scope)
                            lines.append(expressions.construct())

                            or_else = None

                    if not self.nested_if:
                        lines.append(f"{self.tabs}}}")

                case cst.While(test, body, orelse=None):
                    lines.append(f"{self.tabs}while ({node_to_c_str(test, self.scope)}) {{")

                    expressions = Block(body.body, self.tab_count + 1, self.scope)
                    lines.append(expressions.construct())

                    lines.append(f"{self.tabs}}}")

                case cst.While():
                    raise SyntaxError("No support for else clause on while statements")

                case cst.Return(value=None):
                    lines.append(f"{self.tabs}return;")

                case cst.Return(value=cst.Name(value="None")):
                    pyg3a.Main.project.includes.add("stddef.h")
                    lines.append(f"{self.tabs}return NULL;")

                case cst.Return(value=cst.Name(var_name)) if (
                    var_name not in ("None", "True", "False")
                    and self.scope[var_name]
                    in (
                        "mutstr",
                        "arrest",
                    )
                ):
                    pyg3a.Main.project.includes.add("stdlib.h")

                    tmp_name: str = pyg3a.PyG3A.gen_tmp_var(self.scope, "ret_str")
                    lines.append(f"{self.tabs}char* {tmp_name} = (char*) malloc(sizeof {var_name});")
                    lines.append(f"{self.tabs}stripy({tmp_name}, {var_name});")
                    lines.append(f"{self.tabs}return {tmp_name};")

                case cst.Return(value):
                    lines.append(f"{self.tabs}return {node_to_c_str(value, self.scope)};")

                case cst.For(
                    iter=cst.Call(func=cst.Name()), target=(cst.Name())
                ) if pyg3a.Main.project.modules.contains(expr, self.scope):
                    lines.append(pyg3a.Main.project.modules.convert(expr, self.scope, tab_count=self.tab_count))

                case cst.For(target=(cst.Name() as target), iter=iterable, body=body):
                    arr_name: str = pyg3a.PyG3A.gen_tmp_var(self.scope, "for_arr")
                    iter_name: str = pyg3a.PyG3A.gen_tmp_var(self.scope, "for_iter")

                    iter_str: str = node_to_c_str(iterable, self.scope)
                    if iter_str[0] == "{" and iter_str[-1] == "}":
                        iter_items: list[str] = iter_str[1:-1].replace(" ", "").split(",")
                        lines.append(
                            f"{self.tabs}decltype({iter_items[0]}) {arr_name}[{len(iter_items)}] = {iter_str};"
                        )
                    else:
                        lines.append(f"{self.tabs}auto {arr_name} = {iter_str};")

                    lines.append(
                        f"{self.tabs}for (unsigned int {iter_name} = 0; {iter_name} < "
                        f"sizeof({arr_name})/sizeof(*{arr_name}); {iter_name}++) {{"
                    )

                    target_type: Types.type = Types.Any
                    iter_type: Types.type | Types.GenericType = node_type(iterable, self.scope)
                    if issubclass(iter_type, Types.Sequence):
                        # if (
                        #     len(iter_type) == 2
                        #     and (iter_type[0] == "tuple" or iter_type[0] == "list")
                        #     and iter_type[1][-1] == "]"
                        # ):
                        target_type = iter_type.args[0]  # pyg3a.Main.registry[iter_type[1][:-1]]

                    lines.append(f"{self.tabs}\t{target_type} {target.value} = {arr_name}[{iter_name}];")

                    expressions = Block(
                        body.body,
                        self.tab_count + 1,
                        self.scope.inner(target.value, target_type if target_type != "auto" else "any"),
                    )
                    lines.append(expressions.construct())

                    lines.append(f"{self.tabs}}}")

                case cst.Del(target=cst.Name(var_name)) if var_name in self.scope and issubclass(
                    self.scope[var_name].type, Types.Pointer
                ):
                    pyg3a.Main.project.includes.add("stddef.h")
                    lines.append(f"{self.tabs}if ({var_name} != NULL) free({var_name});")

                case cst.Del(target=cst.Tuple(elements)) if all(
                    isinstance(el.value, cst.Name)
                    and el.value in self.scope
                    and issubclass(self.scope[el.value].type, Types.Pointer)
                    for el in elements
                ):
                    pyg3a.Main.project.includes.add("stddef.h")
                    lines.extend(f"{self.tabs}if ({el.value.value} != NULL) free({el.value.value});" for el in elements)

                case cst.Del(target=cst.Subscript()):
                    raise SyntaxError(f"'{node_to_code(expr)}': You cannot delete an item of an array.")

                case cst.Del(target=del_target):
                    raise SyntaxError(f"You cannot delete {node_to_c_str(del_target, self.scope)}")

                case cst.Match(subject=subject, cases=cases):

                    def _match_case_to_c_str(pattern: cst.MatchPattern) -> str:
                        case_lines: list[str] = []
                        match pattern:
                            case cst.MatchValue(value=literal):
                                case_lines.append(f"{self.tabs}\tcase {node_to_c_str(literal, self.scope)}:")

                            case cst.MatchAs(pattern=None):
                                case_lines.append(f"{self.tabs}\tdefault:")

                            case cst.MatchAs(pattern=inner_pattern):
                                case_lines.append(_match_case_to_c_str(inner_pattern))

                            case cst.MatchOr(patterns=sub_patterns):
                                for option in sub_patterns:
                                    case_lines.append(_match_case_to_c_str(option))

                            case _:
                                raise SyntaxError(
                                    "Match statements only support: matching values, _ (default), as, | (or)"
                                )

                        return "\n".join(case_lines)

                    lines.append(f"{self.tabs}switch ({node_to_c_str(subject, self.scope)}) {{")
                    for case in cases:
                        lines.append(_match_case_to_c_str(case.pattern))
                        lines.append(f"{self.tabs}\t\t{{")

                        if isinstance(case.pattern, cst.MatchAs) and case.pattern.name is not None:
                            lines.append(
                                f"{self.tabs}\t\t\tauto {case.pattern.name.value} = {node_to_c_str(subject, self.scope)};"
                            )

                        body: Block = Block(case.body.body, self.tab_count + 3, self.scope)
                        lines.append(body.construct())
                        lines.append(f"{self.tabs}\t\t\tbreak;")

                        lines.append(f"{self.tabs}\t\t}}")

                    if lines[-2] == f"{self.tabs}\t\tbreak;":
                        lines.pop(-2)

                    lines.append(f"{self.tabs}}}")

                case cst.ImportFrom(module=module):
                    pyg3a.PyG3A.import_module(node_to_c_str(module, self.scope).replace(".", "/"))

                case cst.Import(names=modules):
                    for mod in modules:
                        pyg3a.PyG3A.import_module(node_to_c_str(mod.name, self.scope).replace(".", "/"))

                case cst.FunctionDef(name=cst.Name(value=func_name)) as func_def:
                    for func in pyg3a.Main.project.functions:
                        if func_name == func.name:
                            if func.name == "main" and not pyg3a.Main.main_function_overridden:
                                pyg3a.Main.main_function_overridden = True
                            else:
                                raise SyntaxError(f"Cannot override function '{func.name}'")

                    pyg3a.Main.project.add_func(func_def, self.scope)

                case cst.TypeAlias(
                    name=alias,
                    value=cst.Subscript(value=cst.Name(value=origin), slice=generic_args),
                    type_parameters=cst.TypeParameters(params=type_params),
                ):
                    type_param_names: list[str] = []
                    for param in type_params:
                        if isinstance(param.param, cst.TypeVar):
                            type_param_names.append(param.param.name.value)
                        else:
                            raise SyntaxError(f"Invalid type parameter: '{node_to_c_str(param.param, self.scope)}'")

                    generic_arg_types: list[Types.type] = []

                    for arg in generic_args:
                        if isinstance(arg.slice, cst.Index):
                            if isinstance(arg.slice.value, cst.Name) and arg.slice.value.value in type_param_names:
                                generic_arg_types.append(Types.TypeVar.named(arg.slice.value.value))
                            else:
                                generic_arg_types.append(cst_annotation_to_type(arg.slice.value, self.scope))
                        else:
                            raise SyntaxError(f"Invalid generic argument: '{node_to_c_str(arg, self.scope)}'")

                    if not (
                        origin in self.scope
                        and issubclass(self.scope[origin].type, Types.GenericType)
                        and self.scope[origin].value is not Never
                    ):
                        raise SyntaxError(f"'{node_to_c_str(origin, self.scope)}' is not a valid generic type")

                    self.scope.set_var(
                        alias,
                        Types.TypeAliasType,
                        Types.TypeAliasType(type_param_names, self.scope[origin].value, generic_arg_types),
                    )

                case cst.TypeAlias(name=alias, value=type_expr):
                    type_value: Types.type = cst_annotation_to_type(type_expr, self.scope)
                    if type_value:
                        self.scope.set_var(alias, type(type_value), type_value)
                    else:
                        raise SyntaxError(f"'{node_to_c_str(type_expr, self.scope)}' is not a valid type")

                case stmt if type(stmt) in CST_TO_C_EQV:
                    lines.append(f"{self.tabs}{CST_TO_C_EQV[type(stmt)]};")

                case _ as node:
                    raise SyntaxError(f"No support for {type(node)}: '{node_to_code(node)}'")
                # else:
                #     lines.append(f"{self.tabs}{Block._obj_to_c_str(expr, scope=self.scope)};")
        return "\n".join(lines)

    def _assignment_to_c_str(self, assign: cst.Assign | cst.AnnAssign, lines: list[str]) -> None:
        """
        Convert an assignment statement to C code

        :param assign: Assignment or annotated assignment statement.
        :param lines: List of strings to add the converted C code to.
        :raises SyntaxError: If a subscript of a variable not in scope is assigned to, or a tuple is unpacked to a variable not in scope
        """

        var_type: Types.type = Types.NotImplemented
        targets: list[cst.BaseAssignTargetExpression] = (
            [assign.target] if isinstance(assign, cst.AnnAssign) else [target.target for target in assign.targets]
        )

        for target in targets:
            if isinstance(assign, cst.AnnAssign):
                var_type = cst_annotation_to_type(assign.annotation.annotation, self.scope)
                pass
            else:
                match target:
                    case cst.Name() if target not in self.scope:
                        var_type = node_type(assign.value, self.scope)

                        if var_type is Types.Any:
                            logger.warning(
                                f"Type of '{node_to_code(target)}' not be determined - automatically set to any"
                            )

                    case cst.Subscript(value=(cst.Name(value=var_name))) if var_name not in self.scope:
                        raise SyntaxError(f"Type of '{var_name}' not defined in scope")

            match target:
                case cst.Tuple(elements):
                    tmp_var: str = pyg3a.PyG3A.gen_tmp_var(self.scope, "tuple_unpack")
                    lines.append(f"{self.tabs}auto {tmp_var} = {node_to_c_str(assign.value, self.scope)};")

                    for i, elt in enumerate(elements):
                        if isinstance(elt.value, cst.Name):
                            if elt.value.value == "_":
                                continue

                            if elt.value not in self.scope:
                                raise SyntaxError(f"type of variable '{elt.value.value}' must be defined in scope")

                            elif issubclass(self.scope[elt.value.value].type, Types.Pointer):
                                pyg3a.Main.project.includes.add("stddef.h")
                                lines.append(f"{self.tabs}if ({elt.value.value} != NULL) free({elt.value.value});")

                            lines.append(
                                f"{self.tabs}{node_to_c_str(
                                    elt.value, self.scope
                                )} = {tmp_var}._{i};"
                            )
                        else:
                            lines.append(
                                f"{self.tabs}{node_to_c_str(
                                    elt.value, self.scope
                                )} = {tmp_var}._{i};"
                            )

                case cst.Name() as var_name if var_name in self.scope:
                    if issubclass(self.scope[var_name].type, Types.Pointer):
                        pyg3a.Main.project.includes.add("stddef.h")
                        lines.append(f"{self.tabs}if ({var_name.value} != NULL) free({var_name.value});")

                    if assign.value:
                        lines.append(
                            f"{self.tabs}{node_to_c_str(target, self.scope)} = "
                            f"{node_to_c_str(assign.value, self.scope)};"
                        )
                    else:
                        raise SyntaxError(f"Cannot re-initialise variable '{var_name.value}'")

                case cst.Subscript(value=(cst.Name() as var_name)) if var_name in self.scope:
                    lines.append(
                        f"{self.tabs}{node_to_c_str(target, self.scope)} = "
                        f"{node_to_c_str(assign.value, self.scope)};"
                    )

                case cst.Name(value=var_name):
                    if assign.value:
                        lines.append(f"{self.tabs}{var_type} {var_name} = {node_to_c_str(assign.value, self.scope)};")
                    else:
                        lines.append(f"{self.tabs}{var_type} {var_name};")

            if isinstance(target, cst.Name) and var_type:
                self.scope.set_type(target, var_type)
                pyg3a.Main.project.includes.update(var_type.headers)
