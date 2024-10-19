from typing import Iterable, Mapping, Any

from .object import CObjectMeta, CObject


class CEnumType(CObjectMeta):
    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]) -> "CEnumType":
        members: dict[str, str] = {member: c_str for member, c_str in namespace.items() if member[0] != "_"}

        def getattr_impl(_cls, attr: str) -> str:
            if attr in members:
                return members[attr]
            raise AttributeError

        return super().__new__(
            mcls,
            name,
            (CObject,),
            {
                "c": name,
                "__bool__": classmethod(lambda cls: True),
                "__getattr__": classmethod(getattr_impl),
            },
        )


class CEnum(metaclass=CEnumType):
    def __new__(cls, name: str, members: str | Iterable[str] | Iterable[tuple[str, Any]] | Mapping[str, Any]) -> type:
        member_names: Iterable[str] = (
            members.split(" ")
            if isinstance(members, str)
            else (
                members.keys()
                if isinstance(members, Mapping)
                else ([k for k, v in members] if isinstance(next(iter(members)), tuple) else members)
            )
        )

        return CEnumType(name, (cls,), {k: 0 for k in member_names})
