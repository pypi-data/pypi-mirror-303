# TO BE IMPLEMENTED: @cst_types


class unslong(Types.int):
    c = "unsigned long"


class unsint(unslong):
    c = "unsigned int"


class unsshort(unsint):
    c = "unsigned short"


@cst_types
def ref(var: cst.Name) -> any:
    return f"&{var}"


@cst_types
def ref(var: cst.Attribute) -> any:
    return f"&{var}"


def deref(reference: any) -> any:
    return f"*({reference})"
