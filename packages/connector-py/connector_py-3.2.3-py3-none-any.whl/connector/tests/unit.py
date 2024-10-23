from abc import ABC, abstractmethod
from contextlib import contextmanager
from types import FunctionType
from typing import Callable, Type
from unittest import IsolatedAsyncioTestCase, TestCase

from pydantic import BaseModel

from connector.async_.abstract import AbstractCommands as AbstractCommandsAsync
from connector.helpers import collect_methods, is_pydantic_model
from connector.sync_.abstract import AbstractCommands as AbstractCommandsSync

_test_docs = """Integration tests are vital to ensure we cover the grounds of the full API.
Define the commands attribute with the commands class to be tested.

Override `discover_data` which fetches the mock response data from the API data folder.
"""
_test_integration_docs = """Tests that the inputs for a command are valid, the response matches the
expected output, and that the response can handle pagination if we detect pagination in the mock
data. The unittest can also be run in live mode where mock data is not used. If pagination is
detected, the test will run the command multiple times to ensure pagination works for the command.
"""


class BaseIntegrationTest(ABC):
    @staticmethod
    def hyphenated(name: str) -> str:
        return "-".join(name.split("_"))

    @abstractmethod
    def discover_data(self, method: Callable):
        """
        Fetch the data from the API data folder. Example implementation:

        ```python
        def discover_data(self, method: callable):
            with open(f"api_data/self.hyphenated({method.__name__}).json") as f:
                return json.load(f)
        ```

        The format of the data should be a list of dictionaries with the following keys
        ```json
        [
            {
                "arguments": {"arg1": "value1", "arg2": "value2"},
                "data": {"key": "value"}
            },
            {
                "arguments": {"arg1": "value1", "arg2": "value2"},
                "data": {"key": "value"}
            },
        ]
        ```

        If the data is paginated in any way, you must provide at least 2 pages of data. This is
        to ensure the integration paginates correctly.
        """
        raise NotImplementedError

    POTENTIAL_PAGE_NAMES = ["page", "cursor", "offset", "limit", "next_cursor", "next_page", "next"]

    def is_paginated(self, data) -> bool:
        """Detect if the data is paginated"""
        if isinstance(data, dict):
            for key in self.POTENTIAL_PAGE_NAMES:
                if key in data:
                    return True
        return False

    @contextmanager
    @abstractmethod
    def mock_method_call(self, method, **kwargs):
        raise NotImplementedError

    def get_args(self, item: dict, method: FunctionType):
        arguments = item.get("arguments")
        response = item.get("data")
        annotations = method.__annotations__

        # Look for the Pydantic model as the args
        for key, value in annotations.items():
            if key == "return":
                continue
            args = [value(**arguments)]
            break
        else:
            args = []
        return arguments, response, args

    def assertion(
        self,
        i: int,
        method: FunctionType,
        data: list,
        response: dict,
        output: BaseModel,
        annotations: dict[str, type],
    ):
        if i == 0:
            assert not (self.is_paginated(response) and len(data) < 2), (
                "Provided data is paginated but only one page is provided. "
                "Please provide at least 2 pages of data."
            )

        if is_pydantic_model(ret := annotations.get("return")):
            if method.__name__ == "info":
                # It's difficult to do a deep comparison of the JSON schemas
                self.assertEqual(output.app_id, response["app_id"])  # type: ignore
                self.assertEqual(output.capabilities, response["capabilities"])  # type: ignore
            else:
                self.assertEqual(output, ret(**response))  # type: ignore
        else:
            self.assertEqual(output, response)  # type: ignore


class SyncIntegrationTest(BaseIntegrationTest, TestCase, ABC):
    sync_commands: Type[AbstractCommandsSync]
    __doc__ = _test_docs

    @classmethod  # type: ignore[misc]
    @property
    def __test__(cls):
        return cls != SyncIntegrationTest

    def setUp(self):
        self.commands = collect_methods(self.sync_commands())

    def test_integration(self):
        for method in self.commands:
            with self.subTest(case=method.__name__):
                data = self.discover_data(method)
                for i, item in enumerate(data):
                    arguments, response, args = self.get_args(item, method)
                    # FIXME For some reason, patching deletes the annotations :skull:
                    annotations = method.__annotations__.copy()
                    with self.mock_method_call(method, args=arguments, data=response):
                        output = method(*args)
                    self.assertion(i, method, data, response, output, annotations)

    test_integration.__doc__ = _test_integration_docs


class AsyncIntegrationTest(BaseIntegrationTest, IsolatedAsyncioTestCase, ABC):
    async_commands: Type[AbstractCommandsAsync]
    __doc__ = _test_docs

    @classmethod  # type: ignore[misc]
    @property
    def __test__(cls):
        return cls != AsyncIntegrationTest

    async def asyncSetUp(self):
        self.commands = collect_methods(self.async_commands())

    async def test_integration(self):
        for method in self.commands:
            with self.subTest(case=method.__name__):
                data = self.discover_data(method)
                for i, item in enumerate(data):
                    arguments, response, args = self.get_args(item, method)
                    annotations = method.__annotations__.copy()
                    with self.mock_method_call(method, args=arguments, data=response):
                        output = await method(*args)
                    self.assertion(i, method, data, response, output, annotations)

    test_integration.__doc__ = _test_integration_docs
