#!/usr/bin/env python3

from typing import Final, Iterable, override, Any

from .functions import Function, FuncTypes
from .modules import Module
from ..scope import Scope

__all__ = "ModuleSet", "Module"


class ModuleSet:
    """
    A high-level wrapper allowing users to access interfaces on all modules in a set.
    """

    _funcs: Final[dict[type[FuncTypes], set[Function[FuncTypes]]]]
    "Mapping of function types to functions of that type within the added modules."
    _names: Final[set[str]]
    "Set of names of added modules."

    __slots__ = "_funcs", "_names"

    @override
    def __init__(self, iterable: Iterable[Module] = tuple()) -> None:
        """
        Create a new ModuleSet from an optional iterable of modules.

        :param iterable: An optional iterable of initial :py:class:`~pyg3a.modules.modules.Module` s.
        """

        # Generate blank sets by default
        self._funcs = {typ: set() for typ in FuncTypes.__args__}
        self._names = set()

        # If an iterable is passed, add its module names to our set and populate the function sets
        for module in iterable:
            self._names.add(module.name)

            for function in module.functions:
                self._funcs[function.typ].add(function)

    @override
    def __repr__(self) -> str:
        return f"ModuleSet({', '.join(self._names)})"

    def __contains__(self, module: str) -> bool:
        """
        Determine whether the specified module is contained within this set.

        :param module: The name of a module to check.
        :returns: True if the module is contained within this set, False otherwise.
        """
        return module in self._names

    def add(self, module: Module) -> None:
        """
        Add a module to the set.

        :param module: The :py:class:`~pyg3a.modules.modules.Module` to add.
        """

        self._names.add(module.name)
        for function in module.functions:
            self._funcs[function.typ].add(function)

    def contains(self, node: FuncTypes, scope: Scope) -> bool:
        """
        Determine whether this set provides a conversion for a specified node.

        :param node: The node to check. See :py:class:`~pyg3a.modules.functions.Function` for FuncTypes.
        :param scope: The node's enclosing scope.
        :returns: True if a conversion exists, False if it doesn't.
        """

        for fun in self._funcs[type(node)]:
            if fun.accepts(node, scope):
                return True
        return False

    def convert(self, node: FuncTypes, scope: Scope, **kwargs: Any) -> str:
        """
        Convert a node to its C string using this set's function converters.

        :param node: The node to convert. See :py:class:`~pyg3a.modules.functions.Function` for FuncTypes.
        :param scope: The node's enclosing scope.
        :param kwargs: Additional arguments to be passed to the converter. See \
        :py:class:`~pyg3a.modules.functions.FunctionInstance` for possible arguments.
        :returns: C string representation of the node.
        :raises KeyError: If a conversion does not exist within this set.
        """

        for fun in self._funcs[type(node)]:
            if inst := fun.accepts(node, scope):
                return inst.convert(**kwargs)
        raise KeyError(node)
