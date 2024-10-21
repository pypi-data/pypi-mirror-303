from collections.abc import Collection, Iterable, Sequence
from typing import TypedDict, Any, ClassVar, Final, TypeVar, overload

from django.core.checks.messages import CheckMessage
from django.core.exceptions import MultipleObjectsReturned as BaseMultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import BaseConstraint, Field, QuerySet
from django.db.models.manager import Manager
from django.db.models.options import Options
from typing_extensions import Required, Unpack, Self
import datetime
from api.models import APIToken, OutboundWebhook
from core.models import ArchiveResult, Snapshot, SnapshotTag, Tag
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.db.models.expressions import Combinable
from uuid import UUID

class PermissionInitKwargs(TypedDict, total=False):
    id: int | str | Combinable

    name: str | int | Combinable

    content_type: ContentType | Combinable

    codename: str | int | Combinable

class GroupInitKwargs(TypedDict, total=False):
    id: int | str | Combinable

    name: str | int | Combinable

class UserInitKwargs(TypedDict, total=False):
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

class ContentTypeInitKwargs(TypedDict, total=False):
    id: int | str | Combinable

    app_label: str | int | Combinable

    model: str | int | Combinable

class SessionInitKwargs(TypedDict, total=False):
    session_key: str | int | Combinable

    session_data: str | Combinable

    expire_date: str | datetime.datetime | datetime.date | Combinable

class LogEntryInitKwargs(TypedDict, total=False):
    id: int | str | Combinable

    action_time: str | datetime.datetime | datetime.date | Combinable

    user: User | Combinable

    content_type: ContentType | Combinable | None

    object_id: str | Combinable | None

    object_repr: str | int | Combinable

    action_flag: float | int | str | Combinable

    change_message: str | Combinable

class TagInitKwargs(TypedDict, total=False):
    created_by: User | Combinable

    created: str | datetime.datetime | datetime.date | Combinable

    modified: str | datetime.datetime | datetime.date | Combinable

    old_id: float | int | str | Combinable

    id: str | UUID

    abid: str | int | Combinable | None
    """ABID-format identifier for this entity (e.g. snp_01BJQMF54D093DXEAWZ6JYRPAQ)"""

    name: str | int | Combinable

    slug: str | int | Combinable

class SnapshotTagInitKwargs(TypedDict, total=False):
    id: int | str | Combinable

    snapshot: Snapshot | Combinable

    tag: Tag | Combinable

class SnapshotInitKwargs(TypedDict, total=False):
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

class ArchiveResultInitKwargs(TypedDict, total=False):
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

class APITokenInitKwargs(TypedDict, total=False):
    modified: str | datetime.datetime | datetime.date | Combinable

    id: str | UUID

    abid: str | int | Combinable | None
    """ABID-format identifier for this entity (e.g. snp_01BJQMF54D093DXEAWZ6JYRPAQ)"""

    created_by: User | Combinable

    created: str | datetime.datetime | datetime.date | Combinable

    token: str | int | Combinable

    expires: str | datetime.datetime | datetime.date | Combinable | None

class OutboundWebhookInitKwargs(TypedDict, total=False):
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

class PermissionInitKwargs(TypedDict, total=False):
    id: int | str | Combinable

    name: str | int | Combinable

    content_type: ContentType | Combinable

    codename: str | int | Combinable

class GroupInitKwargs(TypedDict, total=False):
    id: int | str | Combinable

    name: str | int | Combinable

class UserInitKwargs(TypedDict, total=False):
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

class ContentTypeInitKwargs(TypedDict, total=False):
    id: int | str | Combinable

    app_label: str | int | Combinable

    model: str | int | Combinable

class SessionInitKwargs(TypedDict, total=False):
    session_key: str | int | Combinable

    session_data: str | Combinable

    expire_date: str | datetime.datetime | datetime.date | Combinable

class LogEntryInitKwargs(TypedDict, total=False):
    id: int | str | Combinable

    action_time: str | datetime.datetime | datetime.date | Combinable

    user: User | Combinable

    content_type: ContentType | Combinable | None

    object_id: str | Combinable | None

    object_repr: str | int | Combinable

    action_flag: float | int | str | Combinable

    change_message: str | Combinable

class TagInitKwargs(TypedDict, total=False):
    created_by: User | Combinable

    created: str | datetime.datetime | datetime.date | Combinable

    modified: str | datetime.datetime | datetime.date | Combinable

    old_id: float | int | str | Combinable

    id: str | UUID

    abid: str | int | Combinable | None
    """ABID-format identifier for this entity (e.g. snp_01BJQMF54D093DXEAWZ6JYRPAQ)"""

    name: str | int | Combinable

    slug: str | int | Combinable

class SnapshotTagInitKwargs(TypedDict, total=False):
    id: int | str | Combinable

    snapshot: Snapshot | Combinable

    tag: Tag | Combinable

class SnapshotInitKwargs(TypedDict, total=False):
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

class ArchiveResultInitKwargs(TypedDict, total=False):
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

class APITokenInitKwargs(TypedDict, total=False):
    modified: str | datetime.datetime | datetime.date | Combinable

    id: str | UUID

    abid: str | int | Combinable | None
    """ABID-format identifier for this entity (e.g. snp_01BJQMF54D093DXEAWZ6JYRPAQ)"""

    created_by: User | Combinable

    created: str | datetime.datetime | datetime.date | Combinable

    token: str | int | Combinable

    expires: str | datetime.datetime | datetime.date | Combinable | None

class OutboundWebhookInitKwargs(TypedDict, total=False):
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

_Self = TypeVar("_Self", bound=Model)

