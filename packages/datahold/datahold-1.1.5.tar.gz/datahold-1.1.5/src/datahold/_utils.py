import functools
from typing import *

__all__ = [
    "getHoldFunc",
    "getHoldType",
]


def getHoldFunc(cls, name):
    old = getattr(cls, name)

    def new(self, *args: Any, **kwargs: Any) -> Any:
        data = self.data
        ans = old(data, *args, **kwargs)
        self.data = data
        return ans

    functools.wraps(old)(new)
    return new


def getHoldType(
    *funcnames,
    name,
    bases,
    datacls,
):
    funcs = dict()
    for n in funcnames:
        funcs[n] = getHoldFunc(datacls, n)
    ans = type(name, bases, funcs)
    ans.__annotations__ = dict(data=datacls)
    return ans
