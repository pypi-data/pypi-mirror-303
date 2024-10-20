from typing import *

__all__ = ["datarepr"]


def datarepr(name: Any, /, *args: Any, **kwargs: Any):
    parts = list()
    for a in args:
        parts.append(repr(a))
    for i in kwargs.items():
        parts.append("%s = %r" % i)
    content = ", ".join(parts)
    ans = "%s(%s)" % (name, content)
    return ans
