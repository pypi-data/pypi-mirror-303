#!/usr/bin/env python3

from collections.abc import Mapping
from types import EllipsisType
from typing import Any, Final, Never, Optional, Sequence, cast, Self, NamedTuple, Iterable

import libcst as cst

from pyg3a.types import Types


class VariableInfo(NamedTuple):
    """
    Tuple representing a variable's type and value in a :py:class:`Scope`.
    """

    type: Types.type | type[Types.type]
    "The type of a variable or function."

    value: Any | Never = Never
    "The value of a variable or function, or Never if it is unknown/not set."


class Scope:
    """
    A high-level mapping of variable or function names to their types and values.
    """

    _data: Final[dict[str, VariableInfo]]
    "Internal mapping of variable names to their types and values."

    _parent: Final[Optional["Scope"]]
    "Optional (mutable) 'parent' scope, used to look up variables when not found in :py:attr:`_data`."

    __slots__ = "_data", "_parent"

    def __init__(
        self,
        parent: Optional[Self] = None,
        mapping: Optional[Mapping[str, VariableInfo | tuple[Types.type | type[Types.type], Any]]] = None,
        **kwargs: VariableInfo | tuple[Types.type | type[Types.type], Any],
    ) -> None:
        """
        Create a new scope from a mapping or kwargs, with optional parent.

        :param parent: Optional parent scope.
        :param mapping: Optional mapping of ``variable_name`` -> :py:class:`VariableInfo` or ``tuple(type, value)``.
        :param kwargs: Optional kwargs used as well as or instead of ``mapping``.
        """

        self._data = {}
        self._parent = parent

        if mapping is not None:
            for key in mapping:
                if isinstance(mapping[key], VariableInfo):
                    self._data[key] = mapping[key]
                else:
                    self._data[key] = VariableInfo(*mapping[key])
        if kwargs:
            for key, value in kwargs.items():
                if isinstance(value, VariableInfo):
                    self._data[key] = value
                else:
                    self._data[key] = VariableInfo(*value)

    def copy(self) -> "Scope":
        """
        Create a deep copy of this scope without changing the parent scope.
        """
        return Scope(self._parent, self._data.copy())

    def __getitem__(self, var: str | cst.Name) -> VariableInfo:
        """
        Get the type and value of a variable.

        :param var: The name of the variable or a :py:class:`cst.Name` node representing it.
        :returns: The type and value of the variable.
        :raises KeyError: If the variable is not found.
        """

        if (isinstance(var, str) and var in self._data) or (isinstance(var, cst.Name) and var.value in self._data):
            return self._data[var] if isinstance(var, str) else self._data[var.value]

        if self._parent and var in self._parent:
            return self._parent[var]

        raise KeyError

    def __contains__(self, var: str | cst.Name) -> bool:
        """
        Check if a variable is defined in this or the parent scope.
        If this returns ``True``, then :py:meth:`__getitem__` will return the type and value of the variable, \
        else :py:meth:`__getitem__` will raise a :py:class:`KeyError`.

        :param var: The name of the variable or a :py:class:`cst.Name` node representing it.
        :returns: ``True`` if the variable is defined in this or the parent scope, else ``False``.
        """
        return ((var in self._data) if isinstance(var, str) else (var.value in self._data)) or (
            var in self._parent if self._parent else False
        )

    def __setitem__(self, *_: Any) -> Never:
        raise TypeError("Use set_var, set_value, or set_type")

    def __repr__(self) -> str:
        return f"Scope(parent={self._parent!r}, mapping={self._data!r})"

    def __str__(self) -> str:
        return f"Scope(\n      parent={"\n      ".join(str(self._parent).split("\n"))},\n      {", \n      ".join([f"{name}: ({repr(typ)}, {repr(val)})" for name, (typ, val) in self._data.items()]) if self._data else "<no data>"}\n)"

    def __iter__(self) -> Iterable[tuple[str, VariableInfo]]:
        """
        Get iterator over internal variable_name -> variable_info mapping

        :returns: dict_items iterator of internal :py:attr:`_data` attribute.
        """
        return iter(self._data.items())

    def set_var(self, var: cst.Name, typ: Types.type | type[Types.type], value: Any | Never) -> None:
        """
        Set the type and value of a variable.

        :param var: The name of the variable or a :py:class:`cst.Name` node representing it.
        :param typ: The type of the variable.
        :param value: The value of the variable.
        :raises TypeError: If the variable name is of the wrong type, the variable name is empty, or the type is not a type object.
        """

        if not isinstance(var, cst.Name):
            raise TypeError("Variable name must be a libcst.Name node.")

        if not isinstance(typ, Types.type) and not (isinstance(typ, type) and issubclass(typ, Types.type)):
            raise TypeError("Passed type is not a type object.")

        self._data[var.value] = VariableInfo(typ, value)

    def set_func(self, name: str, param_types: list[Types.type] | EllipsisType, return_type: Types.type) -> None:
        """
        Set the parameter and return types of a function.

        :param name: The name of the function.
        :param param_types: The types of the parameters.
        :param return_type: The type of the return value.
        :raises TypeError: If the function name is empty.
        """

        if not name:
            raise TypeError("Function name empty.")

        if not (
            param_types == []
            or (isinstance(param_types, list) and all(isinstance(param, Types.type) for param in param_types))
            or param_types is ...
        ):
            raise TypeError("Invalid parameter types.")

        if not isinstance(return_type, Types.type):
            raise TypeError("Return type is not a type object.")

        self._data[name] = VariableInfo(Types.Callable[param_types, return_type])

    def set_value(self, var: cst.Name, value: Any | Never) -> None:
        """
        Set the value of a variable.

        :param var: The name of the variable or a :py:class:`cst.Name` node representing it.
        :param value: The value of the variable.
        :raises TypeError: If the variable name is empty or the variable is not already defined in this scope.
        """

        if not isinstance(var, cst.Name):
            raise TypeError("Variable name must be a libcst.Name node.")

        if var.value not in self._data:
            raise TypeError("Type unspecified - use set_var or set_type")

        self._data[var.value] = VariableInfo(self._data[var.value].type, value)

    def set_type(self, var: cst.Name, typ: Types.type | type[Types.type]) -> None:
        """
        Set the type of a variable.

        :param var: The name of the variable or a :py:class:`cst.Name` node representing it.
        :param typ: The type of the variable.
        :raises TypeError: If the variable name is of the wrong type, the variable name is empty, or the type is not a type object.
        """

        if not isinstance(var, cst.Name):
            raise TypeError("Variable name must be a libcst.Name node.")

        if not isinstance(typ, Types.type) and not (isinstance(typ, type) and issubclass(typ, Types.type)):
            raise TypeError("Passed type is not a type object.")

        self._data[var.value] = VariableInfo(typ, self._data[var.value].value if var.value in self._data else Never)

    def inner(
        self,
        var: Optional[str | cst.Param | Sequence[str] | Sequence[cst.Param]] = None,
        typ: Optional[Types.type | type[Types.type] | Sequence[Types.type | type[Types.type]]] = None,
    ) -> "Scope":
        """
        Create a new scope that is a child of this scope.
        Optionally, one or more variables' types can be set.
        If a sequence is passed to ``var`` or ``typ``, a sequence of the same length should be passed to the other.
        The parent will remain unchanged.

        :param var: Optional name of a new variable to set the type of, or a :py:class:`cst.Param` node representing it, \
        or a sequence of one of these.
        :param typ: Optional type of a new variable to set, or a sequence of types the same length as ``var``.
        :returns: The child scope.
        """
        if not var or not typ:
            return Scope(self)

        new_scope: Scope = Scope(self)
        variables: list[str]

        match var:
            case str():
                variables = [var]
            case cst.Param():
                variables = [var.name.value]
            case [*seq] if isinstance(seq[0], cst.Param):
                variables = [param.name.value for param in cast(Sequence[cst.Param], var)]
            case _:
                variables = list(cast(Sequence[str], var))

        if isinstance(typ, Types.type):
            for i in range(len(variables)):
                new_scope._data[variables[i]] = VariableInfo(typ)
        else:
            for i in range(min(len(variables), len(typ))):
                new_scope._data[variables[i]] = VariableInfo(typ[i])

        return new_scope
