from typing import Any, Optional, Union, List, Dict, TypeVar, Generic, Sequence, Callable, Tuple
from typing_extensions import Protocol
from .elements import ClauseElement as ClauseElement, ColumnElement
from .base import Executable as Executable, SchemaVisitor as SchemaVisitor
from .schema import Table, MetaData, SchemaItem, ForeignKeyConstraint, ForeignKey
from .compiler import IdentifierPreparer
from .type_api import TypeEngine
from .. import engine

_T = TypeVar('_T')
_TE = TypeVar('_TE', bound=TypeEngine[Any])

class _DDLCompiles(ClauseElement): ...

class _DDLCallable(Protocol):
    def __call__(self, ddl: DDLElement, target: Optional[Union[Table, MetaData]], bind: engine.Connection,
                 tables: Optional[List[Any]] = ..., state: Optional[Any] = ...,
                 checkfirst: bool = ...) -> bool: ...

_DDLE = TypeVar('_DDLE', bound=DDLElement)

class DDLElement(Executable, _DDLCompiles):
    target: Optional[SchemaItem] = ...
    on: Optional[Union[str, Tuple[str, ...], _DDLOnCallback]] = ...
    dialect: Optional[engine.Dialect] = ...
    callable_: Optional[_DDLCallable] = ...
    bind: Optional[engine.Connection] = ...
    def execute(self, bind: Optional[engine.Connectable] = ...,  # type: ignore
                target: Optional[SchemaItem] = ...) -> Optional[engine.ResultProxy]: ...
    def execute_at(self, event_name: str, target: SchemaItem) -> None: ...
    def against(self: _DDLE, target: SchemaItem) -> _DDLE: ...
    state: Any = ...
    def execute_if(self: _DDLE, dialect: Optional[engine.Dialect] = ..., callable_: Optional[_DDLCallable] = ...,
                   state: Optional[Any] = ...) -> _DDLE: ...
    def __call__(self, target, bind, **kw): ...

class _DDLOnCallback(Protocol):
    def __call__(self, ddl: DDLElement, event: Optional[str], target: Optional[Union[Table, MetaData]],
                 connection: engine.Connection, tables: Optional[List[Any]] = ...) -> bool: ...

class DDL(DDLElement):
    __visit_name__: str = ...
    statement: str = ...
    context: Dict[Any, Any] = ...
    on: Optional[Union[str, Tuple[str, ...], _DDLOnCallback]] = ...
    def __init__(self, statement: str, on: Optional[Union[str, Tuple[str, ...], _DDLOnCallback]] = ...,
                 context: Optional[Dict[Any, Any]] = ..., bind: Optional[engine.Connectable] = ...) -> None: ...

class _CreateDropBase(DDLElement, Generic[_T]):
    element: _T = ...
    bind: Optional[engine.Connection] = ...
    def __init__(self, element: _T, on: Optional[Union[str, Tuple[str, ...], _DDLOnCallback]] = ...,
                 bind: Optional[engine.Connection] = ...) -> None: ...

class CreateSchema(_CreateDropBase[str]):
    __visit_name__: str = ...
    quote: Any = ...
    def __init__(self, name: str, quote: Optional[Any] = ..., **kw) -> None: ...

class DropSchema(_CreateDropBase[str]):
    __visit_name__: str = ...
    quote: Any = ...
    cascade: bool = ...
    def __init__(self, name: str, quote: Optional[Any] = ..., cascade: bool = ..., **kw) -> None: ...

class CreateTable(_CreateDropBase[Table]):
    __visit_name__: str = ...
    columns: List[CreateColumn[Any]] = ...
    include_foreign_key_constraints: Optional[Sequence[ForeignKeyConstraint]] = ...
    def __init__(self, element: Table, on: Optional[Union[str, Tuple[str, ...], _DDLOnCallback]] = ...,
                 bind: Optional[engine.Connectable] = ...,
                 include_foreign_key_constraints: Optional[Sequence[ForeignKeyConstraint]] = ...) -> None: ...

class _DropView(_CreateDropBase[str]):
    __visit_name__: str = ...

class CreateColumn(_DDLCompiles, Generic[_TE]):
    __visit_name__: str = ...
    element: ColumnElement[_TE] = ...
    def __init__(self, element: ColumnElement[_TE]) -> None: ...

class DropTable(_CreateDropBase[str]):
    __visit_name__: str = ...

class CreateSequence(_CreateDropBase[str]):
    __visit_name__: str = ...

class DropSequence(_CreateDropBase[str]):
    __visit_name__: str = ...

class CreateIndex(_CreateDropBase[str]):
    __visit_name__: str = ...

class DropIndex(_CreateDropBase[str]):
    __visit_name__: str = ...

class AddConstraint(_CreateDropBase[str]):
    __visit_name__: str = ...
    def __init__(self, element: str, *args: Any, **kw: Any) -> None: ...

class DropConstraint(_CreateDropBase[str]):
    __visit_name__: str = ...
    cascade: bool = ...
    def __init__(self, element: str, cascade: bool = ..., **kw) -> None: ...

class DDLBase(SchemaVisitor):
    connection: engine.Connection = ...
    def __init__(self, connection: engine.Connection) -> None: ...

class SchemaGenerator(DDLBase):
    checkfirst: bool = ...
    tables: Optional[List[Table]] = ...
    preparer: IdentifierPreparer = ...
    dialect: engine.Dialect = ...
    memo: Dict[Any, Any] = ...
    def __init__(self, dialect: engine.Dialect, connection: engine.Connection, checkfirst: bool = ...,
                 tables: Optional[List[Table]] = ..., **kwargs: Any) -> None: ...
    def visit_metadata(self, metadata: MetaData) -> None: ...
    def visit_table(self, table: Table, create_ok: bool = ...,
                    include_foreign_key_constraints: Optional[Sequence[ForeignKeyConstraint]] = ...,
                    _is_metadata_operation: bool = ...) -> None: ...
    def visit_foreign_key_constraint(self, constraint: ForeignKeyConstraint) -> None: ...
    def visit_sequence(self, sequence: str, create_ok: bool = ...): ...
    def visit_index(self, index: str) -> None: ...

class SchemaDropper(DDLBase):
    checkfirst: bool = ...
    tables: Optional[List[Table]] = ...
    preparer: IdentifierPreparer = ...
    dialect: engine.Dialect = ...
    memo: Dict[Any, Any] = ...
    def __init__(self, dialect: engine.Dialect, connection: engine.Connection, checkfirst: bool = ...,
                 tables: Optional[List[Table]] = ..., **kwargs: Any) -> None: ...
    def visit_metadata(self, metadata: MetaData) -> None: ...
    def visit_index(self, index: str) -> None: ...
    def visit_table(self, table: Table, drop_ok: bool = ..., _is_metadata_operation: bool = ...) -> None: ...
    def visit_foreign_key_constraint(self, constraint: ForeignKeyConstraint) -> None: ...
    def visit_sequence(self, sequence: str, drop_ok: bool = ...) -> None: ...

def sort_tables(tables: Sequence[Table], skip_fn: Optional[Callable[[ForeignKey], bool]] = ...,
                extra_dependencies: Optional[Sequence[Tuple[Table, Table]]] = ...): ...
def sort_tables_and_constraints(tables: Sequence[Table],
                                filter_fn: Optional[Callable[[ForeignKeyConstraint], Optional[bool]]] = ...,
                                extra_dependencies: Optional[Sequence[Tuple[Table, Table]]] = ...): ...
