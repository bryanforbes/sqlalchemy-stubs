from typing import Any, Optional, Union, TypeVar, NoReturn, Iterable, List, Dict, Iterator
from sqlalchemy import util
from .visitors import ClauseVisitor as ClauseVisitor
import collections
from .schema import Column
from ..util import PopulateDict
from ..engine.base import Engine, Connection
from ..engine.result import ResultProxy

PARSE_AUTOCOMMIT: Any = ...
NO_ARG: Any = ...

_I = TypeVar('_I', bound=Immutable)

class Immutable(object):
    def unique_params(self, *optionaldict: Any, **kwargs: Any): ...
    def params(self, *optionaldict: Any, **kwargs: Any): ...
    def _clone(self: _I) -> _I: ...

class _DialectArgView(collections.MutableMapping[str, Any]):
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Any]: ...

class DialectKWArgs(object):
    @classmethod
    def argument_for(cls, dialect_name: str, argument_name: str, default: Any) -> None: ...
    @property
    def dialect_kwargs(self) -> _DialectArgView: ...
    @property
    def kwargs(self) -> _DialectArgView: ...
    @property
    def dialect_options(self) -> PopulateDict: ...

class Generative(object): ...

_E = TypeVar('_E', bound=Executable)

class Executable(Generative):
    supports_execution: bool = ...
    def execution_options(self: _E, **kw: Any) -> _E: ...
    def execute(self, *multiparams: Any, **params: Any) -> Optional[ResultProxy]: ...
    def scalar(self, *multiparams: Any, **params: Any) -> Any: ...
    @property
    def bind(self) -> Optional[Union[Engine, Connection]]: ...

class SchemaEventTarget(object): ...

class SchemaVisitor(ClauseVisitor):
    __traverse_options__: Any = ...

class ColumnCollection(util.OrderedProperties[Column]):
    def __init__(self, *columns: Column) -> None: ...
    def __str__(self) -> str: ...
    def replace(self, column: Column) -> None: ...
    def add(self, column: Column) -> None: ...
    def __delitem__(self, key: str) -> NoReturn: ...
    def __setattr__(self, key: str, object: Column) -> NoReturn: ...
    def __setitem__(self, key: str, value: Column) -> None: ...
    def clear(self) -> NoReturn: ...
    def remove(self, column: Column) -> None: ...
    def update(self, iter: Iterable[Column]) -> None: ...
    def extend(self, iter: Iterable[Column]) -> None: ...
    __hash__: None = ...  # type: ignore
    def __eq__(self, other: Any) -> bool: ...
    def __contains__(self, other: Any) -> bool: ...
    def contains_column(self, col: Column) -> bool: ...
    def as_immutable(self) -> ImmutableColumnCollection: ...

class ImmutableColumnCollection(util.ImmutableProperties[Column], ColumnCollection):
    def __init__(self, data: Dict[str, Any], all_columns: List[Column]) -> None: ...
    def extend(self, iter: Iterable[Column]) -> NoReturn: ...
    def remove(self, column: Column) -> NoReturn: ...

class ColumnSet(util.ordered_column_set):
    def contains_column(self, col: Column) -> bool: ...
    def extend(self, cols: Iterable[Column]) -> None: ...
    def __add__(self, other: Iterable[Column]) -> List[Column]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
