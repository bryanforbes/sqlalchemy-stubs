from typing import Any, Optional, Union, Type, TypeVar, Generic, Callable, List, Dict, Set, Iterator, Tuple as _TupleType, overload
from . import operators
from sqlalchemy import util
from .visitors import Visitable as Visitable
from .annotation import Annotated as Annotated
from .base import Executable as Executable, Immutable as Immutable
from ..engine.base import Engine, Connection
from .type_api import TypeEngine
from .sqltypes import NullType, Boolean, Integer
from .selectable import TextAsFrom, TableClause
from .functions import FunctionElement

_T = TypeVar('_T')
_V = TypeVar('_V')
_U = TypeVar('_U')

def collate(expression, collation): ...
def between(expr, lower_bound, upper_bound, symmetric: bool = ...): ...
def literal(value, type_: Optional[Any] = ...): ...
def outparam(key, type_: Optional[Any] = ...): ...
def not_(clause): ...

class ClauseElement(Visitable):
    __visit_name__: str = ...
    supports_execution: bool = ...
    bind: Any = ...
    is_selectable: bool = ...
    is_clause_element: bool = ...
    description: Any = ...
    def unique_params(self, *optionaldict, **kwargs): ...
    def params(self, *optionaldict, **kwargs): ...
    def compare(self, other: Any, **kw: Any) -> bool: ...
    def get_children(self, **kwargs: Any) -> Any: ...
    def self_group(self, against: Optional[Any] = ...) -> Any: ...
    def compile(self, bind: Optional[Any] = ..., dialect: Optional[Any] = ..., **kw) -> Any: ...
    def __and__(self, other): ...
    def __or__(self, other): ...
    def __invert__(self): ...
    def __bool__(self): ...
    __nonzero__: Any = ...

class ColumnElement(operators.ColumnOperators, ClauseElement, Generic[_T]):
    __visit_name__: str = ...
    primary_key: Any = ...
    foreign_keys: List[Any] = ...
    key: Any = ...
    def self_group(self, against: Optional[Any] = ...): ...
    @property
    def type(self) -> _T: ...
    def comparator(self): ...
    def __getattr__(self, key): ...
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs): ...
    @property
    def expression(self): ...
    def base_columns(self): ...
    def proxy_set(self): ...
    def shares_lineage(self, othercolumn): ...
    def compare(self, other: Any, **kw: Any) -> bool: ...
    def cast(self, type_): ...
    def label(self, name): ...
    def anon_label(self): ...

class BindParameter(ColumnElement[_T], Generic[_T, _V]):
    __visit_name__: str = ...
    key: str = ...
    unique: bool = ...
    value: Union[_V, Any] = ...
    callable: Any = ...
    isoutparam: Any = ...
    required: Union[bool, Any] = ...
    type: _T = ...
    def __init__(self, key: str, value: _V = ..., type_: Optional[Any] = ..., unique: bool = ...,
                 required: bool = ..., quote: Optional[Any] = ..., callable_: Optional[Callable[[], _V]] = ...,
                 isoutparam: bool = ..., _compared_to_operator: Optional[Any] = ...,
                 _compared_to_type: Optional[Any] = ...) -> None: ...
    @property
    def effective_value(self) -> _V: ...
    def compare(self, other: Any, **kw: Any) -> bool: ...

class TypeClause(ClauseElement, Generic[_T]):
    __visit_name__: str = ...
    type: _T = ...
    def __init__(self, type: _T) -> None: ...

_TC = TypeVar('_TC', bound=TextClause)

class TextClause(Executable, ClauseElement):
    __visit_name__: str = ...
    @property
    def selectable(self: _TC) -> _TC: ...
    key: Any = ...
    text: str = ...
    def __init__(self, text: str, bind: Optional[Union[Engine, Connection]] = ...) -> None: ...
    def bindparams(self: _TC, *binds: BindParameter, **names_to_values: Any) -> _TC: ...
    def columns(self, *cols: ColumnClause, **types: Union[TypeEngine[Any], Type[TypeEngine[Any]]]) -> TextAsFrom: ...
    @property
    def type(self) -> NullType: ...
    @property
    def comparator(self) -> Any: ...
    def self_group(self: _TC, against: Optional[Any] = ...) -> Union[_TC, Grouping[_T]]: ...
    def get_children(self, **kwargs: Any) -> List[BindParameter]: ...
    def compare(self, other: Any) -> bool: ...  # type: ignore
    @classmethod
    def _create_text(cls: Type[_TC], text: str, bind: Optional[Union[Engine, Connection]] = ...,
                     bindparams: Optional[List[BindParameter]] = ...,
                     typemap: Optional[Dict[str, Union[TypeEngine[Any], Type[TypeEngine[Any]]]]] = ...,
                     autocommit: Optional[bool] = ...) -> _TC: ...

