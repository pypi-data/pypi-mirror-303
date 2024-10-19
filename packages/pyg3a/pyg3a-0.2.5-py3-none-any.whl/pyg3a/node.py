#!/usr/bin/env python3
import collections
import functools
from operator import and_
from typing import Never, Any, Final

import libcst as cst

import pyg3a
from .errors import CTypeNotConcreteError, FStringTooComplexError
from .logging import logger
from .py_consts import py_const_to_c_str, node_to_py_const, CSTConstant
from .scope import Scope
from .type_utils import cst_annotation_to_type
from .types import Types

CST_TO_C_EQV: Final[dict[type[cst.CSTNode], str]] = {
    # Statements
    cst.Break: "break",
    cst.Continue: "continue",
    cst.Pass: "/* PASS */",
    #
    # Comparison operators
    cst.Equal: "==",
    cst.Is: "==",
    cst.NotEqual: "!=",
    cst.IsNot: "!=",
    cst.GreaterThan: ">",
    cst.GreaterThanEqual: ">=",
    cst.LessThan: "<",
    cst.LessThanEqual: "<=",
    #
    # Logical operators
    cst.Or: "||",
    cst.And: "&&",
    cst.Not: "!",
    #
    # Numerical operators
    cst.Add: "+",
    cst.Subtract: "-",
    cst.Multiply: "*",
    cst.Divide: "/",
    cst.Modulo: "%",
    cst.Plus: "+",
    cst.Minus: "-",
    # cst.Power - covered in cst.BinaryOperation as it requires math.h.
    # cst.FloorDivide - covered in cst.BinaryOperation as it requires math.h.
    #
    # Binary operators
    cst.BitAnd: "&",
    cst.BitOr: "|",
    cst.BitXor: "^",
    cst.BitInvert: "~",
    cst.LeftShift: "<<",
    cst.RightShift: ">>",
    #
    # Operative assignment
    cst.AddAssign: "+=",
    cst.SubtractAssign: "-=",
    cst.MultiplyAssign: "*=",
    cst.DivideAssign: "/=",
    cst.ModuloAssign: "%=",
    cst.BitAndAssign: "&=",
    cst.BitOrAssign: "|=",
    cst.BitXorAssign: "^=",
    cst.LeftShiftAssign: "<<=",
    cst.RightShiftAssign: ">>=",
    # cst.FloorDivideAssign - covered in cst.AugAssign as it does not have a 1-1 in C
}
"Dictionary mapping CST node types to their C string equivalent."


