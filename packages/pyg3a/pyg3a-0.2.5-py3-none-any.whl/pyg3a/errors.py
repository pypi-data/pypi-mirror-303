#!/usr/bin/env python3


class AnnotationError(Exception):
    """
    Base class for all errors relating to annotations.
    """

    pass


class NotAnnotatedError(AnnotationError, SyntaxError):
    """
    If a function or variable is missing annotations.
    """

    pass


class CTypeNotConcreteError(NotImplementedError):
    """
    If a variable's type is computed to be used in the C++ output and the type is not concrete or does not exist in C++.
    """

    pass


class FStringTooComplexError(Exception):
    """
    If an f-string is too complex to be converted to C++ without using C++ String concatenation.
    """

    pass
