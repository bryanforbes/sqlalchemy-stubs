from typing import Any, Optional, Set, Dict, List, Set, Pattern, TypeVar, Type
from .. import util, engine
from .elements import ClauseElement, BindParameter
from .type_api import TypeEngine

RESERVED_WORDS: Set[str] = ...
LEGAL_CHARACTERS: Pattern[str] = ...
ILLEGAL_INITIAL_CHARACTERS: Set[str] = ...
BIND_PARAMS: Pattern[str] = ...
BIND_PARAMS_ESC: Pattern[str] = ...
BIND_TEMPLATES: Dict[str, str] = ...
OPERATORS: Dict[Any, str] = ...
FUNCTIONS: Dict[Any, str] = ...
EXTRACT_MAP: Dict[str, str] = ...
COMPOUND_KEYWORDS: Dict[Any, str] = ...

class Compiled(object):
    execution_options: Any = ...
    dialect: engine.Dialect = ...
    bind: Any = ...
    preparer: Any = ...
    statement: ClauseElement = ...
    can_execute: Optional[bool] = ...
    string: Optional[str] = ...
    def __init__(self, dialect: engine.Dialect, statement: ClauseElement, bind: Optional[Any] = ...,
                 schema_translate_map: Optional[Any] = ..., compile_kwargs: Any = ...) -> None: ...
    def compile(self) -> str: ...
    @property
    def sql_compiler(self) -> Any: ...
    def process(self, obj: Any, **kwargs: Any) -> str: ...
    def __str__(self) -> str: ...
    def construct_params(self, params: Optional[Dict[str, Any]] = ...) -> Any: ...
    @property
    def params(self) -> Optional[Dict[str, Any]]: ...
    def execute(self, *multiparams: Any, **params: Any) -> engine.ResultProxy: ...
    def scalar(self, *multiparams: Any, **params: Any) -> Any: ...

class TypeCompiler(metaclass=util.EnsureKWArgType):
    ensure_kwarg: str = ...
    dialect: engine.Dialect = ...
    def __init__(self, dialect: engine.Dialect) -> None: ...
    def process(self, type_: TypeEngine[Any], **kw: Any) -> str: ...

_SQLC = TypeVar('_SQLC', bound=SQLCompiler)

