from typing import TYPE_CHECKING
from typing import Protocol

if TYPE_CHECKING:
    from collections.abc import Sequence
    from datetime import date
    from decimal import Decimal


class ColumnHeader(Protocol):
    name: str


class Column(Protocol):
    header: ColumnHeader
    howmuch: 'Decimal | None'


class Info(Protocol):
    when: 'date'
    columns: 'Sequence[Column]'

    def howmuch(self, column_header: ColumnHeader) -> 'Decimal | None': ...
