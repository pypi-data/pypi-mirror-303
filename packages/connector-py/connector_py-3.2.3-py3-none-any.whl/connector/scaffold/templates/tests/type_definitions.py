import dataclasses
import typing as t

import httpx


@dataclasses.dataclass
class MockedResponse:
    status_code: httpx.codes
    response_body: dict[str, t.Any] | None


ResponseBodyMap: t.TypeAlias = dict[
    str,  # http method
    dict[
        str,  # url
        MockedResponse,
    ],
]
ClientContextManager: t.TypeAlias = t.Callable[[str, ResponseBodyMap], t.ContextManager[None]]