class SQLCompiler(Compiled):
    extract_map: Dict[str, str] = ...
    compound_keywords: Dict[Any, str] = ...
    isdelete: bool = ...
    isinsert: bool = ...
    isupdate: bool = ...
    isplaintext: bool = ...
    returning: Any = ...
    returning_precedes_values: bool = ...
    render_table_with_column_in_update_from: bool = ...
    ansi_bind_rules: bool = ...
    insert_prefetch: Any = ...
    update_prefetch: Any = ...
    column_keys: Optional[List[str]] = ...
    inline: bool = ...
    binds: Dict[str, BindParameter[Any]] = ...
    bind_names: Any = ...
    stack: Any = ...
    positional: Any = ...
    positiontup: Any = ...
    bindtemplate: Any = ...
    ctes: Any = ...
    label_length: Any = ...
    anon_map: Any = ...
    truncated_names: Any = ...
    def __init__(self, dialect: engine.Dialect, statement: ClauseElement, column_keys: Optional[List[str]] = ...,
                 inline: bool = ..., **kwargs: Any) -> None: ...
    @property
    def prefetch(self) -> List[Any]: ...
    def is_subquery(self) -> bool: ...
    @property
    def sql_compiler(self: _SQLC) -> _SQLC: ...
    def construct_params(self, params: Optional[Any] = ..., _group_number: Optional[Any] = ...,
                         _check: bool = ...) -> Optional[Dict[str, Any]]: ...
    @property
    def params(self) -> Optional[Dict[str, Any]]: ...
    def default_from(self) -> str: ...
    def visit_grouping(self, grouping: Any, asfrom: bool = ..., **kwargs: Any) -> str: ...
    def visit_label_reference(self, element, within_columns_clause: bool = ..., **kwargs: Any) -> str: ...
    def visit_textual_label_reference(self, element, within_columns_clause: bool = ..., **kwargs: Any) -> str: ...
    def visit_label(self, label, add_to_result_map: Optional[Any] = ..., within_label_clause: bool = ...,
                    within_columns_clause: bool = ..., render_label_as_label: Optional[Any] = ..., **kw: Any) -> str: ...
    def visit_column(self, column, add_to_result_map: Optional[Any] = ..., include_table: bool = ..., **kwargs: Any) -> str: ...
    def escape_literal_column(self, text: str) -> str: ...
    def visit_collation(self, element, **kw: Any) -> str: ...
    def visit_fromclause(self, fromclause, **kwargs: Any) -> str: ...
    def visit_index(self, index, **kwargs: Any) -> str: ...
    def visit_typeclause(self, typeclause, **kw: Any) -> str: ...
    def post_process_text(self, text: str) -> str: ...
    def visit_textclause(self, textclause, **kw: Any) -> str: ...
    def visit_text_as_from(self, taf, compound_index: Optional[Any] = ..., asfrom: bool = ...,
                           parens: bool = ..., **kw: Any) -> str: ...
    def visit_null(self, expr, **kw: Any) -> str: ...
    def visit_true(self, expr, **kw: Any) -> str: ...
    def visit_false(self, expr, **kw: Any) -> str: ...
    def visit_clauselist(self, clauselist, **kw: Any) -> str: ...
    def visit_case(self, clause, **kwargs: Any) -> str: ...
    def visit_type_coerce(self, type_coerce, **kw: Any) -> str: ...
    def visit_cast(self, cast, **kwargs: Any) -> str: ...
    def visit_over(self, over, **kwargs: Any) -> str: ...
    def visit_withingroup(self, withingroup, **kwargs: Any) -> str: ...
    def visit_funcfilter(self, funcfilter, **kwargs: Any) -> str: ...
    def visit_extract(self, extract, **kwargs: Any) -> str: ...
    def visit_function(self, func, add_to_result_map: Optional[Any] = ..., **kwargs: Any) -> str: ...
    def visit_next_value_func(self, next_value, **kw: Any) -> str: ...
    def visit_sequence(self, sequence, **kw: Any) -> str: ...
    def function_argspec(self, func, **kwargs: Any) -> str: ...
    def visit_compound_select(self, cs, asfrom: bool = ..., parens: bool = ...,
                              compound_index: int = ..., **kwargs: Any) -> str: ...
    def visit_unary(self, unary, **kw: Any) -> str: ...
    def visit_istrue_unary_operator(self, element, operator, **kw: Any) -> str: ...
    def visit_isfalse_unary_operator(self, element, operator, **kw: Any) -> str: ...
    def visit_notmatch_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_binary(self, binary, override_operator: Optional[Any] = ...,
                     eager_grouping: bool = ..., **kw: Any) -> str: ...
    def visit_mod_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_custom_op_binary(self, element, operator, **kw: Any) -> str: ...
    def visit_custom_op_unary_operator(self, element, operator, **kw: Any) -> str: ...
    def visit_custom_op_unary_modifier(self, element, operator, **kw: Any) -> str: ...
    def visit_contains_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_notcontains_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_startswith_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_notstartswith_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_endswith_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_notendswith_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_like_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_notlike_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_ilike_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_notilike_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_between_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_notbetween_op_binary(self, binary, operator, **kw: Any) -> str: ...
    def visit_bindparam(self, bindparam, within_columns_clause: bool = ..., literal_binds: bool = ...,
                        skip_bind_expression: bool = ..., **kwargs: Any) -> str: ...
    def render_literal_bindparam(self, bindparam, **kw: Any) -> str: ...
    def render_literal_value(self, value, type_) -> str: ...
    def bindparam_string(self, name, positional_names: Optional[Any] = ..., **kw: Any) -> str: ...
    execution_options: Any = ...
    ctes_recursive: bool = ...
    def visit_cte(self, cte, asfrom: bool = ..., ashint: bool = ...,
                  fromhints: Optional[Any] = ..., **kwargs: Any) -> str: ...
    def visit_alias(self, alias, asfrom: bool = ..., ashint: bool = ..., iscrud: bool = ...,
                    fromhints: Optional[Any] = ..., **kwargs: Any) -> str: ...
    def visit_lateral(self, lateral, **kw: Any) -> str: ...
    def visit_tablesample(self, tablesample, asfrom: bool = ..., **kw: Any) -> str: ...
    def get_render_as_alias_suffix(self, alias_name_text) -> str: ...
    def format_from_hint_text(self, sqltext, table, hint, iscrud) -> str: ...
    def get_select_hint_text(self, byfroms) -> str: ...
    def get_from_hint_text(self, table, text) -> str: ...
    def get_crud_hint_text(self, table, text) -> str: ...
    def get_statement_hint_text(self, hint_texts) -> str: ...
    def visit_select(self, select, asfrom: bool = ..., parens: bool = ..., fromhints: Optional[Any] = ...,
                     compound_index: int = ..., nested_join_translation: bool = ...,
                     select_wraps_for: Optional[Any] = ..., lateral: bool = ..., **kwargs: Any) -> str: ...
    def get_cte_preamble(self, recursive) -> str: ...
    def get_select_precolumns(self, select, **kw: Any) -> str: ...
    def order_by_clause(self, select, **kw: Any) -> str: ...
    def for_update_clause(self, select, **kw: Any) -> str: ...
    def returning_clause(self, stmt, returning_cols) -> str: ...
    def limit_clause(self, select, **kw: Any) -> str: ...
    def visit_table(self, table, asfrom: bool = ..., iscrud: bool = ..., ashint: bool = ...,
                    fromhints: Optional[Any] = ..., use_schema: bool = ..., **kwargs: Any) -> str: ...
    def visit_join(self, join, asfrom: bool = ..., **kwargs: Any) -> str: ...
    def visit_insert(self, insert_stmt, asfrom: bool = ..., **kw: Any) -> str: ...
    def update_limit_clause(self, update_stmt) -> str: ...
    def update_tables_clause(self, update_stmt, from_table, extra_froms, **kw: Any) -> str: ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw: Any) -> str: ...
    def visit_update(self, update_stmt, asfrom: bool = ..., **kw: Any) -> str: ...
    def delete_extra_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw: Any) -> str: ...
    def delete_table_clause(self, delete_stmt, from_table, extra_froms) -> str: ...
    def visit_delete(self, delete_stmt, asfrom: bool = ..., **kw: Any) -> str: ...
    def visit_savepoint(self, savepoint_stmt) -> str: ...
    def visit_rollback_to_savepoint(self, savepoint_stmt) -> str: ...
    def visit_release_savepoint(self, savepoint_stmt) -> str: ...

