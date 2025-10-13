from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum, auto

from xutility import EasyDumpClass


class NewEnum(Enum):
    e1 = auto()


@dataclass
class Foo(EasyDumpClass):
    i: int
    s: str
    f: float
    de: Decimal
    en: NewEnum
    dt: datetime
    li: list


def test_ldc():
    foo = Foo(
        1,
        "2",
        3.3,
        Decimal("4.5"),
        NewEnum.e1,
        datetime(2024, 8, 1, 10, 8, 0, 100),
        ["l", "i", 0, 1.1],
    )
    assert foo.to_dict() == {
        "i": 1,
        "s": "2",
        "f": 3.3,
        "de": "4.5",
        "en": "e1",
        "dt": "2024-08-01T10:08:00.000100",
        "li": ["l", "i", 0, 1.1],
    }
