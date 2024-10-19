from typing import override

from .sequence import CMutableSequence
from .generics import GenericArg
from .numbers import CInt
from .object import CObject, COpNotImplemented, CObjectMeta


class CList(CMutableSequence):
    """
    Lists are a mutable sequence with one generic arg which is the value returned when accessing an element.
    """

    args: tuple[type[CObject]]
    "Accepts one type object as an argument."

    headers: tuple[str] = ("list.hpp",)
    "Requires ``list.hpp`` to instantiate."

    @override
    def __subclasscheck__(self, subclass: type) -> bool:
        try:
            return super().__subclasscheck__(subclass)
        except NotImplementedError:
            # A[B] is a subclass of C[X] if X is a subclass of B
            if issubclass(subclass.args[0], self.args[0]):
                return True

        return False

    @override
    def sequence_access(self, other: type[CObject]) -> type[CObject]:
        if issubclass(other, CInt):
            return self.args[0]

        return COpNotImplemented

    @classmethod
    @override
    def acceptable_args(cls, bases: tuple[GenericArg, ...]) -> bool:
        return len(bases) == 1 and isinstance(bases[0], CObjectMeta)

    @classmethod
    @override
    def name(cls, bases: tuple[GenericArg, ...]) -> str:
        """
        Determines the name of a list instance.

        :param bases: A list of bases consisting of 1 :py:class:`pyg3a.types.object.CObject` .
        :returns: ``List<T>`` where T is the C++ equivalent of the base type.
        """
        return f"List<{bases[0]}>"