def node_type(
    node: cst.CSTNode,
    scope: Scope,
) -> Types.type | Types.GenericType:
    """
    Determine type of CST node under the specified scope.

    :param node: The CST node to determine the type of.
    :param scope: The scope to find variables' types inside.
    :returns: A string representing the 'Python' type (see the type definitions in :py:class:`~pyg3a.pyg3a.Main`) of the specified ``node``.
    If the type cannot be determined, the ``any`` type is returned.
    :raises RuntimeError: If a variable is referenced with no type specified in ``scope``.
    """

    match node:
        # Ellipsis
        case cst.Ellipsis():
            return Types.EllipsisType

        # Numbers
        case cst.Imaginary():
            return Types.NotImplemented
        case cst.Integer():
            return Types.int
        case cst.Float():
            return Types.float

        # Strings
        case cst.BaseString():
            return Types.str

        # True, False, None
        case cst.Name(value="True"):
            return Types.bool
        case cst.Name(value="False"):
            return Types.bool
        case cst.Name(value="None"):
            return Types.NoneType

        # Variables
        case cst.Name(value=var_name):
            if var_name in scope:
                return scope[var_name].type
            raise RuntimeError(f"Variable {var_name} not found in scope")

        # Enums
        case cst.Attribute(value=cst.Name(value=enum), attr=cst.Name()) if enum in scope and issubclass(
            scope[enum].type, Types.EnumType
        ):
            return Types.int

        # Called functions
        case cst.Call(func=cst.Name(value=func_name)) if func_name in scope and isinstance(
            scope[func_name].type, Types.Callable
        ):
            return scope[func_name].type.args[1]
        case cst.Call(func=cst.Name(value=func_name)) if f"{func_name}__init__" in scope and isinstance(
            scope[f"{func_name}__init__"].type, Types.Callable
        ):
            return scope[f"{func_name}__init__"].type.args[1]
        case cst.Call(func=cst.Name(value="cast"), args=[cst.Arg(value=cst.Name(value=typ)), _]):
            return scope[typ].value

        # Iterable[Index]
        case cst.Subscript(value=iterable, slice=[cst.SubscriptElement(slice=cst.Index(value=index))]):
            return node_type(iterable, scope)[node_type(index, scope)]

        # Lambdas
        case cst.Lambda(params, body):
            return_type: Types.type | Types.GenericType = node_type(body, scope)
            if type(return_type) is Types.GenericType:
                raise CTypeNotConcreteError(return_type)
            return Types.Callable[[Types.Any for _ in params.posonly_params + params.params], return_type]

        # Sequences
        case cst.Tuple(elements):
            return Types.tuple[tuple([node_type(elem.value, scope) for elem in elements])]
        case cst.List(elements):
            return Types.list[node_type(elements[0].value, scope)]

        # Operators
        case cst.BinaryOperation(left=left, operator=operator, right=right):
            left_type: Types.type | Types.GenericType = node_type(left, scope)
            right_type: Types.type | Types.GenericType = node_type(right, scope)

            if issubclass(left_type, Types.Generic) or issubclass(right_type, Types.Generic):
                return Types.NotImplemented

            match operator:
                case cst.Add():
                    return left_type + right_type
                case cst.Subtract():
                    return left_type - right_type
                case cst.Multiply():
                    return left_type * right_type
                case cst.Divide():
                    return left_type / right_type
                case cst.Modulo():
                    return left_type % right_type
                case cst.Power():
                    return left_type**right_type
                case cst.FloorDivide():
                    return left_type // right_type
                case cst.LeftShift():
                    return left_type << right_type
                case cst.RightShift():
                    return left_type >> right_type
                case cst.BitAnd():
                    return left_type & right_type
                case cst.BitOr():
                    return left_type | right_type
                case cst.BitXor():
                    return left_type ^ right_type

        case cst.Comparison(left=left, comparisons=comparisons):
            comparison_types: list[Types.type] = []
            left_type: Types.type | Types.GenericType = node_type(left, scope)

            for comparison in comparisons:
                right_type: Types.type | Types.GenericType = node_type(comparison.comparator, scope)

                match comparison.operator:
                    case cst.Equal():
                        comparison_types.append(left_type == right_type)
                    case cst.NotEqual():
                        comparison_types.append(left_type != right_type)
                    case cst.LessThan():
                        comparison_types.append(left_type < right_type)
                    case cst.LessThanEqual():
                        comparison_types.append(left_type <= right_type)
                    case cst.GreaterThan():
                        comparison_types.append(left_type > right_type)
                    case cst.GreaterThanEqual():
                        comparison_types.append(left_type >= right_type)
                    case cst.In() | cst.NotIn() if isinstance(right_type, Types.Sequence):
                        comparison_types.append(Types.bool)
                    case cst.Is() | cst.IsNot():
                        comparison_types.append(Types.bool)

            # Get most derived base of comparison return types
            return next(iter(functools.reduce(and_, (collections.Counter(cls.mro()) for cls in comparison_types))))

    # Auto type if unsure
    return Types.Any


def node_to_code(node: cst.CSTNode) -> str:
    """
    Convert CST Node object to Python code.

    :param node: CST Node
    :returns: String containing Python code equivalent
    """
    return pyg3a.Main.codegen_module.code_for_node(node)


def _complex_f_string_content_to_str(content: cst.BaseFormattedStringContent, scope: Scope) -> tuple[str, ...]:
    if isinstance(content, cst.FormattedStringText):
        return (py_const_to_c_str(content.value.replace("}}", "}").replace("{{", "{").replace("%", "%%")),)

    # It's not a plain string
    assert isinstance(content, cst.FormattedStringExpression)

    fmt: str = ""
    expr_type: Types.type = node_type(content.expression, scope)
    exprs: list[str] = []

    if content.equal:
        fmt += f'{py_const_to_c_str(node_to_code(content.expression) + "=")} + '

    fmt += 'String("%") + '

    if content.format_spec:
        for f in content.format_spec:
            fmt_and_exprs = _complex_f_string_content_to_str(f, scope)
            if len(fmt_and_exprs) == 1:
                fmt += fmt_and_exprs[0]
            else:
                fmt += f"_sprintf({fmt_and_exprs[0]}, {', '.join(fmt_and_exprs[1:])})"

            fmt += " + "

    if issubclass(expr_type, Types.str):
        fmt += 'String("s")'
        exprs.append(f"{node_to_c_str(content.expression, scope)}.c_str()")
    elif issubclass(expr_type, Types.int):
        fmt += 'String("d")'
        exprs.append(node_to_c_str(content.expression, scope))
    elif issubclass(expr_type, Types.float):
        raise SyntaxError("Floats are not supported in f-strings")
    else:
        logger.warning("No conversion specifier determined for type, automatically using %s")
        fmt += 'String("s")'
        exprs.append(f"String({node_to_c_str(content.expression, scope)}).c_str()")

    return fmt, *exprs


