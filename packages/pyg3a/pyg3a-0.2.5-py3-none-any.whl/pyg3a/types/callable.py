from types import EllipsisType
from typing import override, Callable

from .generics import GenericType, GenericArg
from .object import CObject, CObjectMeta


class CCallable(GenericType):
    """
    A function, lambda, or other callable type that may take parameters and may return a value.
    Callables can have a list of type objects representing the callable's parameter types, optionally ending in an ellipsis to indicate that
    further parameters are allowed. Alternatively, the list of parameters can be replaced with an ellipsis to indicate that any number of
    parameters are allowed.

    Callables also expect a type object (which can be :py:class:`~pyg3a.types.misc.CNoneType`) representing the callable's return type.
    """

    args: tuple[list[type[CObject] | EllipsisType] | EllipsisType, type[CObject]]
    "Accepts an ellipsis, or list of types, optionally followed by an ellipsis as parameters, and a return type."

    @override
    def __subclasscheck__(self, subclass: type) -> bool:
        try:
            return super().__subclasscheck__(subclass)
        except NotImplementedError:
            # A[B, C] is not a subclass of D[B, X] unless C is a subclass of X
            if not issubclass(subclass.args[1], self.args[1]):
                return False

            # A[B, C] is a subclass of A[..., C]
            if self.args[0] is ...:
                return True

            # A[B, C] is a subclass of D[X, C] if B is a subclass of X
            if (
                isinstance(self.args[0], list)
                and self.args[0][-1] is Ellipsis
                and all(
                    [
                        (
                            isinstance(arg, CObjectMeta)
                            and isinstance(subclass_arg, CObjectMeta)
                            and issubclass(subclass_arg, arg)
                        )
                        for arg, subclass_arg in zip(self.args[0][:-1], subclass.args[0][: len(self.args[0]) - 1])
                    ]
                )
            ):
                return True

        return False

    @classmethod
    @override
    def acceptable_args(cls, bases: tuple[GenericArg, ...]) -> bool:
        return (
            len(bases) == 2  # (Params, Return)
            and isinstance(bases[1], CObjectMeta)  # Return is a CObject
            and bases[0] is Ellipsis  # Either Params is an Ellipsis
            or (
                isinstance(bases[0], list)  # Or, Params is a list
                and len(bases[0]) == 0  # Which can be empty
                or (
                    all(
                        [isinstance(param, CObjectMeta) for param in bases[0][:-1]]
                    )  # Or, all Params are CObjects, except the last one
                    and (
                        isinstance(bases[0][-1], CObjectMeta) or bases[0][-1] is Ellipsis
                    )  # Which can be CObject or Ellipsis
                )
            )
        )

    @classmethod
    @override
    def name(cls, bases: tuple[GenericArg, ...]) -> str:
        """
        Determines the C function pointer type of this callable.

        :param bases: The arguments used to construct this type.
        :returns: A string representing its type, as used in casting.
        """
        return f"{bases[1]} (*)({'...' if bases[0] is Ellipsis else ', '.join(['...' if param is Ellipsis else str(param) for param in bases[0]])})"

    @classmethod
    def named(cls, bases: tuple[GenericArg, ...]) -> Callable[[str], str]:
        """
        Creates a lambda that can be used to declare a C function pointer of this callable.

        :param bases: The arguments used to construct this type.
        :returns: A lambda accepting a string argument as the name of the variable which returns its type declaration.
        """

        return (
            lambda name: f"{bases[1]} (*{name})({'...' if bases[0] is Ellipsis else ', '.join(['...' if param is Ellipsis else str(param) for param in bases[0]])})"
        )