class ModelStateFieldsCacheDescriptor:
    @overload
    def __get__(self, inst: None, owner: object) -> Self: ...
    @overload
    def __get__(self, inst: object, owner: object) -> dict[Any, Any]: ...

class ModelState:
    db: str | None
    adding: bool
    fields_cache: ModelStateFieldsCacheDescriptor

class ModelBase(type):
    @property
    def _default_manager(cls: type[_Self]) -> Manager[_Self]: ...  # type: ignore[misc]
    @property
    def _base_manager(cls: type[_Self]) -> Manager[_Self]: ...  # type: ignore[misc]

class Model(metaclass=ModelBase):
    # Note: these two metaclass generated attributes don't really exist on the 'Model'
    # class, runtime they are only added on concrete subclasses of 'Model'. The
    # metaclass also sets up correct inheritance from concrete parent models exceptions.
    # Our mypy plugin aligns with this behaviour and will remove the 2 attributes below
    # and re-add them to correct concrete subclasses of 'Model'
    DoesNotExist: Final[type[ObjectDoesNotExist]]
    MultipleObjectsReturned: Final[type[BaseMultipleObjectsReturned]]
    # This 'objects' attribute will be deleted, via the plugin, in favor of managing it
    # to only exist on subclasses it exists on during runtime.
    objects: ClassVar[Manager[Self]]

    _meta: ClassVar[Options[Self]]
    pk: Any
    _state: ModelState
    @overload
    def __init__(self: Permission, **kwargs: Unpack[PermissionInitKwargs]) -> None: ...
    @overload
    def __init__(self: Group, **kwargs: Unpack[GroupInitKwargs]) -> None: ...
    @overload
    def __init__(self: User, **kwargs: Unpack[UserInitKwargs]) -> None: ...
    @overload
    def __init__(self: ContentType, **kwargs: Unpack[ContentTypeInitKwargs]) -> None: ...
    @overload
    def __init__(self: Session, **kwargs: Unpack[SessionInitKwargs]) -> None: ...
    @overload
    def __init__(self: LogEntry, **kwargs: Unpack[LogEntryInitKwargs]) -> None: ...
    @overload
    def __init__(self: Tag, **kwargs: Unpack[TagInitKwargs]) -> None: ...
    @overload
    def __init__(self: SnapshotTag, **kwargs: Unpack[SnapshotTagInitKwargs]) -> None: ...
    @overload
    def __init__(self: Snapshot, **kwargs: Unpack[SnapshotInitKwargs]) -> None: ...
    @overload
    def __init__(self: ArchiveResult, **kwargs: Unpack[ArchiveResultInitKwargs]) -> None: ...
    @overload
    def __init__(self: APIToken, **kwargs: Unpack[APITokenInitKwargs]) -> None: ...
    @overload
    def __init__(self: OutboundWebhook, **kwargs: Unpack[OutboundWebhookInitKwargs]) -> None: ...
    @classmethod
    def add_to_class(cls, name: str, value: Any) -> Any: ...
    @classmethod
    def from_db(cls, db: str | None, field_names: Collection[str], values: Collection[Any]) -> Self: ...
    def _do_update(
        self,
        base_qs: QuerySet[Self],
        using: str | None,
        pk_val: Any,
        values: Collection[tuple[Field, type[Model] | None, Any]],
        update_fields: Iterable[str] | None,
        forced_update: bool,
    ) -> bool: ...
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]: ...
    async def adelete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]: ...
    def full_clean(
        self, exclude: Iterable[str] | None = ..., validate_unique: bool = ..., validate_constraints: bool = ...
    ) -> None: ...
    def clean(self) -> None: ...
    def clean_fields(self, exclude: Collection[str] | None = ...) -> None: ...
    def validate_unique(self, exclude: Collection[str] | None = ...) -> None: ...
    def date_error_message(self, lookup_type: str, field_name: str, unique_for: str) -> ValidationError: ...
    def unique_error_message(self, model_class: type[Self], unique_check: Sequence[str]) -> ValidationError: ...
    def validate_constraints(self, exclude: Collection[str] | None = ...) -> None: ...
    def get_constraints(self) -> list[tuple[type[Model], Sequence[BaseConstraint]]]: ...
    def save(
        self,
        force_insert: bool | tuple[ModelBase, ...] = ...,
        force_update: bool = ...,
        using: str | None = ...,
        update_fields: Iterable[str] | None = ...,
    ) -> None: ...
    async def asave(
        self,
        force_insert: bool | tuple[ModelBase, ...] = ...,
        force_update: bool = ...,
        using: str | None = ...,
        update_fields: Iterable[str] | None = ...,
    ) -> None: ...
    def save_base(
        self,
        raw: bool = ...,
        force_insert: bool | tuple[ModelBase, ...] = ...,
        force_update: bool = ...,
        using: str | None = ...,
        update_fields: Iterable[str] | None = ...,
    ) -> None: ...
    def refresh_from_db(self, using: str | None = ..., fields: Iterable[str] | None = ...) -> None: ...
    async def arefresh_from_db(self, using: str | None = ..., fields: Iterable[str] | None = ...) -> None: ...
    def serializable_value(self, field_name: str) -> Any: ...
    def prepare_database_save(self, field: Field) -> Any: ...
    def get_deferred_fields(self) -> set[str]: ...
    @classmethod
    def check(cls, **kwargs: Any) -> list[CheckMessage]: ...
    def __getstate__(self) -> dict: ...
    def _get_pk_val(self, meta: Options[Self] | None = None) -> str: ...

def model_unpickle(model_id: tuple[str, str] | type[Model]) -> Model: ...
