from typing import (
    Any, Optional, Union, FrozenSet, Generic, Type, TypeVar, Set, Iterator, Iterable, Tuple, List, Callable, Dict, Mapping,
    AbstractSet, overload
)
import sys

_T = TypeVar('_T')
_U = TypeVar('_U')

_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

EMPTY_SET: FrozenSet[Any] = ...

class AbstractKeyedTuple(Tuple[_T, ...], Generic[_T]):
    def keys(self) -> List[str]: ...

class KeyedTuple(AbstractKeyedTuple[_T]):
    def __new__(cls, vals, labels: Optional[Any] = ...): ...
    def __setattr__(self, key, value): ...

class ImmutableContainer(object): ...

class immutabledict(ImmutableContainer, Dict[_KT, _VT]):
    clear: Any = ...
    pop: Any = ...
    popitem: Any = ...
    setdefault: Any = ...
    update: Any = ...
    def __new__(cls, *args): ...
    @overload
    def __init__(self, **kwargs: _VT) -> None: ...
    @overload
    def __init__(self, map: Mapping[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[Tuple[_KT, _VT]], **kwargs: _VT) -> None: ...
    def __reduce__(self) -> Tuple[Type[immutabledict[_KT, _VT]], Tuple[Dict[_KT, _VT]]]: ...
    @overload
    def union(self, d: Mapping[_U, _T]) -> immutabledict[Union[_U, _KT], Union[_VT, _T]]: ...
    @overload
    def union(self, d: Iterable[Tuple[_U, _T]]) -> immutabledict[Union[_U, _KT], Union[_VT, _T]]: ...

class Properties(Generic[_T]):
    def __init__(self, data) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __add__(self, other: Iterable[_U]) -> List[Union[_T, _U]]: ...
    def __setitem__(self, key: str, object: _T) -> None: ...
    def __getitem__(self, key: str) -> _T: ...
    def __delitem__(self, key: str) -> None: ...
    def __setattr__(self, key: str, obj: _T) -> None: ...
    def __getattr__(self, key: str) -> _T: ...
    def __contains__(self, key: str) -> bool: ...
    def as_immutable(self) -> ImmutableProperties[_T]: ...
    @overload
    def update(self, value: Mapping[str, _T]) -> None: ...
    @overload
    def update(self, value: Iterable[Tuple[str, _T]]) -> None: ...
    @overload
    def get(self, k: str) -> Optional[_T]: ...
    @overload
    def get(self, k: str, default: Union[_T, _U]) -> Union[_T, _U]: ...
    def keys(self) -> List[str]: ...
    def values(self) -> List[_T]: ...
    def items(self) -> List[Tuple[str, _T]]: ...
    def has_key(self, key: str) -> bool: ...
    def clear(self) -> None: ...

class OrderedProperties(Properties[_T]):
    def __init__(self) -> None: ...

class ImmutableProperties(ImmutableContainer, Properties[_T]): ...

class OrderedDict(Dict[_KT, _VT]):
    def __reduce__(self): ...
    def __init__(self, ____sequence: Optional[Any] = ..., **kwargs) -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> OrderedDict[_KT, _VT]: ...
    def __copy__(self) -> OrderedDict[_KT, _VT]: ...
    if sys.version_info < (3, 0):
        def sort(self, cmp: Callable[[_VT, _VT], Any] = ..., key: Callable[[_VT], Any] = ..., reverse: bool = ...) -> None: ...
    else:
        def sort(self, *, key: Optional[Callable[[_VT], Any]] = ..., reverse: bool = ...) -> None: ...
    @overload
    def update(self, ____sequence: Mapping[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def update(self, ____sequence: Iterable[Tuple[_KT, _VT]], **kwargs: _VT) -> None: ...
    @overload
    def update(self, **kwargs: _VT) -> None: ...
    # Signature of "setdefault" incompatible with supertype "dict" and "MutableMapping"
    def setdefault(self, key: _KT, value: _VT) -> _VT: ...  # type: ignore
    def __iter__(self) -> Iterator[_KT]: ...
    # Return type of "keys" incompatible with supertype "dict" and "Mapping"
    def keys(self) -> List[_KT]: ...  # type: ignore
    # Return type of "values" incompatible with supertype "dict" and "Mapping"
    def values(self) -> List[_VT]: ...  # type: ignore
    # Return type of "items" incompatible with supertype "dict" and "Mapping"
    def items(self) -> List[Tuple[_KT, _VT]]: ...  # type: ignore
    if sys.version_info < (3, 0):
        def itervalues(self) -> Iterator[_VT]: ...
        def iterkeys(self) -> Iterator[_KT]: ...
        def iteritems(self) -> Iterator[Tuple[_KT, _VT]]: ...
    def __setitem__(self, key: _KT, object: _VT) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
    @overload
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, *default: Union[_VT, _T]) -> Union[_VT, _T]: ...
    def popitem(self) -> Tuple[_KT, _VT]: ...

_OS = TypeVar('_OS', bound=OrderedSet)

class OrderedSet(Set[_T]):
    def __init__(self, d: Optional[Iterable[_T]] = ...) -> None: ...
    def add(self, element: _T) -> None: ...
    def remove(self, element: _T) -> None: ...
    def insert(self, pos: int, element: _T) -> None: ...
    def discard(self, element: _T) -> None: ...
    def clear(self) -> None: ...
    def __getitem__(self, key: int) -> _T: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __add__(self: _OS, other: Iterable[_T]) -> _OS: ...
    def update(self: _OS, iterable: Iterable[_T]) -> _OS: ...  # type: ignore  # signature incompatible with supertype
    def __ior__(self: _OS, iterable: Iterable[_U]) -> OrderedSet[Union[_T, _U]]: ...
    def union(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore  # signature incompatible with supertype
    def __or__(self: _OS, other: Iterable[_U]) -> OrderedSet[Union[_T, _U]]: ...
    def intersection(self: _OS, other: Iterable[object]) -> _OS: ...  # type: ignore  # signature incompatible with supertype
    def __and__(self: _OS, other: Iterable[object]) -> _OS: ...
    def symmetric_difference(self: _OS, other: Iterable[_T]) -> _OS: ...
    def __xor__(self: _OS, other: Iterable[_U]) -> OrderedSet[Union[_T, _U]]: ...
    def difference(self: _OS, other: Iterable[object]) -> _OS: ...  # type: ignore  # signature incompatible with supertype
    def __sub__(self: _OS, other: Iterable[object]) -> _OS: ...
    def intersection_update(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore  # signature incompatible with supertype
    def __iand__(self: _OS, other: Iterable[object]) -> _OS: ...
    # Return type incompatible with supertype
    def symmetric_difference_update(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore
    def __ixor__(self: _OS, other: Iterable[_U]) -> OrderedSet[Union[_T, _U]]: ...
    def difference_update(self: _OS, other: Iterable[object]) -> _OS: ...  # type: ignore  # signature incompatible with supertype
    def __isub__(self: _OS, other: Iterable[object]) -> _OS: ...

class IdentitySet(object):
    def __init__(self, iterable: Optional[Any] = ...) -> None: ...
    def add(self, value): ...
    def __contains__(self, value): ...
    def remove(self, value): ...
    def discard(self, value): ...
    def pop(self): ...
    def clear(self): ...
    def __cmp__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def issubset(self, iterable): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def issuperset(self, iterable): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def union(self, iterable): ...
    def __or__(self, other): ...
    def update(self, iterable): ...
    def __ior__(self, other): ...
    def difference(self, iterable): ...
    def __sub__(self, other): ...
    def difference_update(self, iterable): ...
    def __isub__(self, other): ...
    def intersection(self, iterable): ...
    def __and__(self, other): ...
    def intersection_update(self, iterable): ...
    def __iand__(self, other): ...
    def symmetric_difference(self, iterable): ...
    def __xor__(self, other): ...
    def symmetric_difference_update(self, iterable): ...
    def __ixor__(self, other): ...
    def copy(self): ...
    __copy__: Any = ...
    def __len__(self): ...
    def __iter__(self): ...
    def __hash__(self): ...

class WeakSequence(object):
    def __init__(self, __elements: Any = ...) -> None: ...
    def append(self, item): ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, index): ...

class OrderedIdentitySet(IdentitySet):
    def __init__(self, iterable: Optional[Any] = ...) -> None: ...

class PopulateDict(dict):
    creator: Any = ...
    def __init__(self, creator) -> None: ...
    def __missing__(self, key): ...

column_set = set
column_dict = dict
ordered_column_set = OrderedSet
populate_column_dict = PopulateDict

def unique_list(seq: Iterable[_T], hashfunc: Optional[Callable[[_T], Any]] = ...) -> List[_T]: ...

class UniqueAppender(object):
    data: Any = ...
    def __init__(self, data, via: Optional[Any] = ...) -> None: ...
    def append(self, item): ...
    def __iter__(self): ...

def coerce_generator_arg(arg): ...
def to_list(x, default: Optional[Any] = ...): ...
def has_intersection(set_, iterable): ...
def to_set(x): ...
def to_column_set(x): ...
def update_copy(d, _new: Optional[Any] = ..., **kw): ...
def flatten_iterator(x): ...

class LRUCache(dict):
    capacity: Any = ...
    threshold: Any = ...
    def __init__(self, capacity: int = ..., threshold: float = ...) -> None: ...
    def get(self, key, default: Optional[Any] = ...): ...
    def __getitem__(self, key): ...
    def values(self): ...
    def setdefault(self, key, value): ...
    def __setitem__(self, key, value): ...

def lightweight_named_tuple(name, fields): ...

class ScopedRegistry(object):
    createfunc: Any = ...
    scopefunc: Any = ...
    registry: Any = ...
    def __init__(self, createfunc, scopefunc) -> None: ...
    def __call__(self): ...
    def has(self): ...
    def set(self, obj): ...
    def clear(self): ...

class ThreadLocalRegistry(ScopedRegistry):
    createfunc: Any = ...
    registry: Any = ...
    def __init__(self, createfunc) -> None: ...
    def __call__(self): ...
    def has(self): ...
    def set(self, obj): ...
    def clear(self): ...