class Null(ColumnElement[NullType]):
    __visit_name__: str = ...
    @property
    def type(self) -> NullType: ...
    def compare(self, other: Any) -> bool: ...  # type: ignore
    @classmethod
    def _instance(cls) -> Null: ...

class False_(ColumnElement[Boolean]):
    __visit_name__: str = ...
    @property
    def type(self) -> Boolean: ...
    def compare(self, other: Any) -> bool: ...  # type: ignore
    @classmethod
    def _instance(cls) -> False_: ...

class True_(ColumnElement[Boolean]):
    __visit_name__: str = ...
    @property
    def type(self) -> Boolean: ...
    def compare(self, other: Any) -> bool: ...  # type: ignore
    @classmethod
    def _instance(cls) -> True_: ...

_CL = TypeVar('_CL', bound=ClauseList)

class ClauseList(ClauseElement):
    __visit_name__: str = ...
    operator: Any = ...
    group: bool = ...
    group_contents: bool = ...
    clauses: List[ClauseElement] = ...
    def __init__(self, *clauses: ClauseElement, operator: Callable[..., Any] = ..., group: bool = ...,
                 group_contents: bool = ..., **kwargs: Any) -> None: ...
    def __iter__(self) -> Iterator[ClauseElement]: ...
    def __len__(self) -> int: ...
    def append(self, clause: ClauseElement): ...
    def get_children(self, **kwargs) -> List[ClauseElement]: ...
    def self_group(self: _CL, against: Optional[Any] = ...) -> Union[_CL, Grouping[_T]]: ...
    def compare(self, other: Any, **kw: Any) -> bool: ...

_BCL = TypeVar('_BCL', bound=BooleanClauseList)

class BooleanClauseList(ClauseList, ColumnElement[Boolean]):
    __visit_name__: str = ...
    @classmethod
    def and_(cls, *clauses: ClauseElement) -> BooleanClauseList: ...
    @classmethod
    def or_(cls, *clauses: ClauseElement) -> BooleanClauseList: ...
    def self_group(self: _BCL, against: Optional[Any] = ...) -> Union[_BCL, Grouping[_T]]: ...

and_ = BooleanClauseList.and_
or_ = BooleanClauseList.or_

class Tuple(ClauseList, ColumnElement[_T]):
    type: _T = ...
    @overload
    def __init__(self, *clauses: ColumnElement[Any], type_: TypeEngine[_T], **kw: Any) -> None: ...
    @overload
    def __init__(self, *clauses: ColumnElement[Any], type_: Type[TypeEngine[_T]], **kw: Any) -> None: ...
    @overload
    def __init__(self, clause: ColumnElement[_T], *clauses: ColumnElement[Any], **kw: Any) -> None: ...

class Case(ColumnElement[TypeEngine[_T]], Generic[_T]):
    __visit_name__: str = ...
    value: Any = ...
    type: TypeEngine[_T] = ...
    whens: Any = ...
    else_: Any = ...
    def __init__(self, whens: List[_TupleType[ClauseElement, _T]], value: Optional[_T] = ...,
                 else_: Optional[_T] = ...) -> None: ...
    def get_children(self, **kwargs: Any) -> Any: ...

@overload
def literal_column(text: str, type_: Optional[Type[_T]] = ...) -> ColumnClause[_T]: ...
@overload
def literal_column(text: str, type_: Optional[_T] = ...) -> ColumnClause[_T]: ...

