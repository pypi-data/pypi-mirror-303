import dataclasses
import typing as t

import httpx


@dataclasses.dataclass
class MockedResponse:
    status_code: httpx.codes
    response_body: dict[str, t.Any] | None


ResponseBodyMap: t.TypeAlias = t.Optional[
    dict[
        str,  # http method
        dict[
            str,  # url
            MockedResponse,
        ],
    ]
]
RequestHandler: t.TypeAlias = t.Callable[[httpx.Request], httpx.Response]
ClientContextManager: t.TypeAlias = t.Callable[[str, str, RequestHandler], t.ContextManager[None]]
