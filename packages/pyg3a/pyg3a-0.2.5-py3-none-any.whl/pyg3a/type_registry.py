#!/usr/bin/env python3

import copy
from enum import Enum
from typing import Optional


class TypeCategory(Enum):
    """
    Enum describing type categories used by :py:class:`TypeRegistry`.
    All types specified in Python scripts must be registered to both a C type equivalent in :py:class:`TypeRegistry` and one of these categories.
    """

    NONE = 0
    "Default category: None/void."

    PY = 1
    "Types that exist in Python: int, str, etc."

    INTEGERS = 2
    r"All integers: int, char, short, long, unsigned, int \*, etc."

    FLOATS = 3
    "All floats: float, double, etc."

    NUMBERS = 4
    "Broad category encompassing both floating-point and integer values."

    C_STRINGS = 5
    r"Types that represent 'C-style' strings: char \*, unsigned char \*, const char \*, char[], etc."


class TypeRegistry:
    """
    Registry storing conversions for Python type names -> C type names.
    Each type is associated with one or more :py:class:`TypeCategory` category, and each category can have 'sub-categories' which automatically register all their types to the 'super-category'.
    """

    registry: dict[TypeCategory, dict[str, str]]
    "Main registry, mapping a :py:class:`TypeCategory` to a dictionary of Python -> C type names."

    all_cats: dict[str, str]
    "Collapsed version of :py:attr:`registry` containing all Python -> C type name mappings."

    auto_registry: dict[TypeCategory, list[TypeCategory]] = {}
    "Map supertypes to subtypes, e.g. :py:attr:`TypeCategory.NUMBERS`: [ :py:attr:`TypeCategory.INTEGERS`, :py:attr:`TypeCategory.FLOATS` ]."

    def __init__(
        self,
        registry: Optional[dict[TypeCategory, dict[str, str]]] = None,
        all_cats: Optional[dict[str, str]] = None,
    ):
        """
        Create a type registry. Inital ``registry`` and ``all_cats`` dictionaries can optionally be passed.

        :param registry: Optional initial registry dictionary. See :py:attr:`registry`.
        :param all_cats: Optional initial all-category dictionary. See :py:attr:`all_cats`.
        """

        self.registry = copy.deepcopy(registry) if registry else {}
        self.all_cats = all_cats.copy() if all_cats else {}

    def register(self, py_type: str, c_type: str, cat: TypeCategory) -> None:
        """
        Register a ``py_type`` -> ``c_type`` conversion within a specific :py:class:`TypeCategory` category.

        :param py_type: Python name of the type.
        :param c_type: C equivalent type string.
        :param cat: Type category. See :py:class:`TypeCategory` for options.
        """

        if cat in self.registry:
            self.registry[cat][py_type] = c_type
        else:
            self.registry[cat] = {py_type: c_type}

        self._update()

    def auto_register(self, subset: TypeCategory, superset: TypeCategory) -> None:
        """
        Set up auto-registration such that types in the ``subset`` category also appear as a ``superset`` type.
        For example, ``auto_register(TypeCategory.INTEGERS, TypeCategory.NUMBERS)`` makes all types added as an integer also come under the numbers category.

        :param subset: The more-specific subset category.
        :param superset: The less-specific superset category - ``subset`` types will be added to this category.
        """

        if superset in self.auto_registry:
            self.auto_registry[superset].append(subset)
        else:
            self.auto_registry[superset] = [subset]

    def copy(self) -> "TypeRegistry":
        """
        Make a deep copy of this TypeRegistry with the current registry information but without its auto-registries.

        :returns: The new :py:class:`TypeRegistry`.
        """
        return TypeRegistry(self.registry, self.all_cats)

    def _update(self) -> None:
        """
        Update the :py:attr:`all_cats` info from the registered types in all categories.
        """

        self.all_cats = {key: val for cat in self.registry.values() for key, val in cat.items()}

    def __getitem__(self, py_type: object) -> str:
        """
        Get the C-equivalent type for a specified ``py_type``.

        :returns: The C equivalent type string from any category.
        """
        if type(py_type) is not str:
            raise TypeError
        if py_type not in self.all_cats:
            raise KeyError
        return self.all_cats[py_type]

    def __getattr__(self, cat: str) -> dict[str, str]:
        """
        Get a dictionary of Python -> C types for a specific category ``cat``.

        :param cat: The name of the category to get the type dictionary for. See :py:class:`TypeCategory` for a list of category names.
        :returns: A dictionary mapping Python types to C type strings for the specified category.
        """

        if cat not in TypeCategory.__members__:
            raise AttributeError(f"Registry Type '{cat}' not found")

        if TypeCategory[cat] not in self.registry:
            self.registry[TypeCategory[cat]] = {}

        if TypeCategory[cat] in self.auto_registry:
            return {
                key: val
                for subcat in self.auto_registry[TypeCategory[cat]]
                for key, val in self.registry[subcat].items()
            } | self.registry[TypeCategory[cat]]

        return self.registry[TypeCategory[cat]]

    def __contains__(self, py_type: str) -> bool:
        """
        Determines if a specified Python type has been registered in this ``TypeRegistry``.

        :param py_type: The Python type to check.
        :returns: ``True`` if the type has been registered and ``False`` if it hasn't.
        """

        return py_type in self.all_cats

    def __str__(self):
        return str(self.registry)