def _f_string_content_to_str(content: cst.BaseFormattedStringContent, scope: Scope) -> tuple[str, ...]:
    if isinstance(content, cst.FormattedStringText):
        return (content.value.replace("}}", "}").replace("{{", "{").replace("%", "%%"),)

    # It's not a string
    assert isinstance(content, cst.FormattedStringExpression)

    fmt: str = ""
    expr_type: Types.type = node_type(content.expression, scope)
    exprs: list[str] = []

    if content.equal:
        fmt += f"{node_to_code(content.expression)}="

    fmt += "%"

    if content.format_spec:
        try:
            fmt += "".join(
                [
                    _f_string_content_to_str(f, scope)[0] if len(_f_string_content_to_str(f, scope)) == 1 else None
                    for f in content.format_spec
                ]
            )
        except TypeError:
            raise FStringTooComplexError()

    if issubclass(expr_type, Types.str):
        fmt += "s"
        exprs.append(f"{node_to_c_str(content.expression, scope)}.c_str()")
    elif issubclass(expr_type, Types.int):
        fmt += "d"
        exprs.append(node_to_c_str(content.expression, scope))
    elif issubclass(expr_type, Types.float):
        raise SyntaxError("Floats are not supported in f-strings")
    else:
        logger.warning("No conversion specifier determined for type, automatically using %s")
        fmt += "s"
        exprs.append(f"String({node_to_c_str(content.expression, scope)}).c_str()")

    return fmt, *exprs


