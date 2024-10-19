#!/usr/bin/env python3

import builtins
import functools
import inspect
import textwrap
from dataclasses import dataclass
from types import FunctionType, GenericAlias
from typing import Any, Final, NamedTuple, Never, Optional, TypeVar, cast, Callable

import libcst as cst

import pyg3a
from ..block import Block
from ..errors import NotAnnotatedError
from ..functions import Function as CFunction, Parameter as CSTParameter
from ..logging import logger
from ..node import node_to_code, node_type, node_to_c_str
from ..py_consts import node_to_py_const, Constant, CSTConstant
from ..scope import Scope
from ..type_utils import cst_annotation_to_type, py_annotation_to_type
from ..types import Types

FuncTypes = cst.Call | cst.For

# For some reason our type checkers can't figure this out
# Node = TypeVar("Node", *FuncTypes.__args__)
Node = TypeVar("Node", cst.Call, cst.For)


class Parameter(NamedTuple):
    """
    Tuple representing a parsed parameter.
    """

    name: str
    "The name of the Parameter."
    type: Types.type
    "Its Python type."
    default: Constant | Never
    "Its default value (must be a Python constant), or Never if no default is specified."
    to_arg: Callable[[cst.Arg, Scope], object]
    "The function used to convert an argument passed into this parameter into a C string or \
    other object to be used inside module functions."


def _gen_param(p: cst.Param) -> Parameter:
    """
    Generate a :py:class:`Parameter` from a :py:class:`libcst.Param` node.

    :param p: The CST Param node.
    :returns: A generated :py:class:`Parameter` tuple.
    :raises NotAnnotatedError: If the parameter is missing an annotation.
    :raises TypeError: If a non-constant default is set.
    """

    if p.annotation is None:
        raise NotAnnotatedError("Parameters must have annotations.")

    if p.default is not None and not isinstance(p.default, CSTConstant.__value__):
        raise TypeError("Default parameters must be constants.")

    if isinstance(p.annotation.annotation, cst.List):
        return Parameter(
            p.name.value,
            Types.tuple[*[cst_annotation_to_type(el.value) for el in p.annotation.annotation.elements]],
            Never if p.default is None else node_to_py_const(cast(CSTConstant, p.default)),
            lambda arg, scope: [node_to_c_str(elem.value, scope) for elem in arg.value.elements],
        )

    return Parameter(
        p.name.value,
        cst_annotation_to_type(p.annotation.annotation),
        Never if p.default is None else node_to_py_const(cast(CSTConstant, p.default)),
        lambda arg, scope: node_to_c_str(arg.value, scope),
    )


def importer(
    name: str,
    _globs: Optional[dict[str, Any]] = None,
    locals: Optional[dict[str, Any]] = None,
    *_args: Any,
) -> None:
    """
    Custom __import__ function used when executing module functions.
    Includes the specified header into the output C++.

    :param name: The header name to import (see :py:meth:`~pyg3a.Project.include_from_python_name`).
    :param _globs: Globals dictionary from the import statement's scope.
    :param locals: Locals dictionary from the import statement's scope.
    :param _args: Unused arguments passed by import statements.
    :raises ImportError: If a local variable has already been defined which including this header would override.
    """

    if locals and name.split(".", maxsplit=1)[0] in locals:
        raise ImportError("Cannot import module with same name as local variable", name=name)

    pyg3a.Main.project.include_from_python_name(name)