class Cast(ColumnElement[_T], Generic[_T, _U]):
    __visit_name__: str = ...
    type: _T = ...
    clause: ClauseElement = ...
    typeclause: TypeClause[_T] = ...
    @overload
    def __init__(self, expression: Union[str, List[str], ColumnElement[_U], List[ColumnElement[_U]]], type_: _T) -> None: ...
    @overload
    def __init__(self,
                 expression: Union[str, List[str], ColumnElement[_U], List[ColumnElement[_U]]], type_: Type[_T]) -> None: ...
    def get_children(self, **kwargs: Any) -> _TupleType[ClauseElement, TypeClause[_T]]: ...

class TypeCoerce(ColumnElement[_T]):
    __visit_name__: str = ...
    type: _T = ...
    clause: ClauseElement = ...
    @overload
    def __init__(self, expression: str, type_: _T) -> None: ...
    @overload
    def __init__(self, expression: ColumnElement[Any], type_: _T) -> None: ...
    @overload
    def __init__(self, expression: str, type_: Type[_T]) -> None: ...
    @overload
    def __init__(self, expression: ColumnElement[Any], type_: Type[_T]) -> None: ...
    def get_children(self, **kwargs: Any) -> _TupleType[ClauseElement]: ...
    @property
    def typed_expression(self) -> Any: ...

class Extract(ColumnElement[Integer]):
    __visit_name__: str = ...
    type: Integer = ...
    field: Any = ...
    expr: ClauseElement = ...
    def __init__(self, field: Any, expr: ClauseElement, **kwargs: Any) -> None: ...
    def get_children(self, **kwargs) -> _TupleType[ClauseElement]: ...

_UE = TypeVar('_UE', bound=UnaryExpression)

class UnaryExpression(ColumnElement[_T]):
    __visit_name__: str = ...
    operator: Callable[..., Any] = ...
    modifier: Any = ...
    element: Any = ...
    type: _T = ...
    negate: Any = ...
    wraps_column_expression: bool = ...
    @overload
    def __init__(self, element: Any, operator: Optional[Callable[..., Any]] = ..., modifier: Optional[Any] = ...,
                 type_: Optional[_T] = ..., negate: Optional[Any] = ...,
                 wraps_column_expression: bool = ...) -> None: ...
    @overload
    def __init__(self, element: Any, operator: Optional[Callable[..., Any]] = ..., modifier: Optional[Any] = ...,
                 type_: Optional[Type[_T]] = ..., negate: Optional[Any] = ...,
                 wraps_column_expression: bool = ...) -> None: ...
    def get_children(self, **kwargs) -> _TupleType[Any]: ...
    def compare(self, other: Any, **kw: Any) -> bool: ...
    def self_group(self: _UE, against: Optional[Any] = ...) ->  Union[_UE, Grouping[_T]]: ...
    @classmethod
    def _create_nullsfirst(cls, column: ColumnElement[Any]) -> UnaryExpression[None]: ...
    @classmethod
    def _create_nullslast(cls, column: ColumnElement[Any]) -> UnaryExpression[None]: ...
    @classmethod
    def _create_desc(cls, column: ColumnElement[Any]) -> UnaryExpression[None]: ...
    @classmethod
    def _create_asc(cls, column: ColumnElement[Any]) -> UnaryExpression[None]: ...
    @classmethod
    def _create_distinct(cls, expr: ColumnElement[_U]) -> UnaryExpression[_U]: ...

class CollectionAggregate(UnaryExpression[_T]):
    def operate(self, op: Any, *other: Any, **kwargs: Any) -> Any: ...
    def reverse_operate(self, op: Any, other: Any, **kwargs: Any) -> Any: ...
    @overload
    @classmethod
    def _create_all(cls, expr: ColumnElement[_U]) -> CollectionAggregate[_U]: ...
    @overload
    @classmethod
    def _create_all(cls, expr: ClauseElement) -> CollectionAggregate[Any]: ...
    @overload
    @classmethod
    def _create_any(cls, expr: ColumnElement[_U]) -> CollectionAggregate[_U]: ...
    @overload
    @classmethod
    def _create_any(cls, expr: ClauseElement) -> CollectionAggregate[_U]: ...

_AB = TypeVar('_AB', bound=AsBoolean)

