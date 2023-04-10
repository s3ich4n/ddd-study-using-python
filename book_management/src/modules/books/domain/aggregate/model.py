import datetime

from pydantic import PositiveInt, Field
from pydantic.dataclasses import dataclass

from src.core.pydantic.immutables import Config
from src.modules.books.domain.value_objects import Isbn


@dataclass(config=Config, frozen=True)
class Book:
    id: PositiveInt
    isbn: Isbn
    page: PositiveInt
    revision: PositiveInt
    dt_released_in: datetime.date
    title: str = Field(..., min_length=1, max_length=128)
