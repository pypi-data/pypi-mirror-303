__all__ = ["subclass"]


def subclass(cls):
    return type(cls.__name__, (), {})
