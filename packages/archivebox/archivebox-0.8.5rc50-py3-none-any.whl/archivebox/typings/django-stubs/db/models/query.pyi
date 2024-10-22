import datetime
from collections.abc import AsyncIterator, Collection, Iterable, Iterator, Mapping, Sequence, Sized
from typing import TypeVar, TypedDict, Any, Generic, NamedTuple, overload

from django.db.backends.utils import _ExecuteQuery
from django.db.models import Manager
from django.db.models.base import Model
from django.db.models.expressions import Combinable, OrderBy
from django.db.models.sql.query import Query, RawQuery
from django.utils.functional import cached_property
from typing_extensions import Required, Unpack, Self, TypeAlias, TypeVar
from api.models import APIToken, OutboundWebhook
from core.models import ArchiveResult, Snapshot, SnapshotTag, Tag
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from uuid import UUID

class PermissionCreateKwargs(TypedDict, total=False):
    id: int | str | Combinable

    name: str | int | Combinable

    content_type: ContentType | Combinable

    codename: str | int | Combinable

class GroupCreateKwargs(TypedDict, total=False):
    id: int | str | Combinable

    name: str | int | Combinable

class UserCreateKwargs(TypedDict, total=False):
    id: int | str | Combinable

    password: str | int | Combinable

    last_login: str | datetime.datetime | datetime.date | Combinable | None

    is_superuser: bool | Combinable
    """Designates that this user has all permissions without explicitly assigning them."""

    username: str | int | Combinable
    """Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."""

    first_name: str | int | Combinable

    last_name: str | int | Combinable

    email: str | int | Combinable

    is_staff: bool | Combinable
    """Designates whether the user can log into this admin site."""

    is_active: bool | Combinable
    """Designates whether this user should be treated as active. Unselect this instead of deleting accounts."""

    date_joined: str | datetime.datetime | datetime.date | Combinable

class ContentTypeCreateKwargs(TypedDict, total=False):
    id: int | str | Combinable

    app_label: str | int | Combinable

    model: str | int | Combinable

class SessionCreateKwargs(TypedDict, total=False):
    session_key: str | int | Combinable

    session_data: str | Combinable

    expire_date: str | datetime.datetime | datetime.date | Combinable

class LogEntryCreateKwargs(TypedDict, total=False):
    id: int | str | Combinable

    action_time: str | datetime.datetime | datetime.date | Combinable

    user: User | Combinable

    content_type: ContentType | Combinable | None

    object_id: str | Combinable | None

    object_repr: str | int | Combinable

    action_flag: float | int | str | Combinable

    change_message: str | Combinable

class TagCreateKwargs(TypedDict, total=False):
    created_by: User | Combinable

    created: str | datetime.datetime | datetime.date | Combinable

    modified: str | datetime.datetime | datetime.date | Combinable

    old_id: float | int | str | Combinable

    id: str | UUID

    abid: str | int | Combinable | None
    """ABID-format identifier for this entity (e.g. snp_01BJQMF54D093DXEAWZ6JYRPAQ)"""

    name: str | int | Combinable

    slug: str | int | Combinable

class SnapshotTagCreateKwargs(TypedDict, total=False):
    id: int | str | Combinable

    snapshot: Snapshot | Combinable

    tag: Tag | Combinable

class SnapshotCreateKwargs(TypedDict, total=False):
    created_by: User | Combinable

    created: str | datetime.datetime | datetime.date | Combinable

    modified: str | datetime.datetime | datetime.date | Combinable

    old_id: str | UUID

    id: str | UUID

    abid: str | int | Combinable | None
    """ABID-format identifier for this entity (e.g. snp_01BJQMF54D093DXEAWZ6JYRPAQ)"""

    url: str | int | Combinable

    timestamp: str | int | Combinable

    title: str | int | Combinable | None

    added: str | datetime.datetime | datetime.date | Combinable

    updated: str | datetime.datetime | datetime.date | Combinable | None

class ArchiveResultCreateKwargs(TypedDict, total=False):
    created_by: User | Combinable

    created: str | datetime.datetime | datetime.date | Combinable

    modified: str | datetime.datetime | datetime.date | Combinable

    old_id: float | int | str | Combinable

    id: str | UUID

    abid: str | int | Combinable | None
    """ABID-format identifier for this entity (e.g. snp_01BJQMF54D093DXEAWZ6JYRPAQ)"""

    snapshot: Snapshot | Combinable

    extractor: str | int | Combinable

    cmd: Any

    pwd: str | int | Combinable

    cmd_version: str | int | Combinable | None

    output: str | int | Combinable

    start_ts: str | datetime.datetime | datetime.date | Combinable

    end_ts: str | datetime.datetime | datetime.date | Combinable

    status: str | int | Combinable