class StrSQLCompiler(SQLCompiler):
    def visit_getitem_binary(self, binary, operator, **kw): ...
    def visit_json_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_json_path_getitem_op_binary(self, binary, operator, **kw): ...
    def returning_clause(self, stmt, returning_cols): ...

class DDLCompiler(Compiled):
    @property
    def sql_compiler(self) -> SQLCompiler: ...
    @property
    def type_compiler(self) -> Type[TypeCompiler]: ...
    def construct_params(self, params: Optional[Any] = ...) -> Any: ...
    def visit_ddl(self, ddl, **kwargs) -> str: ...
    def visit_create_schema(self, create) -> str: ...
    def visit_drop_schema(self, drop) -> str: ...
    def visit_create_table(self, create) -> Optional[str]: ...
    def visit_create_column(self, create, first_pk: bool = ...) -> str: ...
    def create_table_constraints(self, table, _include_foreign_key_constraints: Optional[Any] = ...) -> str: ...
    def visit_drop_table(self, drop) -> str: ...
    def visit_drop_view(self, drop) -> str: ...
    def visit_create_index(self, create, include_schema: bool = ..., include_table_schema: bool = ...) -> str: ...
    def visit_drop_index(self, drop) -> str: ...
    def visit_add_constraint(self, create) -> str: ...
    def visit_set_table_comment(self, create) -> str: ...
    def visit_drop_table_comment(self, drop) -> str: ...
    def visit_set_column_comment(self, create) -> str: ...
    def visit_drop_column_comment(self, drop) -> str: ...
    def visit_create_sequence(self, create) -> str: ...
    def visit_drop_sequence(self, drop) -> str: ...
    def visit_drop_constraint(self, drop) -> str: ...
    def get_column_specification(self, column, **kwargs) -> str: ...
    def create_table_suffix(self, table) -> str: ...
    def post_create_table(self, table) -> str: ...
    def get_column_default_string(self, column) -> Optional[str]: ...
    def visit_check_constraint(self, constraint) -> str: ...
    def visit_column_check_constraint(self, constraint) -> str: ...
    def visit_primary_key_constraint(self, constraint) -> str: ...
    def visit_foreign_key_constraint(self, constraint) -> str: ...
    def define_constraint_remote_table(self, constraint, table, preparer) -> str: ...
    def visit_unique_constraint(self, constraint) -> str: ...
    def define_constraint_cascades(self, constraint) -> str: ...
    def define_constraint_deferrability(self, constraint) -> str: ...
    def define_constraint_match(self, constraint) -> str: ...

