import functools
from abc import ABC, abstractmethod
from collections import abc
from typing import *

from datarepr import datarepr
from scaevola import Scaevola

from datahold._utils import getHoldType

__all__ = [
    "HoldABC",
    "HoldDict",
    "HoldList",
    "HoldSet",
    "OkayABC",
    "OkayDict",
    "OkayList",
    "OkaySet",
]


class HoldABC(ABC):
    def __hash__(self, /) -> int:
        """raise TypeError"""
        raise TypeError("unhashable type: %r" % type(self).__name__)

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __setattr__(self, name: str, value: Any, /) -> None:
        """Implement setattr(self, name, value)."""
        cls = type(self)
        if name.startswith("_"):
            super().__setattr__(name, value)
            return
        if isinstance(getattr(cls, name, None), property):
            super().__setattr__(name, value)
            return
        e = "%r object has no property %r"
        e %= (cls.__name__, name)
        raise AttributeError(e)

    @classmethod
    def __subclasshook__(cls, other: type, /) -> bool:
        """Overwrite for custom subclass check."""
        return NotImplemented

    @property
    @abstractmethod
    def data(self): ...


HoldDict = getHoldType(
    "__contains__",
    "__delitem__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getitem__",
    "__gt__",
    "__ior__",
    "__iter__",
    "__le__",
    "__len__",
    "__lt__",
    "__or__",
    "__repr__",
    "__reversed__",
    "__ror__",
    "__setitem__",
    "__str__",
    "clear",
    "copy",
    "get",
    "items",
    "keys",
    "pop",
    "popitem",
    "setdefault",
    "update",
    "values",
    name="HoldDict",
    bases=(HoldABC, abc.MutableMapping),
    datacls=dict,
)

HoldList = getHoldType(
    "__add__",
    "__contains__",
    "__delitem__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getitem__",
    "__gt__",
    "__iadd__",
    "__imul__",
    "__iter__",
    "__le__",
    "__len__",
    "__lt__",
    "__mul__",
    "__repr__",
    "__reversed__",
    "__rmul__",
    "__setitem__",
    "__str__",
    "append",
    "clear",
    "copy",
    "count",
    "extend",
    "index",
    "insert",
    "pop",
    "remove",
    "reverse",
    "sort",
    name="HoldList",
    bases=(HoldABC, abc.MutableSequence),
    datacls=list,
)

HoldSet = getHoldType(
    "__and__",
    "__contains__",
    "__eq__",
    "__format__",
    "__ge__",
    "__gt__",
    "__iand__",
    "__ior__",
    "__isub__",
    "__iter__",
    "__ixor__",
    "__le__",
    "__len__",
    "__lt__",
    "__or__",
    "__rand__",
    "__repr__",
    "__ror__",
    "__rsub__",
    "__rxor__",
    "__str__",
    "__sub__",
    "__xor__",
    "add",
    "clear",
    "copy",
    "difference",
    "difference_update",
    "discard",
    "intersection",
    "intersection_update",
    "isdisjoint",
    "issubset",
    "issuperset",
    "pop",
    "remove",
    "symmetric_difference",
    "symmetric_difference_update",
    "union",
    "update",
    name="HoldSet",
    bases=(HoldABC, abc.MutableSet),
    datacls=set,
)


class OkayABC(Scaevola, HoldABC):

    def __bool__(self, /) -> bool:
        """Return bool(self)."""
        return bool(self._data)

    def __contains__(self, value: Any, /) -> bool:
        """Return value in self."""
        return value in self._data

    def __eq__(self, other: Any, /) -> bool:
        """Return self==other."""
        if type(self) is type(other):
            return self._data == other._data
        try:
            other = type(self)(other)
        except:
            return False
        return self._data == other._data

    def __format__(self, format_spec: Any = "", /) -> str:
        """Return format(self, format_spec)."""
        return format(str(self), str(format_spec))

    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
        return self._data[key]

    def __gt__(self, other: Any, /) -> bool:
        """Return self>=other."""
        return not (self == other) and (self >= other)

    def __iter__(self, /) -> Iterator:
        """Return iter(self)."""
        return iter(self._data)

    def __le__(self, other: Any, /) -> bool:
        """Return self<=other."""
        return self._data <= type(self._data)(other)

    def __len__(self, /) -> int:
        """Return len(self)."""
        return len(self._data)

    def __lt__(self, other: Any, /) -> bool:
        """Return self<other."""
        return not (self == other) and (self <= other)

    def __ne__(self, other: Any, /) -> bool:
        """Return self!=other."""
        return not (self == other)

    def __repr__(self, /) -> str:
        """Return repr(self)."""
        return datarepr(type(self).__name__, self._data)

    def __reversed__(self, /) -> Self:
        """Return reversed(self)."""
        return type(self)(reversed(self.data))

    def __sorted__(self, /, **kwargs: Any) -> Self:
        """Return sorted(self, **kwargs)."""
        ans = type(self)(self.data)
        ans.sort(**kwargs)
        return ans

    def __str__(self, /) -> str:
        """Return str(self)."""
        return repr(self)

    def copy(self, /) -> Self:
        """New holder for equivalent data."""
        return type(self)(self.data)


