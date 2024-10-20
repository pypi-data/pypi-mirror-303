from typing import ClassVar
from typing import override
from unittest.async_case import IsolatedAsyncioTestCase

from _support.actions import T_contra
from _support.actions import add_action


class static_setup(add_action[T_contra]):  # noqa:N801
    actions: ClassVar = []

    @classmethod
    def execute_actions(cls) -> None:
        for action in cls.actions:
            action()


class static_teardown(add_action[T_contra]):  # noqa:N801
    actions: ClassVar = []

    @classmethod
    def execute_actions(cls) -> None:
        for action in reversed(cls.actions):
            action()


class BaseTest(IsolatedAsyncioTestCase):
    __test_cases: ClassVar[dict[type[IsolatedAsyncioTestCase], bool]] = {}

    @override
    def __init__(self, methodName: str = 'runTest') -> None:  # noqa: N803
        super().__init__(methodName)
        self.__test_cases[self.__class__] = True

    @override
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        if all(cls.__test_cases.values()):  # all True -> first time
            static_setup.execute_actions()
        cls.__test_cases[cls] = False

    @override
    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        if not any(cls.__test_cases.values()):  # all False -> last time
            static_teardown.execute_actions()
