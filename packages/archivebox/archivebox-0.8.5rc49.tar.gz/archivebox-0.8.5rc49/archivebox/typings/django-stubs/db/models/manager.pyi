import datetime
from collections.abc import AsyncIterator, Callable, Collection, Iterable, Iterator, Mapping, Sequence
from typing import TypedDict, Any, Generic, NoReturn, TypeVar, overload

from django.db.models.base import Model
from django.db.models.expressions import Combinable, OrderBy
from django.db.models.query import QuerySet, RawQuerySet
from typing_extensions import Required, Unpack, Self
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

_T = TypeVar("_T", bound=Model, covariant=True)

class BaseManager(Generic[_T]):
    cache: Callable[[], Self]  # django-cacheops
    creation_counter: int
    auto_created: bool
    use_in_migrations: bool
    name: str
    model: type[_T]
    _db: str | None
    def __new__(cls, *args: Any, **kwargs: Any) -> Self: ...
    def __init__(self) -> None: ...
    def __class_getitem__(cls, *args: Any, **kwargs: Any) -> type[Self]: ...
    def deconstruct(
        self,
    ) -> tuple[bool, str | None, str | None, Sequence[Any] | None, dict[str, Any] | None]: ...
    def check(self, **kwargs: Any) -> list[Any]: ...
    @classmethod
    def from_queryset(cls, queryset_class: type[QuerySet[_T]], class_name: str | None = ...) -> type[Self]: ...
    @classmethod
    def _get_queryset_methods(cls, queryset_class: type) -> dict[str, Any]: ...
    def contribute_to_class(self, cls: type[Model], name: str) -> None: ...
    def db_manager(self, using: str | None = ..., hints: dict[str, Model] | None = ...) -> Self: ...
    @property
    def db(self) -> str: ...
    def get_queryset(self) -> QuerySet[_T]: ...
    # NOTE: The following methods are in common with QuerySet, but note that the use of QuerySet as a return type
    # rather than a self-type (_QS), since Manager's QuerySet-like methods return QuerySets and not Managers.
    def iterator(self, chunk_size: int | None = ...) -> Iterator[_T]: ...
    def aiterator(self, chunk_size: int = ...) -> AsyncIterator[_T]: ...
    def aggregate(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...
    async def aaggregate(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...
    def get(self, *args: Any, **kwargs: Any) -> _T: ...
    async def aget(self, *args: Any, **kwargs: Any) -> _T: ...
    @overload
    def create(self: BaseManager[Permission], **kwargs: Unpack[PermissionCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[Group], **kwargs: Unpack[GroupCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[User], **kwargs: Unpack[UserCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[ContentType], **kwargs: Unpack[ContentTypeCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[Session], **kwargs: Unpack[SessionCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[LogEntry], **kwargs: Unpack[LogEntryCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[Tag], **kwargs: Unpack[TagCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[SnapshotTag], **kwargs: Unpack[SnapshotTagCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[Snapshot], **kwargs: Unpack[SnapshotCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[ArchiveResult], **kwargs: Unpack[ArchiveResultCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[APIToken], **kwargs: Unpack[APITokenCreateKwargs]) -> _T: ...
    @overload
    def create(self: BaseManager[OutboundWebhook], **kwargs: Unpack[OutboundWebhookCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[Permission], **kwargs: Unpack[PermissionCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[Group], **kwargs: Unpack[GroupCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[User], **kwargs: Unpack[UserCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[ContentType], **kwargs: Unpack[ContentTypeCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[Session], **kwargs: Unpack[SessionCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[LogEntry], **kwargs: Unpack[LogEntryCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[Tag], **kwargs: Unpack[TagCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[SnapshotTag], **kwargs: Unpack[SnapshotTagCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[Snapshot], **kwargs: Unpack[SnapshotCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[ArchiveResult], **kwargs: Unpack[ArchiveResultCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[APIToken], **kwargs: Unpack[APITokenCreateKwargs]) -> _T: ...
    @overload
    async def acreate(self: BaseManager[OutboundWebhook], **kwargs: Unpack[OutboundWebhookCreateKwargs]) -> _T: ...
    def bulk_create(
        self,
        objs: Iterable[_T],
        batch_size: int | None = ...,
        ignore_conflicts: bool = ...,
        update_conflicts: bool = ...,
        update_fields: Collection[str] | None = ...,
        unique_fields: Collection[str] | None = ...,
    ) -> list[_T]: ...
    async def abulk_create(
        self,
        objs: Iterable[_T],
        batch_size: int | None = ...,
        ignore_conflicts: bool = ...,
        update_conflicts: bool = ...,
        update_fields: Collection[str] | None = ...,
        unique_fields: Collection[str] | None = ...,
    ) -> list[_T]: ...
    def bulk_update(self, objs: Iterable[_T], fields: Sequence[str], batch_size: int | None = ...) -> int: ...
    async def abulk_update(self, objs: Iterable[_T], fields: Sequence[str], batch_size: int | None = ...) -> int: ...
    def get_or_create(self, defaults: Mapping[str, Any] | None = ..., **kwargs: Any) -> tuple[_T, bool]: ...
    async def aget_or_create(self, defaults: Mapping[str, Any] | None = ..., **kwargs: Any) -> tuple[_T, bool]: ...
    def update_or_create(
        self,
        defaults: Mapping[str, Any] | None = ...,
        create_defaults: Mapping[str, Any] | None = ...,
        **kwargs: Any,
    ) -> tuple[_T, bool]: ...
    async def aupdate_or_create(
        self,
        defaults: Mapping[str, Any] | None = ...,
        create_defaults: Mapping[str, Any] | None = ...,
        **kwargs: Any,
    ) -> tuple[_T, bool]: ...
    def earliest(self, *fields: str | OrderBy) -> _T: ...
    async def aearliest(self, *fields: str | OrderBy) -> _T: ...
    def latest(self, *fields: str | OrderBy) -> _T: ...
    async def alatest(self, *fields: str | OrderBy) -> _T: ...
    def first(self) -> _T | None: ...
    async def afirst(self) -> _T | None: ...
    def last(self) -> _T | None: ...
    async def alast(self) -> _T | None: ...
    def in_bulk(self, id_list: Iterable[Any] | None = ..., *, field_name: str = ...) -> dict[Any, _T]: ...
    async def ain_bulk(self, id_list: Iterable[Any] | None = ..., *, field_name: str = ...) -> dict[Any, _T]: ...
    def update(self, **kwargs: Any) -> int: ...
    async def aupdate(self, **kwargs: Any) -> int: ...
    def exists(self) -> bool: ...
    async def aexists(self) -> bool: ...
    def explain(self, *, format: Any | None = ..., **options: Any) -> str: ...
    async def aexplain(self, *, format: Any | None = ..., **options: Any) -> str: ...
    def contains(self, objs: Model) -> bool: ...
    async def acontains(self, objs: Model) -> bool: ...
    def raw(
        self,
        raw_query: str,
        params: Any = ...,
        translations: dict[str, str] | None = ...,
        using: str | None = ...,
    ) -> RawQuerySet: ...
    # The type of values may be overridden to be more specific in the mypy plugin, depending on the fields param
    def values(self, *fields: str | Combinable, **expressions: Any) -> QuerySet[_T, dict[str, Any]]: ...
    # The type of values_list may be overridden to be more specific in the mypy plugin, depending on the fields param
    def values_list(self, *fields: str | Combinable, flat: bool = ..., named: bool = ...) -> QuerySet[_T, Any]: ...
    def dates(self, field_name: str, kind: str, order: str = ...) -> QuerySet[_T, datetime.date]: ...
    def datetimes(
        self, field_name: str, kind: str, order: str = ..., tzinfo: datetime.tzinfo | None = ...
    ) -> QuerySet[_T, datetime.datetime]: ...
    def none(self) -> QuerySet[_T]: ...
    def all(self) -> QuerySet[_T]: ...
    def filter(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def exclude(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def complex_filter(self, filter_obj: Any) -> QuerySet[_T]: ...
    def count(self) -> int: ...
    async def acount(self) -> int: ...
    def union(self, *other_qs: Any, all: bool = ...) -> QuerySet[_T]: ...
    def intersection(self, *other_qs: Any) -> QuerySet[_T]: ...
    def difference(self, *other_qs: Any) -> QuerySet[_T]: ...
    def select_for_update(
        self, nowait: bool = ..., skip_locked: bool = ..., of: Sequence[str] = ..., no_key: bool = ...
    ) -> QuerySet[_T]: ...
    def select_related(self, *fields: Any) -> QuerySet[_T]: ...
    def prefetch_related(self, *lookups: Any) -> QuerySet[_T]: ...
    def annotate(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def alias(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def order_by(self, *field_names: Any) -> QuerySet[_T]: ...
    def distinct(self, *field_names: Any) -> QuerySet[_T]: ...
    # extra() return type won't be supported any time soon
    def extra(
        self,
        select: dict[str, Any] | None = ...,
        where: list[str] | None = ...,
        params: list[Any] | None = ...,
        tables: list[str] | None = ...,
        order_by: Sequence[str] | None = ...,
        select_params: Sequence[Any] | None = ...,
    ) -> QuerySet[Any]: ...
    def reverse(self) -> QuerySet[_T]: ...
    def defer(self, *fields: Any) -> QuerySet[_T]: ...
    def only(self, *fields: Any) -> QuerySet[_T]: ...
    def using(self, alias: str | None) -> QuerySet[_T]: ...
    @property
    def ordered(self) -> bool: ...

class Manager(BaseManager[_T]): ...

class ManagerDescriptor:
    manager: BaseManager
    def __init__(self, manager: BaseManager) -> None: ...
    @overload
    def __get__(self, instance: None, cls: type[Model] | None = ...) -> BaseManager: ...
    @overload
    def __get__(self, instance: Model, cls: type[Model] | None = ...) -> NoReturn: ...

class EmptyManager(Manager[_T]):
    def __init__(self, model: type[_T]) -> None: ...
