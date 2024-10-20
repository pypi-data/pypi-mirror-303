from functools import partial
from typing import ClassVar
from typing import Generic
from typing import Protocol
from typing import TypeVar
from typing import cast

T_contra = TypeVar('T_contra', contravariant=True)


class Consumer(Protocol):
    def __call__(self, t: T_contra) -> None: ...


class Action(Protocol):
    def __call__(self) -> None: ...


class ClassMethodWorkAround(Protocol, Generic[T_contra]):
    def __call__(self, method: type[T_contra], /) -> None: ...
    def __get__(self, instance: None, owner: type[T_contra]) -> Action: ...


class ClassMethod(ClassMethodWorkAround[T_contra]):
    __wrapped__: Consumer


class add_action(Generic[T_contra]):  # noqa:N801
    actions: ClassVar[list[Action]] = []

    def __init__(self, clsmethod: ClassMethodWorkAround[T_contra]) -> None:
        self.clsmethod = cast(ClassMethod[T_contra], clsmethod)

    def __get__(self, instance: None, owner: type[T_contra]) -> Action:
        return self.clsmethod.__get__(instance, owner)

    def __set_name__(self, owner: type[T_contra], _name: str, /) -> None:
        self.actions.append(partial(self.clsmethod.__wrapped__, owner))