class GenericTypeCompiler(TypeCompiler):
    def visit_FLOAT(self, type_, **kw) -> str: ...
    def visit_REAL(self, type_, **kw) -> str: ...
    def visit_NUMERIC(self, type_, **kw) -> str: ...
    def visit_DECIMAL(self, type_, **kw) -> str: ...
    def visit_INTEGER(self, type_, **kw) -> str: ...
    def visit_SMALLINT(self, type_, **kw) -> str: ...
    def visit_BIGINT(self, type_, **kw) -> str: ...
    def visit_TIMESTAMP(self, type_, **kw) -> str: ...
    def visit_DATETIME(self, type_, **kw) -> str: ...
    def visit_DATE(self, type_, **kw) -> str: ...
    def visit_TIME(self, type_, **kw) -> str: ...
    def visit_CLOB(self, type_, **kw) -> str: ...
    def visit_NCLOB(self, type_, **kw) -> str: ...
    def visit_CHAR(self, type_, **kw) -> str: ...
    def visit_NCHAR(self, type_, **kw) -> str: ...
    def visit_VARCHAR(self, type_, **kw) -> str: ...
    def visit_NVARCHAR(self, type_, **kw) -> str: ...
    def visit_TEXT(self, type_, **kw) -> str: ...
    def visit_BLOB(self, type_, **kw) -> str: ...
    def visit_BINARY(self, type_, **kw) -> str: ...
    def visit_VARBINARY(self, type_, **kw) -> str: ...
    def visit_BOOLEAN(self, type_, **kw) -> str: ...
    def visit_large_binary(self, type_, **kw) -> str: ...
    def visit_boolean(self, type_, **kw) -> str: ...
    def visit_time(self, type_, **kw) -> str: ...
    def visit_datetime(self, type_, **kw) -> str: ...
    def visit_date(self, type_, **kw) -> str: ...
    def visit_big_integer(self, type_, **kw) -> str: ...
    def visit_small_integer(self, type_, **kw) -> str: ...
    def visit_integer(self, type_, **kw) -> str: ...
    def visit_real(self, type_, **kw) -> str: ...
    def visit_float(self, type_, **kw) -> str: ...
    def visit_numeric(self, type_, **kw) -> str: ...
    def visit_string(self, type_, **kw) -> str: ...
    def visit_unicode(self, type_, **kw) -> str: ...
    def visit_text(self, type_, **kw) -> str: ...
    def visit_unicode_text(self, type_, **kw) -> str: ...
    def visit_enum(self, type_, **kw) -> str: ...
    def visit_null(self, type_, **kw) -> str: ...
    def visit_type_decorator(self, type_, **kw) -> str: ...
    def visit_user_defined(self, type_, **kw) -> str: ...

class StrSQLTypeCompiler(GenericTypeCompiler):
    def __getattr__(self, key: str) -> Any: ...

class IdentifierPreparer(object):
    reserved_words: Set[str] = ...
    legal_characters: Pattern[str] = ...
    illegal_initial_characters: Pattern[str] = ...
    schema_for_object: Any = ...
    dialect: engine.Dialect = ...
    initial_quote: str = ...
    final_quote: str = ...
    escape_quote: str = ...
    escape_to_quote: str = ...
    omit_schema: bool = ...
    quote_case_sensitive_collations: bool = ...
    def __init__(self, dialect, initial_quote: str = ..., final_quote: Optional[str] = ...,
                 escape_quote: str = ..., omit_schema: bool = ...) -> None: ...
    def quote_identifier(self, value: str) -> str: ...
    def quote_schema(self, schema: Any, force: Optional[bool] = ...) -> str: ...
    def quote(self, ident: Any, force: Optional[bool] = ...) -> str: ...
    def format_collation(self, collation_name: str) -> str: ...
    def format_sequence(self, sequence: Any, use_schema: bool = ...) -> str: ...
    def format_label(self, label: Any, name: Optional[str] = ...) -> str: ...
    def format_alias(self, alias, name: Optional[Any] = ...) -> str: ...
    def format_savepoint(self, savepoint, name: Optional[Any] = ...) -> str: ...
    def format_constraint(self, constraint: Any) -> str: ...
    def format_table(self, table: Any, use_schema: bool = ..., name: Optional[str] = ...) -> str: ...
    def format_schema(self, name: Any, quote: Optional[bool] = ...) -> str: ...
    def format_column(self, column: Any, use_table: bool = ..., name: Optional[str] = ...,
                      table_name: Optional[str] = ...) -> str: ...
    def format_table_seq(self, table: Any, use_schema: bool = ...) -> str: ...
    def unformat_identifiers(self, identifiers: Any) -> List[Any]: ...