class AsBoolean(UnaryExpression):
    element: Any = ...
    type: Boolean = ...
    operator: Callable[..., Any] = ...
    negate: Any = ...
    modifier: Any = ...
    wraps_column_expression: bool = ...
    def __init__(self, element: Any, operator: Callable[..., Any], negate: Any) -> None: ...
    def self_group(self: _AB, against: Optional[Any] = ...) -> _AB: ...

_BE = TypeVar('_BE', bound=BinaryExpression)

class BinaryExpression(ColumnElement[_T], Generic[_T, _U, _V]):
    __visit_name__: str = ...
    left: Union[Grouping[_U], ColumnClause[_U]] = ...
    right: Union[Grouping[_V], ColumnElement[_V]] = ...
    operator: Callable[..., Any] = ...
    type: _T = ...
    negate: Any = ...
    modifiers: Any = ...
    @overload
    def __init__(self, left: ColumnClause[_U], right: ColumnClause[_V], operator: Callable[..., Any],
                 type_: Optional[_T] = ..., negate: Optional[Any] = ..., modifiers: Optional[Any] = ...) -> None: ...
    @overload
    def __init__(self, left: ColumnClause[_U], right: ColumnClause[_V], operator: Callable[..., Any],
                 type_: Optional[Type[_T]] = ..., negate: Optional[Any] = ..., modifiers: Optional[Any] = ...) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__: Any = ...
    @property
    def is_comparison(self): ...
    def get_children(self, **kwargs): ...
    def compare(self, other: Any, **kw: Any) -> bool: ...
    def self_group(self: _BE, against: Optional[Any] = ...) -> Union[_BE, Grouping[_T]]: ...

_SL = TypeVar('_SL', bound=Slice)

class Slice(ColumnElement[_T]):
    __visit_name__: str = ...
    start: Any = ...
    stop: Any = ...
    step: Any = ...
    type: _T = ...
    def __init__(self, start, stop, step) -> None: ...
    def self_group(self: _SL, against: Optional[Any] = ...) -> Union[_SL, Grouping[_T]]: ...

class IndexExpression(BinaryExpression): ...

_G = TypeVar('_G', bound=Grouping)

class Grouping(ColumnElement[Union[_T, NullType]], Generic[_T]):
    __visit_name__: str = ...
    element: ColumnElement[_T] = ...
    type: Union[_T, NullType] = ...
    def __init__(self, element: ColumnElement[_T]) -> None: ...
    def self_group(self: _G, against: Optional[Any] = ...) -> _G: ...
    def get_children(self, **kwargs) -> _TupleType[ColumnElement[_T]]: ...
    def __getattr__(self, attr): ...
    def compare(self, other: Any, **kw: Any) -> bool: ...

RANGE_UNBOUNDED: Any = ...
RANGE_CURRENT: Any = ...

class Over(ColumnElement[_T]):
    __visit_name__: str = ...
    order_by: Optional[ClauseList] = ...
    partition_by: Optional[ClauseList] = ...
    element: Union[WithinGroup[_T], FunctionElement[_T]] = ...
    range_: Optional[Any] = ...
    rows: Optional[Any] = ...
    @overload
    def __init__(self, element: WithinGroup[_T],
                 partition_by: Optional[Union[str, ColumnElement[Any], List[Union[str, ColumnElement[Any]]]]] = ...,
                 order_by: Optional[Union[str, ColumnElement[Any], List[Union[str, ColumnElement[Any]]]]] = ...,
                 range_: Optional[Any] = ..., rows: Optional[Any] = ...) -> None: ...
    @overload
    def __init__(self, element: FunctionElement[_T],
                 partition_by: Optional[Union[str, ColumnElement[Any], List[Union[str, ColumnElement[Any]]]]] = ...,
                 order_by: Optional[Union[str, ColumnElement[Any], List[Union[str, ColumnElement[Any]]]]] = ...,
                 range_: Optional[Any] = ..., rows: Optional[Any] = ...) -> None: ...
    @property
    def func(self) -> Union[WithinGroup[_T], FunctionElement[_T]]: ...
    @property
    def type(self) -> _T: ...
    def get_children(self, **kwargs: Any) -> List[Union[WithinGroup[_T], FunctionElement[_T], ClauseList]]: ...

