from typing import override, Self

from .generics import GenericType, GenericArg, GenericNotImplemented
from .object import CObject


class CTypeVar(CObject):
    """
    Type variables are parameters to generic types in Python.
    They are currently not implemented for C++.
    """

    var_name: str
    "The name of the type variable in Python."

    @classmethod
    def __bool__(cls) -> bool:
        """
        This class is not concrete.

        :returns: ``False``
        """
        return False

    @classmethod
    def named(cls, var_name: str) -> type[Self]:
        """
        Create a type variable with the given name.

        :param var_name: The name of the type variable.
        :returns: A type variable instance with the given name.
        """

        if not var_name.isidentifier():
            raise ValueError(f"'{var_name}' is not a valid identifier")

        return type(cls)(f"{cls.__name__}_{var_name}", (cls,), {"var_name": var_name})


class CGenericTypeAlias(GenericType):
    """
    Generic type alias (i.e. with type params) to a Python type.
    """

    type_params: list[str]
    "List of parameters to this type alias, e.g. ['T1', 'T2']."

    generic_args: list[type[CObject]]
    "The arguments to the generic this type alias represents, e.g. [CInt, T1, CFloat]."

    origin: type[GenericType]
    "The origin of the generic this type alias represents, e.g. :py:class:`CList`."

    def __new__(
        cls, type_params: list[str], origin: type[GenericType], type_args: list[type[CObject]]
    ) -> type["CGenericTypeAlias"]:
        """
        Create a new generic type alias with parameters, from a generic type and arguments.

        :param type_params: The parameters to this type alias, e.g. ['T1', 'T2'].
        :param origin: The origin of the generic this type alias represents, e.g. :py:class:`CList`.
        :param type_args: The arguments to the generic this type alias represents, e.g. [CInt, T1, CFloat].

        :returns: A new generic type alias instance.
        """

        return type(cls)(
            f"{cls.__name__}_{'_'.join(type_params)}",
            (cls,),
            {"origin": origin, "type_params": type_params, "generic_args": type_args},
        )

    @override
    def __class_getitem__(cls, *args: GenericArg) -> GenericType:
        """
        Generate a concrete generic instance from this type alias from the given type arguments.

        :param args: The type arguments.
        :returns: A concrete generic instance.
        """

        # Turn args into a tuple
        type_args: tuple[GenericArg, ...] = args[0] if isinstance(args[0], tuple) else args

        # If the number of args provided != the number of parameters
        if len(type_args) != len(cls.type_params):
            return GenericNotImplemented

        # Generate the generic args from the provided type args and the alias' stored generic args
        generic_args: list[type[CObject]] = [
            type_args[cls.type_params.index(arg.var_name)] if issubclass(arg, CTypeVar) else arg
            for arg in cls.generic_args
        ]

        return cls.origin[*generic_args]
