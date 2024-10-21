from collections.abc import Callable, Sequence
from typing import Protocol, TypedDict, overload, Any, Literal

from django.http.response import HttpResponse
from django.urls.resolvers import ResolverMatch
from typing_extensions import NotRequired

class EmptyDict(TypedDict):
    pass

class SupportsStr(Protocol):
    def __str__(self) -> str:
        ...

class _6A7DA8Kwargs(TypedDict):
    abid: SupportsStr

class _EBDF36Kwargs(TypedDict):
    tag_id: SupportsStr

class _FDAA00Kwargs(TypedDict):
    snapshot_id: SupportsStr

class _D8E25EKwargs(TypedDict):
    archiveresult_id: SupportsStr

class _DA39A3Kwargs(TypedDict):
    pass

class _D120B5Kwargs(TypedDict):
    app_label: SupportsStr

class _F3C29BKwargs(TypedDict):
    object_id: SupportsStr

class _8E988FKwargs(TypedDict):
    content_type_id: SupportsStr

    object_id: SupportsStr

class _BA2AC4Kwargs(TypedDict):
    key: SupportsStr

class _D109D1Kwargs(TypedDict):
    uidb64: SupportsStr

    token: SupportsStr

class _2C4C13Kwargs(TypedDict):
    path: SupportsStr

def resolve(path: str, urlconf: str | None = ...) -> ResolverMatch: ...
@overload
def reverse(
    viewname: Literal["Home", "healthcheck", "api-1:api-root", "api-1:cli_remove", "api-1:cli_list", "api-1:cli_schedule", "api-1:cli_update", "api-1:cli_add", "api-1:get_tags", "api-1:get_snapshots", "api-1:check_api_token", "api-1:get_api_token", "api-1:openapi-view", "api-1:openapi-json", "admin:core_archiveresult_add", "admin:core_archiveresult_changelist", "admin:core_tag_add", "admin:core_tag_changelist", "admin:core_snapshot_add", "admin:core_snapshot_changelist", "admin:grid", "admin:api_outboundwebhook_add", "admin:api_outboundwebhook_changelist", "admin:api_apitoken_add", "admin:api_apitoken_changelist", "admin:auth_user_add", "admin:auth_user_changelist", "admin:jsi18n", "admin:autocomplete", "admin:password_change_done", "admin:password_change", "admin:logout", "admin:login", "admin:index", "admin:Add", "admin:Plugins", "admin:Binaries", "admin:Configuration", "admin:admin-data-download", "admin:admin-data-index-view", "password_reset_complete", "password_reset_done", "password_reset", "password_change_done", "password_change", "logout", "login", "add", "Docs", "public-index"],
    urlconf: str | None = ...,
    args: tuple[()] | None = ...,
    kwargs: EmptyDict | None = ...,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Literal["api-1:get_any"],
    urlconf: str | None = ...,
    *, args: Literal[None] = ...,
    kwargs: _6A7DA8Kwargs,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Literal["api-1:get_tag"],
    urlconf: str | None = ...,
    *, args: Literal[None] = ...,
    kwargs: _EBDF36Kwargs,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Literal["api-1:get_snapshot"],
    urlconf: str | None = ...,
    *, args: Literal[None] = ...,
    kwargs: _FDAA00Kwargs,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Literal["api-1:get_archiveresult"],
    urlconf: str | None = ...,
    *, args: Literal[None] = ...,
    kwargs: _D8E25EKwargs | EmptyDict | None,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Literal["admin:app_list"],
    urlconf: str | None = ...,
    *, args: Literal[None] = ...,
    kwargs: _D120B5Kwargs,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Literal["admin:core_archiveresult_change", "admin:core_archiveresult_delete", "admin:core_archiveresult_history", "admin:core_tag_change", "admin:core_tag_delete", "admin:core_tag_history", "admin:core_snapshot_change", "admin:core_snapshot_delete", "admin:core_snapshot_history", "admin:api_outboundwebhook_change", "admin:api_outboundwebhook_delete", "admin:api_outboundwebhook_history", "admin:api_apitoken_change", "admin:api_apitoken_delete", "admin:api_apitoken_history", "admin:auth_user_change", "admin:auth_user_delete", "admin:auth_user_history"],
    urlconf: str | None = ...,
    *, args: Literal[None] = ...,
    kwargs: _F3C29BKwargs,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Literal["admin:view_on_site"],
    urlconf: str | None = ...,
    *, args: Literal[None] = ...,
    kwargs: _8E988FKwargs,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Literal["admin:plugin", "admin:binary", "admin:config_val"],
    urlconf: str | None = ...,
    *, args: Literal[None] = ...,
    kwargs: _BA2AC4Kwargs,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Literal["password_reset_confirm"],
    urlconf: str | None = ...,
    *, args: Literal[None] = ...,
    kwargs: _D109D1Kwargs,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Literal["Snapshot"],
    urlconf: str | None = ...,
    *, args: Literal[None] = ...,
    kwargs: _2C4C13Kwargs,
    current_app: Literal[None] = ...,
) -> str: ...
@overload
def reverse(
    viewname: Callable[..., Any] | None,
    urlconf: str | None = ...,
    args: Sequence[Any] | None = ...,
    kwargs: dict[str, Any] | None = ...,
    current_app: str | None = ...,
) -> str: ...

reverse_lazy: Any

def clear_url_caches() -> None: ...
def set_script_prefix(prefix: str) -> None: ...
def get_script_prefix() -> str: ...
def clear_script_prefix() -> None: ...
def set_urlconf(urlconf_name: str | None) -> None: ...
def get_urlconf(default: str | None = ...) -> str | None: ...
def is_valid_path(path: str, urlconf: str | None = ...) -> Literal[False] | ResolverMatch: ...
def translate_url(url: str, lang_code: str) -> str: ...
