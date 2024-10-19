import abc
from types import EllipsisType
from typing import Iterable

from .object import CObjectMeta, CObject, classproperty

type GenericArg = EllipsisType | type[CObject] | list[GenericArg]


class GenericType(CObjectMeta, abc.ABCMeta):  # type: ignore[misc,valid-type] # mypy complains about our metaclass
    """
    Abstract metaclass for Python generic/C++ template types.
    Can take any number of arguments, which may be ellipses, C++ types, or a list of arguments.
    """

    origin: type["GenericType"]
    "The original generic type."

    args: tuple[GenericArg, ...]
    "The arguments given to create this generic."

    @classmethod
    def _generate_class_name(cls, bases: tuple[GenericArg, ...]) -> str:
        """
        Helper method to generate the name of a generic class created by this metaclass.

        :param bases: The arguments given to create this generic.
        :return: The 'hashed' name of the class.
        """
        return f"{cls.__name__}_{"_".join([b.__name__ if isinstance(b, type) else str(b) for b in bases])}"

    @classmethod
    @abc.abstractmethod
    def name(cls, bases: tuple[GenericArg, ...]) -> str | None:
        """
        Function to generate the name of a generic created by this metaclass from the given bases.

        :param bases: The arguments given to create this generic.
        :returns: The name of the class, or ``None`` if the class is not concrete.
        """
        ...

    @classmethod
    @abc.abstractmethod
    def acceptable_args(cls, bases: tuple[GenericArg, ...]) -> bool:
        """
        Determine whether the given bases are acceptable arguments for this generic.

        :param bases: The arguments given to create this generic.
        :returns: ``True`` if the arguments are acceptable, ``False`` otherwise.
        """
        ...

    @classproperty
    def headers(cls) -> Iterable[str]:
        """
        Property to get the C++ headers to import on usage.
        """
        return tuple()

    @classproperty
    def _base_classes(cls) -> Iterable[type[CObject]]:
        """
        Property for the base classes of instances of this generic.
        """
        return (CObject,)

    def __subclasscheck__(self, subclass: type) -> bool:
        """
        Determine whether this generic type is a subclass of another type.

        :param subclass: The type to check against.
        :returns: ``True`` if this generic is a subclass of ``subclass``, ``False`` otherwise.
        :raises NotImplementedError: If it cannot be determined and should be handled by the implementation of this generic.
        """
        # A[B] is subclass of C if C inherits A[B]
        if type.__subclasscheck__(self, subclass):
            return True

        # A[B] is not a subclass of C if C is not a generic
        if not isinstance(subclass, GenericType):
            return False

        # A[B] is not a subclass of C[X] if C does not inherit A
        if not issubclass(subclass.origin, self.origin):
            return False

        # A[B] is a subclass of C[X] if X == B
        if self.args == subclass.args:
            return True

        # A[B, C] is a subclass of D[X, Y] if B is a subclass of X and C is a subclass of Y
        if all(
            [
                (
                    isinstance(arg, CObjectMeta)
                    and isinstance(subclass_arg, CObjectMeta)
                    and issubclass(subclass_arg, arg)
                )
                or arg == subclass_arg
                for arg, subclass_arg in zip(self.args, subclass.args)
            ]
        ):
            return True

        raise NotImplementedError

    def __class_getitem__(cls, *args: GenericArg) -> "GenericType":
        """
        Create an instance of this generic with the given arguments.

        :param args: The arguments to use to create this generic.
        :returns: An instance of this generic with the given arguments.
        """
        type_args: tuple[GenericArg, ...] = args[0] if isinstance(args[0], tuple) else args

        if not cls.acceptable_args(type_args):
            return GenericNotImplemented

        return cls(
            cls._generate_class_name(type_args),
            cls._base_classes,
            {
                "c": classproperty(lambda c: c.name(type_args)),
                "headers": tuple(cls.headers),
                "origin": cls,
                "args": type_args,
            },
        )


class GenericNotImplemented(metaclass=GenericType):
    """
    Placeholder class for when a generic is not concrete/cannot be implemented in C++.
    """

    @classmethod
    def __bool__(cls) -> bool:
        """
        Returns ``False`` as this generic is not concrete.
        """
        return False

    @classmethod
    def __str__(cls) -> str:
        return "GenericNotImplemented"