class APITokenCreateKwargs(TypedDict, total=False):
    modified: str | datetime.datetime | datetime.date | Combinable

    id: str | UUID

    abid: str | int | Combinable | None
    """ABID-format identifier for this entity (e.g. snp_01BJQMF54D093DXEAWZ6JYRPAQ)"""

    created_by: User | Combinable

    created: str | datetime.datetime | datetime.date | Combinable

    token: str | int | Combinable

    expires: str | datetime.datetime | datetime.date | Combinable | None

class OutboundWebhookCreateKwargs(TypedDict, total=False):
    name: str | int | Combinable
    """Give your webhook a descriptive name (e.g. Notify ACME Slack channel of any new ArchiveResults)."""

    signal: str | int | Combinable
    """The type of event the webhook should fire for (e.g. Create, Update, Delete)."""

    ref: str | int | Combinable
    """Dot import notation of the model the webhook should fire for (e.g. core.models.Snapshot or core.models.ArchiveResult)."""

    endpoint: str | int | Combinable
    """External URL to POST the webhook notification to (e.g. https://someapp.example.com/webhook/some-webhook-receiver)."""

    headers: Any
    """Headers to send with the webhook request."""

    auth_token: str | int | Combinable
    """Authentication token to use in an Authorization header."""

    enabled: bool | Combinable
    """Is this webhook enabled?"""

    keep_last_response: bool | Combinable
    """Should the webhook keep a log of the latest response it got?"""

    updated: str | datetime.datetime | datetime.date | Combinable
    """When the webhook was last updated."""

    last_response: str | int | Combinable
    """Latest response to this webhook."""

    last_success: str | datetime.datetime | datetime.date | Combinable | None
    """When the webhook last succeeded."""

    last_failure: str | datetime.datetime | datetime.date | Combinable | None
    """When the webhook last failed."""

    id: str | UUID

    abid: str | int | Combinable | None
    """ABID-format identifier for this entity (e.g. snp_01BJQMF54D093DXEAWZ6JYRPAQ)"""

    created_by: User | Combinable

    created: str | datetime.datetime | datetime.date | Combinable

    modified: str | datetime.datetime | datetime.date | Combinable

_T = TypeVar("_T", covariant=True)
_Model = TypeVar("_Model", bound=Model, covariant=True)
_Row = TypeVar("_Row", covariant=True, default=_Model)  # ONLY use together with _Model
_QS = TypeVar("_QS", bound=_QuerySet)
_TupleT = TypeVar("_TupleT", bound=tuple[Any, ...], covariant=True)

MAX_GET_RESULTS: int
REPR_OUTPUT_SIZE: int

class BaseIterable(Generic[_T]):
    queryset: QuerySet[Model]
    chunked_fetch: bool
    chunk_size: int
    def __init__(self, queryset: QuerySet[Model], chunked_fetch: bool = ..., chunk_size: int = ...) -> None: ...
    def __aiter__(self) -> AsyncIterator[_T]: ...

class ModelIterable(Generic[_Model], BaseIterable[_Model]):
    def __iter__(self) -> Iterator[_Model]: ...

class RawModelIterable(BaseIterable[dict[str, Any]]):
    def __iter__(self) -> Iterator[dict[str, Any]]: ...

class ValuesIterable(BaseIterable[dict[str, Any]]):
    def __iter__(self) -> Iterator[dict[str, Any]]: ...

class ValuesListIterable(BaseIterable[_TupleT]):
    def __iter__(self) -> Iterator[_TupleT]: ...

class NamedValuesListIterable(ValuesListIterable[NamedTuple]):
    def __iter__(self) -> Iterator[NamedTuple]: ...

class FlatValuesListIterable(BaseIterable[_T]):
    def __iter__(self) -> Iterator[_T]: ...