def _c_func_decorator(parent_mod_name: str, func: FunctionType) -> None:
    """
    Decorator used when executing module functions.

    Denotes that the decorated ``func`` represents a raw C function.

    Under the hood it adds a C function whose signature is translated from ``func``'s,
    and whose body is the output of running ``func`` with ``None`` passed as all arguments.
    This function is added to :py:attr:`~pyg3a.pyg3a.Main.globs`.

    :param parent_mod_name: The name of the module the decorated function is defined in.
    :param func: The decorated function.
    :raises NotAnnotatedError: If there is no return type specified for ``func``.
    """

    if "return" not in func.__annotations__:
        raise NotAnnotatedError(f"No return annotation on function {func.__name__}() from module '{parent_mod_name}'")

    ret: Types.type = py_annotation_to_type(func.__annotations__["return"])

    func_c_body: str = textwrap.indent(textwrap.dedent(func(*((None,) * func.__code__.co_argcount))), "\t").strip()

    pyg3a.PyG3A.add_c_func(
        func.__name__,
        CFunction(
            cst.FunctionDef(name=cst.Name(value=func.__name__), params=cst.Parameters(), body=cst.IndentedBlock([])),
            pyg3a.Main.globs,
            name=func.__name__,
            ret=ret,
            node=None,
            statements=[cst.parse_statement(f'raw_c("""{func_c_body}""")')],
            params=[
                CSTParameter(
                    name=cst.Name(value=param.name),
                    annotation=cst.Annotation(
                        annotation=cst.SimpleString(value=f"'{py_annotation_to_type(param.annotation)}'")
                    ),
                    star="*" if param.kind == param.VAR_POSITIONAL else "**" if param.kind == param.VAR_KEYWORD else "",
                    default=(cst.parse_expression(str(param.default)) if param.default is not param.empty else None),
                )
                for param in inspect.signature(func).parameters.values()
            ],
        ).construct(),
        [py_annotation_to_type(ann) for name, ann in func.__annotations__.items() if name != "return"],
        ret,
    )


def _struct_c_func_decorator(parent_mod_name: str, func: FunctionType) -> None:
    """
    Decorator used when executing module functions.

    Denotes that the decorated ``func`` represents a raw C function that returns
    a struct which we should treat as a tuple.

    Under the hood it creates a struct named __pyg3a_struct_``function name`` with the same fields as
    the struct returned by ``func``. Then it adds a C function whose signature is translated from ``func``'s,
    and whose body is the output of running ``func`` with ``None`` passed as all arguments.
    This function is added to :py:attr:`~pyg3a.pyg3a.Main.globs`, and the struct is added
    to the :py:attr:`~pyg3a.pyg3a.Main.type_registry`.

    :param parent_mod_name: The name of the module the decorated function is defined in.
    :param func: The decorated function.
    :raises NotAnnotatedError: If there is no return type specified for ``func``.
    :raises TypeError: If the return type is not a tuple.
    """

    if "return" not in func.__annotations__:
        raise NotAnnotatedError(f"No return annotation on function {func.__name__}() from module '{parent_mod_name}'")

    if not (
        isinstance(func.__annotations__["return"], GenericAlias) and func.__annotations__["return"].__origin__ is tuple
    ):
        raise TypeError("@struct_c_func can only be used on functions that return a tuple")

    func_c_body: str = textwrap.indent(textwrap.dedent(func(*((None,) * func.__code__.co_argcount))), "\t").strip()
    struct_name: str = f"__pyg3a_struct_{func.__name__}"

    struct_type: Types.SpecificTuple = Types.SpecificTuple.struct(struct_name)[
        tuple(py_annotation_to_type(t) for t in func.__annotations__["return"].__args__)
    ]

    # Add struct to C project
    pyg3a.PyG3A.add_c_func(
        struct_name,
        f"struct {struct_name} {{\n"
        + "\n".join(
            [f"\t{py_annotation_to_type(t)} _{i};" for i, t in enumerate(func.__annotations__["return"].__args__)]
        )
        + "\n};",
        [py_annotation_to_type(t) for t in func.__annotations__["return"].__args__],
        struct_type,
    )

    # Add struct type to global scope now that C is set
    pyg3a.Main.globs.set_var(cst.Name(struct_name), Types.SpecificTuple, struct_type)

    # Adjust the return annotation for later
    func.__annotations__["return"] = struct_name

    def init(self: object) -> None:
        self.__repr__ = lambda: struct_name

    struct_annotation: type = type(struct_name, (), {"__slots__": "__repr__", "__init__": init})

    pyg3a.PyG3A.add_c_func(
        func.__name__,
        CFunction(
            cast(
                cst.FunctionDef,
                cst.parse_statement(
                    # Map struct_name: str(struct_name) so we evaluate it to itself
                    f'def {func.__name__}{inspect.signature(
                        func,
                        globals={struct_name: struct_annotation()},
                        eval_str=True
                    )}:\n\traw_c("""{func_c_body}""")'
                ),
            ),
            pyg3a.Main.globs,
        ).construct(),
        [py_annotation_to_type(ann) for name, ann in func.__annotations__.items() if name != "return"],
        py_annotation_to_type(func.__annotations__["return"]),
    )


