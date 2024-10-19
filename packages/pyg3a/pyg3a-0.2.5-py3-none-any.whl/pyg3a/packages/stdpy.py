#!/usr/bin/env python3


def len(s: str) -> int:
    import string

    return f"strlen({s}.c_str())"


def str__init__(object: int) -> str:
    import fxcg.misc

    @c_func
    def _str(i: int) -> "str":
        return """
        unsigned char buffer[12];
        itoa(i, buffer);
        return String((char *) buffer);
        """

    return f"_str({object})"


def range(stop: int) -> tuple[int, ...]:
    return f"{{{', '.join([str(i) for i in range(int(stop))])}}}"


def range(start: int, stop: int, step: int = 1) -> tuple[int, ...]:
    return f"{{{', '.join([str(i) for i in range(int(start), int(stop), int(step))])}}}"


def range__iter__(var_name: str, stop: int) -> int:
    return f"int {var_name} = 0; {var_name} < {stop}; {var_name}++"


def range__iter__(var_name: str, start: int, stop: int, step: int = 1) -> int:
    return f"int {var_name} = {start}; {var_name} < {stop}; {var_name} += {step}"


def int__init__(number: float) -> int:
    return f"(int) ({number})"


def round(number: float) -> int:
    @c_func
    def _round(val: float) -> int:
        return """
        if (val < 0.0)
            return (int) (val - 0.5);
        return (int) (val + 0.5);
        """

    return f"_round({number})"


def max(a: int, b: int) -> int:
    @c_func
    def _max(a: int, b: int) -> int:
        return """
        if (a > b)
            return a;
        return b;
        """

    return f"_max({a}, {b})"


def min(a: int, b: int) -> int:
    @c_func
    def _min(a: int, b: int) -> int:
        return """
        if (a < b)
            return a;
        return b;
        """

    return f"_min({a}, {b})"


def __pyg3a_sprintf() -> None:
    import stdarg
    import stdio

    @c_func
    def _sprintf(fmt: str, *args: Any) -> str:
        return """
        char buffer[256];
        sprintf(buffer, fmt.c_str(), args...);
        return String(buffer);
        """

    return "/* placeholder */"