class OkayDict(OkayABC, HoldDict):

    @functools.wraps(dict.__init__)
    def __init__(self, data: Any = {}, /, **kwargs) -> None:
        self.data = dict(data, **kwargs)

    __init__.__doc__ = "Initialize self."

    def __or__(self, other: Any, /) -> Self:
        """Return self|other."""
        return type(self)(self._data | dict(other))

    @property
    def data(self, /) -> dict:
        """self.data"""
        return dict(self._data)

    @data.setter
    def data(self, values: Any, /) -> None:
        self._data = dict(values)

    @data.deleter
    def data(self, /) -> None:
        self._data = dict()

    @classmethod
    def fromkeys(cls, iterable: Iterable, value: Any = None, /) -> Self:
        """Create a new instance with keys from iterable and values set to value."""
        return cls(dict.fromkeys(iterable, value))

    @functools.wraps(dict.get)
    def get(self, /, *args: Any) -> Any:
        return self._data.get(*args)

    @functools.wraps(dict.items)
    def items(self, /) -> abc.ItemsView:
        return self._data.items()

    @functools.wraps(dict.keys)
    def keys(self, /) -> abc.KeysView:
        return self._data.keys()

    @functools.wraps(dict.values)
    def values(self, /) -> abc.ValuesView:
        return self._data.values()


class OkayList(OkayABC, HoldList):

    def __add__(self, other: Any, /) -> Self:
        """Return self+other."""
        return type(self)(self._data + list(other))

    def __init__(self, data: Iterable = []) -> None:
        """Initialize self."""
        self.data = data

    def __mul__(self, value: SupportsIndex, /) -> Self:
        """Return self*other."""
        return type(self)(self.data * value)

    def __rmul__(self, value: SupportsIndex, /) -> Self:
        """Return other*self."""
        return self * value

    @functools.wraps(list.count)
    def count(self, value: Any, /) -> int:
        return self._data.count(value)

    @property
    def data(self, /) -> list:
        """self.data"""
        return list(self._data)

    @data.setter
    def data(self, values: Iterable, /) -> None:
        self._data = list(values)

    @data.deleter
    def data(self, /) -> None:
        self._data = list()

    @functools.wraps(list.index)
    def index(self, /, *args: Any) -> int:
        return self._data.index(*args)


class OkaySet(OkayABC, HoldSet):

    def __and__(self, other: Any, /) -> Self:
        """Return self&other."""
        return type(self)(self._data & set(other))

    def __init__(self, data: Iterable = set()) -> None:
        """Initialize self."""
        self.data = data

    def __or__(self, other: Any, /) -> Self:
        """Return self|other."""
        return type(self)(self._data | set(other))

    def __sub__(self, other: Any, /) -> Self:
        """Return self-other."""
        return type(self)(self._data - set(other))

    def __xor__(self, other: Any, /) -> Self:
        """Return self^other."""
        return type(self)(self._data ^ set(other))

    @property
    def data(self, /) -> set:
        """self.data"""
        return set(self._data)

    @data.setter
    def data(self, values: Iterable) -> None:
        self._data = set(values)

    @data.deleter
    def data(self, /) -> None:
        self._data = set()

    @functools.wraps(set.difference)
    def difference(self, /, *args: Any) -> Self:
        return type(self)(self._data.difference(*args))

    @functools.wraps(set.intersection)
    def intersection(self, /, *args: Any) -> set:
        return type(self)(self._data.intersection(*args))

    @functools.wraps(set.isdisjoint)
    def isdisjoint(self, other: Any, /) -> bool:
        return self._data.isdisjoint(other)

    @functools.wraps(set.issubset)
    def issubset(self, other: Any, /) -> bool:
        return self._data.issubset(other)

    @functools.wraps(set.issuperset)
    def issuperset(self, other: Any, /) -> bool:
        return self._data.issuperset(other)

    @functools.wraps(set.symmetric_difference)
    def symmetric_difference(self, other: Any, /) -> Self:
        return type(self)(self._data.symmetric_difference(other))

    @functools.wraps(set.union)
    def union(self, /, *args: Any) -> Self:
        return type(self)(self._data.union(*args))