class QuerySet(Generic[_Model, _Row], Iterable[_Row], Sized):
    model: type[_Model]
    query: Query
    _iterable_class: type[BaseIterable]
    _result_cache: list[_Row] | None
    def __init__(
        self,
        model: type[Model] | None = ...,
        query: Query | None = ...,
        using: str | None = ...,
        hints: dict[str, Model] | None = ...,
    ) -> None: ...
    @classmethod
    def as_manager(cls) -> Manager[_Model]: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __class_getitem__(cls: type[_QS], item: type[_Model]) -> type[_QS]: ...
    def __getstate__(self) -> dict[str, Any]: ...
    # Technically, the other QuerySet must be of the same type _T, but _T is covariant
    def __and__(self, other: QuerySet[_Model, _Row]) -> Self: ...
    def __or__(self, other: QuerySet[_Model, _Row]) -> Self: ...
    # IMPORTANT: When updating any of the following methods' signatures, please ALSO modify
    # the corresponding method in BaseManager.
    def iterator(self, chunk_size: int | None = ...) -> Iterator[_Row]: ...
    def aiterator(self, chunk_size: int = ...) -> AsyncIterator[_Row]: ...
    def aggregate(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...
    async def aaggregate(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...
    def get(self, *args: Any, **kwargs: Any) -> _Row: ...
    async def aget(self, *args: Any, **kwargs: Any) -> _Row: ...
    def create(self, **kwargs: Any) -> _Model: ...
    async def acreate(self, **kwargs: Any) -> _Model: ...
    def bulk_create(
        self,
        objs: Iterable[_Model],
        batch_size: int | None = ...,
        ignore_conflicts: bool = ...,
        update_conflicts: bool = ...,
        update_fields: Collection[str] | None = ...,
        unique_fields: Collection[str] | None = ...,
    ) -> list[_Model]: ...
    async def abulk_create(
        self,
        objs: Iterable[_Model],
        batch_size: int | None = ...,
        ignore_conflicts: bool = ...,
        update_conflicts: bool = ...,
        update_fields: Collection[str] | None = ...,
        unique_fields: Collection[str] | None = ...,
    ) -> list[_Model]: ...
    def bulk_update(self, objs: Iterable[_Model], fields: Iterable[str], batch_size: int | None = ...) -> int: ...
    async def abulk_update(
        self, objs: Iterable[_Model], fields: Iterable[str], batch_size: int | None = ...
    ) -> int: ...
    def get_or_create(self, defaults: Mapping[str, Any] | None = ..., **kwargs: Any) -> tuple[_Model, bool]: ...
    async def aget_or_create(self, defaults: Mapping[str, Any] | None = ..., **kwargs: Any) -> tuple[_Model, bool]: ...
    def update_or_create(
        self,
        defaults: Mapping[str, Any] | None = ...,
        create_defaults: Mapping[str, Any] | None = ...,
        **kwargs: Any,
    ) -> tuple[_Model, bool]: ...
    async def aupdate_or_create(
        self,
        defaults: Mapping[str, Any] | None = ...,
        create_defaults: Mapping[str, Any] | None = ...,
        **kwargs: Any,
    ) -> tuple[_Model, bool]: ...
    def earliest(self, *fields: str | OrderBy) -> _Row: ...
    async def aearliest(self, *fields: str | OrderBy) -> _Row: ...
    def latest(self, *fields: str | OrderBy) -> _Row: ...
    async def alatest(self, *fields: str | OrderBy) -> _Row: ...
    def first(self) -> _Row | None: ...
    async def afirst(self) -> _Row | None: ...
    def last(self) -> _Row | None: ...
    async def alast(self) -> _Row | None: ...
    def in_bulk(self, id_list: Iterable[Any] | None = ..., *, field_name: str = ...) -> dict[Any, _Model]: ...
    async def ain_bulk(self, id_list: Iterable[Any] | None = ..., *, field_name: str = ...) -> dict[Any, _Model]: ...
    def delete(self) -> tuple[int, dict[str, int]]: ...
    async def adelete(self) -> tuple[int, dict[str, int]]: ...
    def update(self, **kwargs: Any) -> int: ...
    async def aupdate(self, **kwargs: Any) -> int: ...
    def exists(self) -> bool: ...
    async def aexists(self) -> bool: ...
    def explain(self, *, format: Any | None = ..., **options: Any) -> str: ...
    async def aexplain(self, *, format: Any | None = ..., **options: Any) -> str: ...
    def contains(self, obj: Model) -> bool: ...
    async def acontains(self, obj: Model) -> bool: ...
    def raw(
        self,
        raw_query: _ExecuteQuery,
        params: Any = ...,
        translations: dict[str, str] | None = ...,
        using: str | None = ...,
    ) -> RawQuerySet: ...
    # The type of values may be overridden to be more specific in the mypy plugin, depending on the fields param
    def values(self, *fields: str | Combinable, **expressions: Any) -> QuerySet[_Model, dict[str, Any]]: ...
    # The type of values_list may be overridden to be more specific in the mypy plugin, depending on the fields param
    def values_list(self, *fields: str | Combinable, flat: bool = ..., named: bool = ...) -> QuerySet[_Model, Any]: ...
    def dates(self, field_name: str, kind: str, order: str = ...) -> QuerySet[_Model, datetime.date]: ...
    def datetimes(
        self, field_name: str, kind: str, order: str = ..., tzinfo: datetime.tzinfo | None = ...
    ) -> QuerySet[_Model, datetime.datetime]: ...
    def none(self) -> Self: ...
    def all(self) -> Self: ...
    def filter(self, *args: Any, **kwargs: Any) -> Self: ...
    def exclude(self, *args: Any, **kwargs: Any) -> Self: ...
    def complex_filter(self, filter_obj: Any) -> Self: ...
    def count(self) -> int: ...
    async def acount(self) -> int: ...
    def union(self, *other_qs: Any, all: bool = ...) -> Self: ...
    def intersection(self, *other_qs: Any) -> Self: ...
    def difference(self, *other_qs: Any) -> Self: ...
    def select_for_update(
        self, nowait: bool = ..., skip_locked: bool = ..., of: Sequence[str] = ..., no_key: bool = ...
    ) -> Self: ...
    def select_related(self, *fields: Any) -> Self: ...
    def prefetch_related(self, *lookups: Any) -> Self: ...
    def annotate(self, *args: Any, **kwargs: Any) -> Self: ...
    def alias(self, *args: Any, **kwargs: Any) -> Self: ...
    def order_by(self, *field_names: Any) -> Self: ...
    def distinct(self, *field_names: Any) -> Self: ...
    # extra() return type won't be supported any time soon
    def extra(
        self,
        select: dict[str, Any] | None = ...,
        where: Sequence[str] | None = ...,
        params: Sequence[Any] | None = ...,
        tables: Sequence[str] | None = ...,
        order_by: Sequence[str] | None = ...,
        select_params: Sequence[Any] | None = ...,
    ) -> QuerySet[Any, Any]: ...
    def reverse(self) -> Self: ...
    def defer(self, *fields: Any) -> Self: ...
    def only(self, *fields: Any) -> Self: ...
    def using(self, alias: str | None) -> Self: ...
    @property
    def ordered(self) -> bool: ...
    @property
    def db(self) -> str: ...
    def _fetch_all(self) -> None: ...
    def resolve_expression(self, *args: Any, **kwargs: Any) -> Any: ...
    def __iter__(self) -> Iterator[_Row]: ...
    def __aiter__(self) -> AsyncIterator[_Row]: ...
    @overload
    def __getitem__(self, i: int) -> _Row: ...
    @overload
    def __getitem__(self, s: slice) -> Self: ...
    def __reversed__(self) -> Iterator[_Row]: ...

class RawQuerySet(Iterable[_Model], Sized):
    query: RawQuery
    def __init__(
        self,
        raw_query: RawQuery | str,
        model: type[Model] | None = ...,
        query: Query | None = ...,
        params: tuple[Any] = ...,
        translations: dict[str, str] | None = ...,
        using: str = ...,
        hints: dict[str, Model] | None = ...,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_Model]: ...
    def __bool__(self) -> bool: ...
    @overload
    def __getitem__(self, k: int) -> _Model: ...
    @overload
    def __getitem__(self, k: str) -> Any: ...
    @overload
    def __getitem__(self, k: slice) -> RawQuerySet[_Model]: ...
    @cached_property
    def columns(self) -> list[str]: ...
    @property
    def db(self) -> str: ...
    def iterator(self) -> Iterator[_Model]: ...
    @cached_property
    def model_fields(self) -> dict[str, str]: ...
    def prefetch_related(self, *lookups: Any) -> RawQuerySet[_Model]: ...
    def resolve_model_init_order(self) -> tuple[list[str], list[int], list[tuple[str, int]]]: ...
    def using(self, alias: str | None) -> RawQuerySet[_Model]: ...

# Deprecated alias of QuerySet, for compatibility only.
_QuerySet: TypeAlias = QuerySet

class Prefetch:
    prefetch_through: str
    prefetch_to: str
    queryset: QuerySet | None
    to_attr: str | None
    def __init__(self, lookup: str, queryset: QuerySet | None = ..., to_attr: str | None = ...) -> None: ...
    def __getstate__(self) -> dict[str, Any]: ...
    def add_prefix(self, prefix: str) -> None: ...
    def get_current_prefetch_to(self, level: int) -> str: ...
    def get_current_to_attr(self, level: int) -> tuple[str, str]: ...
    def get_current_queryset(self, level: int) -> QuerySet | None: ...
    def get_current_querysets(self, level: int) -> list[QuerySet] | None: ...

def prefetch_related_objects(model_instances: Iterable[_Model], *related_lookups: str | Prefetch) -> None: ...
async def aprefetch_related_objects(model_instances: Iterable[_Model], *related_lookups: str | Prefetch) -> None: ...
def get_prefetcher(instance: Model, through_attr: str, to_attr: str) -> tuple[Any, Any, bool, bool]: ...

class InstanceCheckMeta(type): ...
class EmptyQuerySet(metaclass=InstanceCheckMeta): ...