class WithinGroup(ColumnElement[_T]):
    __visit_name__: str = ...
    order_by: Optional[ClauseList] = ...
    element: FunctionElement[_T] = ...
    def __init__(self, element: FunctionElement[_T],
                 *order_by: Union[str, ColumnElement[Any], List[Union[str, ColumnElement[Any]]]]) -> None: ...
    def over(self, partition_by: Optional[Union[str, ColumnElement[Any], List[Union[str, ColumnElement[Any]]]]] = ...,
             order_by: Optional[Union[str, ColumnElement[Any], List[Union[str, ColumnElement[Any]]]]] = ...) -> Over[_T]: ...
    @property
    def type(self) -> _T: ...
    def get_children(self, **kwargs: Any) -> List[Union[FunctionElement[_T], ClauseList]]: ...

class FunctionFilter(ColumnElement[_T]):
    __visit_name__: str = ...
    criterion: Any = ...
    func: FunctionElement[_T] = ...
    def __init__(self, func: FunctionElement[_T], *criterion: Any) -> None: ...
    def filter(self, *criterion: Any) -> FunctionFilter[_T]: ...
    def over(self, partition_by: Optional[Union[str, ColumnElement[Any], List[Union[str, ColumnElement[Any]]]]] = ...,
             order_by: Optional[Union[str, ColumnElement[Any], List[Union[str, ColumnElement[Any]]]]] = ...) -> Over[_T]: ...
    @property
    def type(self) -> _T: ...
    def get_children(self, **kwargs: Any) -> List[Any]: ...

_L = TypeVar('_L', bound=Label)

class Label(ColumnElement[_T]):
    __visit_name__: str = ...
    name: str = ...
    key: str = ...
    @overload
    def __init__(self, name: str, element: ColumnElement[_T]) -> None: ...
    @overload
    def __init__(self, name: str, element: ColumnElement[Any], type_: _T = ...) -> None: ...
    @overload
    def __init__(self, name: str, element: ColumnElement[Any], type_: Type[_T] = ...) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def type(self) -> Union[_T, NullType]: ...  # type: ignore
    @property
    def element(self) -> ColumnElement[_T]: ...
    def self_group(self, against: Optional[Any] = ...) -> Union[ColumnElement[_T], Grouping[_T]]: ...
    @property
    def primary_key(self) -> Any: ...
    @property
    def foreign_keys(self) -> List[Any]: ...  # type: ignore
    def get_children(self, **kwargs: Any) -> Any: ...

class ColumnClause(Immutable, ColumnElement[_T]):
    __visit_name__: str = ...
    onupdate: Any = ...
    default: Any = ...
    server_default: Any = ...
    server_onupdate: Any = ...
    key: str = ...
    name: str = ...
    table: Optional[TableClause] = ...
    type: Union[_T, NullType] = ...  # type: ignore
    is_literal: bool = ...
    @overload
    def __init__(self, text: str, type_: Optional[Type[_T]] = ..., is_literal: bool = ...,
                 _selectable: Optional[TableClause] = ...) -> None: ...
    @overload
    def __init__(self, text: str, type_: Optional[_T] = ..., is_literal: bool = ...,
                 _selectable: Optional[TableClause] = ...) -> None: ...
    @property
    def description(self) -> str: ...

class _IdentifiedClause(Executable, ClauseElement):
    __visit_name__: str = ...
    ident: Any = ...
    def __init__(self, ident: Any) -> None: ...

class SavepointClause(_IdentifiedClause):
    __visit_name__: str = ...

class RollbackToSavepointClause(_IdentifiedClause):
    __visit_name__: str = ...

class ReleaseSavepointClause(_IdentifiedClause):
    __visit_name__: str = ...

class quoted_name(util.MemoizedSlots, util.text_type):
    quote: Any = ...
    def __new__(cls, value, quote): ...
    def __reduce__(self): ...

class _truncated_label(quoted_name):
    def __new__(cls, value, quote: Optional[Any] = ...): ...
    def __reduce__(self): ...
    def apply_map(self, map_): ...

class conv(_truncated_label): ...

class AnnotatedColumnElement(Annotated, Generic[_T]):
    def __init__(self, element: ColumnElement[_T], values: Any) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def table(self) -> TableClause: ...
    @property
    def key(self) -> str: ...
    @property
    def info(self) -> Any: ...
    @property
    def anon_label(self) -> str: ...