def _syscall_decorator(parent_mod_name: str, number: int) -> Callable[[FunctionType], None]:
    """
    Decorator used when executing module functions.

    This adds a new function which runs syscall ``number`` to :py:attr:`~pyg3a.pyg3a.Main.globs` whose \\
    name and signature is that of the decorated function.

    :param parent_mod_name: The name of the module the decorated function is defined in.
    :param number: The syscall's number (usually specified in hexadecimal).
    :raises NotAnnotatedError: If there is no return type specified for ``func``.
    """

    def wrapper(func: FunctionType) -> None:
        if "return" not in func.__annotations__:
            raise NotAnnotatedError(
                f"No return annotation on function {func.__name__}() from module '{parent_mod_name}'"
            )

        ret_annotation: Types.type = py_annotation_to_type(func.__annotations__["return"])
        param_annotations: dict[str, Types.type] = {
            p_name: py_annotation_to_type(p_ann) for p_name, p_ann in func.__annotations__.items() if p_name != "return"
        }

        pyg3a.PyG3A.add_c_func(
            f"__pyg3a_asm_{func.__name__}",
            f'extern "C" {ret_annotation} {func.__name__}({
            ', '.join(
                [
                    f"{ann} {name}" for name, ann in param_annotations.items()
                ]
            )
            }); \
            __asm__(".text; .align 2; .global _{func.__name__}; _{func.__name__}: \
                    mov.l sc_addr, r2; mov.l 1f, r0; jmp @r2; nop; 1: .long {number}; sc_addr: .long 0x80020070");',
            list(param_annotations.values()),
            ret_annotation,
        )

    return wrapper


@dataclass(slots=True, init=False, unsafe_hash=True)
class Function[Node]:
    """
    High-level generic representation of a module function for a specific Node type.

    Currently supporting :py:class:`libcst.Call` and :py:class:`libcst.For`.
    """

    name: Final[str]
    "The name of this function."

    parent_mod_name: Final[str]
    "The name of the module this function is defined in."

    func_def: Final[cst.FunctionDef]
    "The underlying :py:class:`libcst.FunctionDef` for this function."

    typ: type[Node]
    "The :py:class:`libcst.Call` or :py:class:`libcst.For` type of this function."

    params: Final[tuple[Parameter, ...]]
    "Standard parameters for this function."

    posonly_params: Final[tuple[Parameter, ...]]
    "Positional-only parameters for this function."

    kwonly_params: Final[tuple[Parameter, ...]]
    "Keyword-only parameters for this function."

    starargs: Final[Optional[Parameter]]
    "Optional parameter collecting all other positional arguments for this function."

    kwargs: Final[Optional[Parameter]]
    "Optional parameter collecting all other keyword arguments for this function."

    def __init__(self, func_def: cst.FunctionDef, parent_mod_name: str, typ: type[Node]) -> None:
        """
        Initialise the function from a CST definition, generating and classifying its parameters and adding it
        to :py:attr:`~pyg3a.pyg3a.Main.globs`.

        :param func_def: The CST definition of this function.
        :param parent_mod_name: The name of the module this function is defined in.
        :param typ: The :py:class:`libcst.Call` or :py:class:`libcst.For` type of this function. This should match
        its generic ``Node`` type.
        :raises TypeError: If the function is a :py:class:`libcst.For` and has no positional params.
        :raises NotAnnotatedError: If there is no return type annotated in the ``func_def``.
        """
        self.typ = typ

        self.name = func_def.name.value if self.typ is cst.Call else func_def.name.value.split("__iter__")[0]
        self.parent_mod_name = parent_mod_name
        self.func_def = func_def

        if self.typ is cst.For:
            # If the __iter__ function has pos-only params, then the first one is the var name
            # (i.e. it's not passed in by calls)
            if func_def.params.posonly_params:
                self.posonly_params = tuple([_gen_param(param) for param in func_def.params.posonly_params[1:]])
                self.params = tuple([_gen_param(param) for param in func_def.params.params])

            # Else if the __iter__ function has standard params, then the first one is the var name
            elif func_def.params.params:
                self.posonly_params = tuple([_gen_param(param) for param in func_def.params.posonly_params])
                self.params = tuple([_gen_param(param) for param in func_def.params.params[1:]])

            # We don't support passing the var name as a keyword param, so error
            else:
                raise TypeError("__iter__ functions must have a positional parameter to pass the var name into")
        else:
            self.posonly_params = tuple([_gen_param(param) for param in func_def.params.posonly_params])
            self.params = tuple([_gen_param(param) for param in func_def.params.params])

        self.kwonly_params = tuple([_gen_param(param) for param in func_def.params.kwonly_params])

        self.kwargs = _gen_param(func_def.params.star_kwarg) if func_def.params.star_kwarg else None
        self.starargs = (
            _gen_param(func_def.params.star_arg) if isinstance(func_def.params.star_arg, cst.Param) else None
        )

        if func_def.returns is None:
            raise NotAnnotatedError("Return type must be annotated")

        pyg3a.Main.globs.set_func(
            self.name,
            [param.type for param in self.posonly_params + self.params + self.kwonly_params],
            cst_annotation_to_type(func_def.returns.annotation),
        )

    def accepts(self, node: Node, scope: Scope) -> Optional["FunctionInstance[Node]"]:
        """
        Check if this function accepts the given node.

        :param node: The node to check.
        :param scope: The enclosing scope the node is referenced in.
        :returns: A :py:class:`FunctionInstance` generated from ``node`` and ``scope``
        if the function accepts the node, else None.
        """

        inst: FunctionInstance[Node] = FunctionInstance[Node](self, node, scope)
        if inst.acceptable():
            return inst

        return None


