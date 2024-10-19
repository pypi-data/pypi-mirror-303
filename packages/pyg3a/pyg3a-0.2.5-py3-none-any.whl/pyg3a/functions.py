#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Any, Optional, Sequence, override, TypedDict, NotRequired, Unpack

import libcst as cst

# Can't import from or we cause recursive imports
import pyg3a
from .block import Block
from .errors import NotAnnotatedError
from .logging import logger
from .node import node_to_code, node_type, node_to_c_str
from .scope import Scope
from .type_utils import cst_annotation_to_type
from .types import Types


class Parameter(cst.Param):
    """
    A positional or keyword argument in a :py:class:`libcst.Parameters` list.
    Always contains an :py:class:`libcst.Annotation`, and in some cases a ``default``.
    """

    annotation: cst.Annotation
    "A required :py:class:`libcst.Annotation`, used as a type hint."

    @override
    def __init__(self, parent: Optional[cst.Param] = None, **kwargs: Any):
        r"""
        Create a Parameter from either an annotated :py:class:`libcst.Param` or from keyword attributes.

        :param parent: Optional 'parent' :py:class:`libcst.Param` with defined :py:attr:`annotation`.
        :param \**kwargs: Attributes of the created class to be used if ``parent`` isn't specified, or to overwrite ``parent``'s.

        :raises NotAnnotatedError: If ``parent`` is not annotated.
        """

        if parent is None:
            super().__init__(**kwargs)
        else:
            if parent.annotation is None:
                raise NotAnnotatedError

            super().__init__(
                star=parent.star if "star" not in kwargs else kwargs["star"],
                whitespace_after_star=(
                    parent.whitespace_after_star
                    if "whitespace_after_star" not in kwargs
                    else kwargs["whitespace_after_star"]
                ),
                name=parent.name if "name" not in kwargs else kwargs["name"],
                annotation=parent.annotation if "annotation" not in kwargs else kwargs["annotation"],
                equal=parent.equal if "equal" not in kwargs else kwargs["equal"],
                default=parent.default if "default" not in kwargs else kwargs["default"],
                comma=parent.comma if "comma" not in kwargs else kwargs["comma"],
                whitespace_after_param=(
                    parent.whitespace_after_param
                    if "whitespace_after_param" not in kwargs
                    else kwargs["whitespace_after_param"]
                ),
            )


class FunctionData(TypedDict):
    name: NotRequired[str]
    ret: NotRequired[Types.type]
    node: NotRequired[cst.FunctionDef | None]
    statements: NotRequired[Sequence[cst.BaseStatement] | Sequence[cst.BaseSmallStatement]]
    params: NotRequired[list[Parameter]]
    scope: NotRequired[Scope]