def node_to_c_str(node: cst.CSTNode, scope, /, *, is_type=False) -> str:
    match node:
        # If we're calling a function
        case cst.Call():
            # If we have a custom function defined for this function
            try:
                return pyg3a.Main.project.modules.convert(node, scope)
            except KeyError:
                pass

            match node:
                # If we're casting a value
                case cst.Call(func=cst.Name(value="cast"), args=[cst.Arg(value=typ), cst.Arg(value=val)]):
                    return f"({cst_annotation_to_type(typ, scope)}) ({node_to_c_str(val, scope)})"
                case cst.Call(func=cst.Name(value=func_name), args=arguments) if func_name in scope and scope[
                    func_name
                ].type is Types.type and f"{func_name}__init__" in scope and isinstance(
                    scope[f"{func_name}__init__"].type, Types.Callable
                ):
                    return node_to_c_str(cst.Call(func=cst.Name(f"{func_name}__init__"), args=arguments), scope)
                case cst.Call(func=func, args=arguments):
                    # If no custom __pyg3a_, just run the function
                    return f"{node_to_c_str(func, scope)}({', '.join([node_to_c_str(arg.value, scope) for arg in arguments])})"

        case cst.Name(value=value) as const:
            # Constants
            if value in ("True", "False", "None"):
                return py_const_to_c_str(node_to_py_const(const))

            # Known variable (e.g. type)
            if value in scope and scope[value].value is not Never:
                ret: Any = scope[value].value

                if isinstance(ret, Types.type):
                    pyg3a.Main.project.includes.update(ret.headers)

                return str(ret)

            # Variable
            return value

        case cst.FormattedString(parts=parts):
            pyg3a.Main.project.modules.convert(cst.Call(func=cst.Name(value="__pyg3a_sprintf")), scope)

            try:
                fmt: str = ""
                args: list[str] = []

                for part in parts:
                    part_fmt_and_args = _f_string_content_to_str(part, scope)
                    fmt += part_fmt_and_args[0]
                    args.extend(part_fmt_and_args[1:])

                return f"_sprintf({py_const_to_c_str(fmt)}{', ' if args else ''}{', '.join(args)})"
            except FStringTooComplexError:
                fmt: list[str] = []
                args: list[str] = []

                for part in parts:
                    part_fmt_and_args = _complex_f_string_content_to_str(part, scope)
                    fmt.append(part_fmt_and_args[0])
                    args.extend(part_fmt_and_args[1:])

                return f"_sprintf({' + '.join(fmt)}{', ' if args else ''}{', '.join(args)})"

        # Other constants
        case node if isinstance(node, CSTConstant.__value__):
            const = node_to_py_const(node)

            # Explicit string types
            if is_type and isinstance(const, str):
                return const

            # Other constants
            return py_const_to_c_str(const)

        # Sli[c:e:s]
        case cst.Subscript(slice=[cst.SubscriptElement(slice=cst.Slice())]):
            raise SyntaxError("There is no support for slices")

        # GenericOrigin[args]
        case cst.Subscript(value=cst.Name(value=origin)) as generic if is_type and origin in scope and isinstance(
            scope[origin].type, Types.GenericType
        ) and scope[origin].value is not Never:
            return str(cst_annotation_to_type(generic, scope))

        # Array/list/class item access
        case cst.Subscript(value=collection, slice=[cst.SubscriptElement(cst.Index(value=index))]):
            # Otherwise translate our item access directly to C
            return f"{node_to_c_str(collection, scope)}[{node_to_c_str(index, scope)}]"

        # Translate Enum.member from stored enums
        case cst.Attribute(value=cst.Name(value=enum), attr=cst.Name(value=member)) if enum in scope and issubclass(
            scope[enum].type, Types.EnumType
        ):
            if scope[enum].value is not Never:
                return getattr(scope[enum].value, member)
            return member

        # struct.prop translates directly to C
        case cst.Attribute(value=struct, attr=cst.Name(prop)):
            return f"{node_to_c_str(struct, scope)}.{prop}"

        # Use CST_TO_C_EQV to translate comparisons, boolean, and unary operators
        case cst.Comparison(left, comparisons):
            # && separated comparisons
            return CST_TO_C_EQV[cst.And].join(
                [
                    f"{node_to_c_str(left, scope)} {CST_TO_C_EQV[type(comp.operator)]} "
                    f"{node_to_c_str(comp.comparator, scope)}"
                    for comp in comparisons
                ]
            )

        case cst.BooleanOperation(left, operator, right):
            return f"({node_to_c_str(left, scope)} {CST_TO_C_EQV[type(operator)]} {node_to_c_str(right, scope)})"

        case cst.UnaryOperation(operator, expression):
            return f"({CST_TO_C_EQV[type(operator)]} {node_to_c_str(expression, scope)})"

        case cst.BinaryOperation(left=left, operator=cst.Power(), right=right) if node_type(left, scope) ** node_type(
            right, scope
        ):
            # Use <math.h>'s pow function for power operators.
            pyg3a.Main.project.includes.add("math.h")
            return f"pow({node_to_c_str(left, scope)}, {node_to_c_str(right, scope)})"

        case cst.BinaryOperation(left=left, operator=cst.FloorDivide(), right=right) if node_type(
            left, scope
        ) // node_type(right, scope):
            # Use casts for C equivalent of floor division.
            # If left and right are integers => left / right == left // right
            if issubclass(node_type(left, scope), Types.int) and issubclass(node_type(right, scope), Types.int):
                return f"({node_to_c_str(left, scope)} / {node_to_c_str(right, scope)})"

            # Otherwise, round left / right and then convert it to a float
            return f"({node_type(left, scope) // node_type(right, scope)}) ((int) ({node_to_c_str(left, scope)} / {node_to_c_str(right, scope)}))"

        case cst.BinaryOperation(left, operator, right) as op:
            # Otherwise use CST_C_EQV for supported operations
            if node_type(op, scope):
                return f"({node_to_c_str(left, scope)} {CST_TO_C_EQV[type(operator)]} {node_to_c_str(right, scope)})"

            try:
                raise SyntaxError(
                    f"'{node_to_code(node)}': Unsupported types {(
                        node_type(left, scope)
                    )} and {(
                        node_type(right, scope)
                    )} for operation {type(operator).__name__}"
                )
            except CTypeNotConcreteError:
                raise SyntaxError(
                    f"'{node_to_code(node)}': Unsupported types {(
                        node_type(left, scope)
                    ).__name__} and {(
                        node_type(right, scope)
                    ).__name__} for operation {type(operator).__name__}"
                )

        # Walrus operator
        case cst.NamedExpr(target=cst.Name(value=var_name)) if var_name not in scope:
            # You can't declare a variable in the C equivalent ((int a = b) doesn't syntax correctly),
            # so it must be something already in scope
            raise SyntaxError(f"type of variable '{var_name}' must be defined in scope")

        case cst.NamedExpr(target, value):
            # a := b => a = b in C
            return f"({node_to_c_str(target, scope)} = {node_to_c_str(value, scope)})"

        # Lambdas
        case cst.Lambda(params=cst.Parameters(params), body=body):
            # You can't annotate lambda args, so we'll have to automatically determine their type
            args: list[str] = [f"auto {param.name.value}" for param in params]

            stmt: str = node_to_c_str(
                # Create inner scope from the lambda args with 'any' types
                body,
                scope.inner(params, "any"),
            )

            # Return outcome of lambda by default
            return f"[]({', '.join(args)}){{return {stmt};}}"

        # Ternary if
        case cst.IfExp(test, body, orelse=or_else):
            return f"({node_to_c_str(test, scope)} ? {node_to_c_str(body, scope)} : {node_to_c_str(or_else, scope)})"

        # Sets, tuples, lists are all struct initializers
        case cst.Set(elements) | cst.Tuple(elements) | cst.List(elements):
            return f"{{{', '.join([node_to_c_str(elt.value, scope) for elt in elements])}}}"

        # Catch-all error
        case _:
            raise SyntaxError(f"No support for {type(node)}: '{node_to_code(node)}'")