# noinspection PyFinal
@dataclass(slots=True)
class FunctionInstance[Node]:
    """
    Instance of a :py:class:`Function` for a specific node and scope.
    """

    function: Final[Function[Node]]
    "The :py:class:`Function` this is an instance of."

    node: Final[Node]
    "The node this function is called with."

    scope: Final[Scope]
    "The enclosing scope the node is referenced in."

    complete_args: list[cst.Arg | Parameter] = lambda: []
    "A complete list of passed arguments and parameters to this function. Generated in :py:meth:`acceptable()`"

    def acceptable(self) -> bool:
        """
        Determine if this instance's node and scope are acceptable for this instance's function.

        Also generates :py:attr:`complete_args`.

        :returns: True if the node is acceptable, else False.
        :raises AssertionError: If the node is a :py:class:`libcst.For` and it's not iterating over a function call.
        """

        # All For nodes are iterating over a callable
        if self.function.typ is cst.For:
            assert isinstance(self.node.iter, cst.Call)

        call: cst.Call = self.node.iter if self.function.typ is cst.For else self.node

        # If we're not calling a function with the same name as ours, don't accept
        if self.function.name != node_to_c_str(call.func, self.scope):
            return False

        # If too many args, we don't accept
        if (
            not self.function.kwargs
            and not self.function.starargs
            and len(call.args)
            > (len(self.function.params) + len(self.function.kwonly_params) + len(self.function.posonly_params))
        ):
            logger.debug("2")
            return False

        # If not enough args for just standard params, short-circuit and don't accept
        if len(call.args) < len([p for p in self.function.params if p.default is Never]):
            logger.debug("3")
            return False

        # Get the passed positional args
        pos_args: list[cst.Arg] | None = []
        kw_args: list[cst.Arg] | None = []

        for arg in call.args:
            if arg.keyword:
                # We're not worrying about evaluating **kwargs arguments
                if arg.star:
                    kw_args = None
                elif kw_args is not None:
                    kw_args.append(arg)
            else:
                # We're not worrying about evaluating *args arguments
                if arg.star:
                    pos_args = None
                elif pos_args is not None:
                    pos_args.append(arg)

        # If we can't process the pos and kw arg counts, short-circuit to accept
        if kw_args is None and pos_args is None:
            logger.debug("4")
            return True

        # Expanded list of arguments or their parameters if defaulted
        self.complete_args: list[cst.Arg | Parameter] = []

        # The number of positional args
        checked_posargs: int = 0

        # If pos_args is None, we won't process the posargs
        if pos_args is not None:
            # Now we'll check the positional arguments
            self.complete_args.extend(pos_args)

            # Fill in with posonly defaults
            if len(pos_args) < len(self.function.posonly_params):
                for param in self.function.posonly_params[checked_posargs:]:

                    # If we haven't specified an argument, and it doesn't have a default param, don't accept
                    if param.default is Never:
                        logger.debug("5")
                        return False

                    # Otherwise add the default's type to the list of specified args
                    self.complete_args.append(param)
                    checked_posargs += 1

            checked_posargs = len(pos_args) - len(self.function.posonly_params)

            # If we have too many positional params to fill, don't accept
            if checked_posargs > len(self.function.params):
                logger.debug("6")
                return False

        # If kw_args is None, we won't process the kwargs
        if kw_args is not None:
            # Map argument names
            arg_map: dict[str, cst.Arg] = {arg.keyword.value: arg for arg in kw_args}

            # Now generate the complete_args from our map
            for param in self.function.params[checked_posargs:] + self.function.kwonly_params:
                # Use default if necessary
                if param.name not in arg_map:
                    # If it's not specified and there's no default, don't accept
                    if param.default is Never:
                        logger.debug("7")
                        return False

                    # Otherwise add the default's type to the list of specified args
                    self.complete_args.append(param)
                else:
                    self.complete_args.append(arg_map[param.name])

        # This should hopefully work, but really I should write a test for it
        try:
            for arg, param in zip(
                self.complete_args,
                (self.function.posonly_params if pos_args is not None else tuple())
                + (self.function.params + self.function.kwonly_params if kw_args is not None else tuple()),
                strict=True,
            ):
                if isinstance(arg, Parameter):
                    # We must have defaulted so let's assume for now that it's fine
                    continue

                if not issubclass(node_type(arg.value, self.scope), param.type):
                    logger.debug("8")
                    logger.debug(self.function.name)
                    logger.debug(arg.value)
                    logger.debug(node_type(arg.value, self.scope))
                    return False
        except ValueError:
            logger.debug("9")
            return False

        return True

    def _call_get_args(self) -> tuple[list[object], dict[str, object]]:
        """
        Get this instance's positional and keyword arguments to pass to its function.

        This requires having run :py:meth:`__init__` first to generate :py:attr:`complete_args`.

        :returns: A tuple of (positional arguments, keyword name: keyword arguments).
        """

        return (
            [
                # Convert the argument to a string or other type, according to the parameter's to_arg()
                param.to_arg(arg, self.scope)
                for arg, param in zip(
                    # All passed arguments/default parameters
                    self.complete_args,
                    # All function params
                    self.function.posonly_params + self.function.params + self.function.kwonly_params,
                )
                # Only convert non-keyword arguments. Default params are all at the end so don't bother.
                if isinstance(arg, cst.Arg) and not arg.keyword
            ],
            {
                # Convert the argument to a string or other type, according to the parameter's to_arg()
                arg.keyword.value: param.to_arg(arg, self.scope)
                for arg, param in zip(
                    # All passed arguments/default parameters
                    self.complete_args,
                    # All function params
                    self.function.posonly_params + self.function.params + self.function.kwonly_params,
                )
                # Only convert keyword arguments. Default params are all at the end so don't bother.
                if isinstance(arg, cst.Arg) and arg.keyword
            },
        )

    def _call_converter(self) -> str:
        """
        Converter implementation for :py:class:`libcst.Call` nodes.

        :returns: The C equivalent of the function call.
        """

        args, kwargs = self._call_get_args()
        return self._eval_module_func(*args, **kwargs)

    def _eval_module_func(self, *args: str, **kwargs: str) -> str:
        """
        Evaluate this instance's function with specified positional and keyword arguments.

        Under the hood, this reconstructs the instance's function definition without any annotations, then defines
        new builtins such as ``__import__`` to include and ``eval`` to evaluate safely, defines decorators,
        generates the new function definition code, and calls the function with a mangled name.

        :param args: Positional arguments to pass to the function.
        :param kwargs: Keyword arguments to pass to the function.
        :returns: The C equivalent of the function call.
        :raises RuntimeError: If the called function doesn't return a non-empty string.
        """

        func_def: cst.FunctionDef = self.function.func_def

        untyped_funcdef: cst.FunctionDef = cst.FunctionDef(
            name=cst.Name(f"__pyg3a_{self.function.name}"),
            body=(
                cst.IndentedBlock(
                    body=[cst.SimpleStatementLine(body=[cst.Expr(cst.Call(func=cst.Name("locals")))])]
                    + list(func_def.body.body),
                    indent=func_def.body.indent,
                )
                if isinstance(func_def.body, cst.IndentedBlock)
                else cst.SimpleStatementSuite(
                    body=[cst.Expr(cst.Call(func=cst.Name("locals")))]
                    + list(cast(cst.SimpleStatementSuite, func_def.body).body)
                )
            ),
            params=cst.Parameters(
                params=[cst.Param(param.name, default=param.default) for param in func_def.params.params],
                star_arg=(
                    cst.Param(func_def.params.star_arg.name, default=func_def.params.star_arg.default)
                    if type(func_def.params.star_arg) is cst.Param
                    else func_def.params.star_arg
                ),
                kwonly_params=[cst.Param(param.name, default=param.default) for param in func_def.params.kwonly_params],
                star_kwarg=(
                    cst.Param(func_def.params.star_kwarg.name, default=func_def.params.star_kwarg.default)
                    if func_def.params.star_kwarg
                    else None
                ),
                posonly_params=[
                    cst.Param(param.name, default=param.default) for param in func_def.params.posonly_params
                ],
                posonly_ind=func_def.params.posonly_ind,
            ),
        )

        custom_builtins: dict[str, Any] = builtins.__dict__.copy()
        custom_builtins["__import__"] = importer
        custom_builtins["eval"] = lambda code: eval(code, {"__builtins__": {}}, {})
        custom_builtins["exec"] = lambda code: eval(code, {"__builtins__": {}}, {})

        globs: dict[str, Any] = {
            "__builtins__": custom_builtins,
            "c_func": functools.partial(_c_func_decorator, self.function.parent_mod_name),
            "struct_c_func": functools.partial(_struct_c_func_decorator, self.function.parent_mod_name),
            "syscall": functools.partial(_syscall_decorator, self.function.parent_mod_name),
        }

        def init(sel: object, name: str) -> None:
            sel.__repr__ = lambda: name

        for custom_type, (typ, _) in pyg3a.Main.globs:
            if issubclass(typ, Types.type) and custom_type not in builtins.__dict__:
                globs[custom_type] = type(
                    custom_type, (), {"__slots__": "__repr__", "__init__": functools.partial(init, name=custom_type)}
                )

        exec(node_to_code(untyped_funcdef), globs)

        evaluated: Any = globs[f"__pyg3a_{self.function.name}"](*args, **kwargs)
        if evaluated and isinstance(evaluated, str):
            return cast(str, evaluated)

        raise RuntimeError(
            f"Function '{self.function.name}' from module '{self.function.parent_mod_name}' did not return a string."
        )

    def _iter_converter(self, tab_count: int) -> str:
        """
        Converter implementation for :py:class:`libcst.For` nodes.

        :param tab_count: The number of tabs to use for indentation.
        :returns: The C equivalent of the for loop.
        """
        assert isinstance(self.node, cst.For)

        args, kwargs = self._call_get_args()
        args.insert(0, self.node.target.value)
        lines: list[str] = [f"{tab_count * "\t"}for ({self._eval_module_func(*args, **kwargs)}) {{"]

        if self.function.func_def.returns is None:
            raise TypeError

        expressions = Block(
            self.node.body.body,
            tab_count + 1,
            self.scope.inner(
                self.node.target.value, cst_annotation_to_type(self.function.func_def.returns.annotation, self.scope)
            ),
        )
        lines.append(expressions.construct())

        lines.append(tab_count * "\t" + "}")

        return "\n".join(lines)

    def convert(self, **kwargs: Any) -> str:
        """
        Convert this function instance into a C string.

        :param kwargs: Keyword arguments to pass to the node type's specific conversion implementation.
        :returns: The C equivalent of the node.
        """

        return self._call_converter() if self.function.typ is cst.Call else self._iter_converter(**kwargs)