class Function:
    name: str
    "Name of function."

    ret: Types.type
    "Return type."

    _node: cst.FunctionDef | None
    "Original CST node, optionally used to 'visit' it later when determining return type in :py:meth:`construct`."

    _statements: Sequence[cst.BaseStatement] | Sequence[cst.BaseSmallStatement]
    "List of statements (body) inside function."

    _params: list[Parameter]
    "List of parameters, all type-annotated."

    _scope: Scope
    "Inner scope of function."

    def __init__(self, func: cst.FunctionDef, parent_scope: Scope, **kwargs: Unpack[FunctionData]) -> None:
        """
        Create Function object from CST function definition.

        :param func: Function definition from the CST.
        :param parent_scope: Parent scope that the function is defined in (e.g. global scope for main()).
        :raises NotAnnotatedError: If any parameters don't have type annotations
        """

        # Save CST node
        self._node = kwargs["node"] if "node" in kwargs else func

        # Save name of function
        self.name = kwargs["name"] if "name" in kwargs else func.name.value

        # Save 'body' of function (list of expressions)
        self._statements = kwargs["statements"] if "statements" in kwargs else func.body.body

        # If return type is annotated, set self.ret to it
        if "ret" in kwargs:
            self.ret = kwargs["ret"]
        elif isinstance(func.returns, cst.Annotation):
            self.ret = cst_annotation_to_type(func.returns.annotation, parent_scope)
        else:
            self.ret = Types.Any

        # Raise SyntaxError if any parameters don't have an annotation, including all offenders in the error message
        if "params" not in kwargs:
            if missing_annotations := [str(i) for i, arg in enumerate(func.params.params) if arg.annotation is None]:
                raise NotAnnotatedError(
                    "Missing type annotation on parameter(s) "
                    + ", ".join(missing_annotations)
                    + " of function "
                    + self.name
                )

        # Save args as custom Parameter (forcing annotations to exist)
        self._params: list[Parameter] = (
            kwargs["params"] if "params" in kwargs else [Parameter(p) for p in func.params.params]
        )

        # Base scope inside function
        self._scope = (
            kwargs["scope"]
            if "scope" in kwargs
            else parent_scope.inner(
                [arg.name.value for arg in self._params],
                [cst_annotation_to_type(arg.annotation.annotation, parent_scope) for arg in self._params],
            )
        )

        # Save this function's type (return_type, [annotation_types]) to the global scope
        pyg3a.Main.globs.set_func(
            self.name,
            [cst_annotation_to_type(arg.annotation.annotation, self._scope) for arg in self._params],
            self.ret,
        )

    def __str__(self) -> str:
        """
        Create human-readable String containing all Function attributes.

        :returns: Function(name= :py:attr:`name`, params= :py:attr:`_params`, statements= :py:attr:`_statements`, ret= :py:attr:`ret`).
        """

        return (
            f"Function(\n\tname='{self.name}',\n\targs=({', '.join([node_to_code(p) for p in self._params])}),"
            f"\n\tstatements=[{'\n\t\t'.join([node_to_code(s) for s in self._statements])}],\n\tret='{self.ret}'\n)"
        )

    def __repr__(self) -> str:
        """
        Just use __str__ function for reprs.

        :returns: ``self.``:py:meth:`__str__`.
        """
        return str(self)

    def _str_params(self) -> str:
        """
        Helper function for :py:meth:`construct`, creating C-style list of parameters.

        :returns: comma-separated list of arguments in C format (``type name`` ).
        """

        return ", ".join(
            # <annotation -> C type str> <name>
            (
                f"{( "Args" if issubclass(cst_annotation_to_type(param.annotation.annotation, self._scope), Types.Any) else 
                     node_to_c_str(param.annotation.annotation, self._scope, is_type=True)) + "..."
                if "*" in param.star
                else node_to_c_str(param.annotation.annotation, self._scope, is_type=True)} {param.name.value}"
            )
            for param in self._params
        )

    def _signature(self) -> str:
        return (
            "template<class... Args> " if any("*" in p.star for p in self._params) else ""
        ) + f"{self.ret} {self.name}({self._str_params()})"

    def construct(self) -> str:
        """
        High-level construction of C function definition from stored attributes:
            #. Generates the base inner scope from function arguments.
            #. Constructs the inside of the function with this base scope (see :py:meth:`pyg3a.block.Block.construct`).
            #. Determines the function return type if previously unknown, using found return statements.
            #. Re-registers function to Main singleton with new return type.
            #. Adds function signature to start of constructed function lines.
            #. Adds ``GetKey(&key)`` forever-loop to end of function if ``main()`` function.
            #. Ends function and returns constructed lines.

        :returns: Newline-delimited constructed C function.
        """

        # Output function lines
        lines: list[str] = []

        # Add inside of function to ``lines``
        block: Block = Block(self._statements, 1, self._scope)
        lines.append(block.construct())

        # Save new scope
        self._scope = block.scope

        # Automatically find return type if unspecified
        if self.ret is Types.Any and self._node:
            # If there's no return statement, we're void/None
            self.ret = Types.NoneType

            # See :py:class:`FunctionVisitor`
            self._node.visit(FunctionVisitor(self, self._scope))

            # Re-register function type now we know what it is
            pyg3a.Main.globs.set_func(self.name, pyg3a.Main.globs[self.name].type.args[0], self.ret)

        # Add signature to ``lines``
        lines.insert(0, f"{self._signature()} {{")

        # If we're the main function, ensure that the app doesn't automatically exit when Python's main() function completes
        if self.name == "main":
            # Create a temp var inside the function's scope
            tmp_var: str = pyg3a.PyG3A.gen_tmp_var(self._scope, "key")
            pyg3a.Main.project.includes.add("fxcg/keyboard.h")
            lines.append(f"\tint {tmp_var}; while (1) GetKey(&{tmp_var});")

        # End the function and return
        lines.append("}")
        return "\n".join(lines)

    def declaration(self) -> str:
        return f"{self._signature()};"


@dataclass(slots=True)
class FunctionVisitor(cst.CSTVisitor):
    """
    Traverses the CST of a Function's FunctionDef node to find a :py:class:`libcst.Return` node to determine the Function's return type.
    """

    func: Function
    "Function to set the return type of."

    scope: Scope
    "Scope inside function."

    @override
    def leave_Return_value(self, node: cst.Return) -> None:
        """
        If we find a ``return`` statement, get the type of the returned object and set our Function's return type to that.
        If the type cannot be determined, the user is warned and the type is automatically set to ``any``.

        :param node: The :py:class:`libcst.Return` node we've encountered.
        """

        if node.value is None:
            self.func.ret = Types.NoneType
        else:
            self.func.ret = node_type(node.value, self.scope)
            if self.func.ret is Types.Any:
                logger.warning(f"Return type of '{self.func.name}' could not be determined - automatically set to any")
