from .object import CObject, COpNotImplemented
from .numbers import CInt, CBool


class CStr(CObject):
    c = "String"

    @classmethod
    def __add__(cls, other: type[CObject]) -> type[CObject]:
        """
        String concatenation with a :py:class:`CStr` subclass returns the least derived class.
        """
        if issubclass(other, cls):
            return cls

        if issubclass(cls, other):
            return other

        return COpNotImplemented

    @classmethod
    def __mul__(cls, other: type[CObject]) -> type[CObject]:
        """
        Strings can be multiplied by subtypes of a :py:class:`CInt`.
        """
        if issubclass(other, CInt):
            return cls

        return COpNotImplemented

    @classmethod
    def __eq__(cls, other: type[CObject]) -> type[CObject]:  # type: ignore[override]
        """
        Strings can be equality-compared to return a :py:class:`CBool`.
        """
        if issubclass(other, cls) or issubclass(cls, other):
            return CBool

        return COpNotImplemented

    @classmethod
    def __ne__(cls, other: type[CObject]) -> type[CObject]:
        """
        Strings can be equality-compared to return a :py:class:`CBool`.
        """
        if issubclass(other, cls) or issubclass(cls, other):
            return CBool

        return COpNotImplemented

    @classmethod
    def __gt__(cls, other: type[CObject]) -> type[CObject]:
        """
        Strings can be equality-compared to return a :py:class:`CBool`.
        """
        if issubclass(other, cls) or issubclass(cls, other):
            return CBool

        return COpNotImplemented

    @classmethod
    def __lt__(cls, other: type[CObject]) -> type[CObject]:
        """
        Strings can be equality-compared to return a :py:class:`CBool`.
        """
        if issubclass(other, cls) or issubclass(cls, other):
            return CBool

        return COpNotImplemented
