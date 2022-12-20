import re


def camelcase(name: str) -> str:
    """Converts a snakecase string to camelcase"""
    return name.sub(r"(_|-)+", " ").title().replace("_", "")


def snakecase(name: str) -> str:
    """Converts a camelcase string to snakecase"""
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("__([A-Z])", r"_\1", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


def singular(name: str) -> str:
    """Returns singular version of plural word"""
    if name.endswith("ies"):
        return name[0:-3] + "y"
    elif name.endswith("s"):
        return name[0:-1]
    else:
        return name
