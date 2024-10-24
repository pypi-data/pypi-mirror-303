from __future__ import annotations

from typing import Any, Callable, TypedDict

from httpx import URL, Limits
from httpx._types import (
    AuthTypes,
    CertTypes,
    CookieTypes,
    HeaderTypes,
    ProxiesTypes,
    ProxyTypes,
    QueryParamTypes,
    TimeoutTypes,
    VerifyTypes,
)
from typing_extensions import NotRequired


class HTTPXPayload(TypedDict):
    auth: NotRequired[AuthTypes | None]
    params: NotRequired[QueryParamTypes | None]
    headers: NotRequired[HeaderTypes | None]
    cookies: NotRequired[CookieTypes | None]
    verify: NotRequired[VerifyTypes]
    cert: NotRequired[CertTypes | None]
    http1: NotRequired[bool]
    http2: NotRequired[bool]
    proxy: NotRequired[ProxyTypes | None]
    proxies: NotRequired[ProxiesTypes | None]
    timeout: NotRequired[TimeoutTypes]
    follow_redirects: NotRequired[bool]
    limits: NotRequired[Limits]
    max_redirects: NotRequired[int]
    base_url: NotRequired[URL | str]
    app: NotRequired[Callable[..., Any] | None]
    trust_env: NotRequired[bool]
    default_encoding: NotRequired[str | Callable[[bytes], str]]
