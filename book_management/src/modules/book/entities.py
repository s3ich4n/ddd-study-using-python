#
# "책" 엔티티
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/03/25 22:59 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


import datetime

from pydantic import BaseModel, Field

from src.modules.book.isbn import Isbn


class Book(BaseModel):
    """ "책"에 대한 엔티티 모음

    """
    id: int = Field(ge=1)
    isbn: Isbn
    title: str = Field(min_length=1, max_length=128)
    page: int = Field(gt=0)
    revision: int = Field(ge=1)
    dt_released_in: datetime.date

    class Config:
        allow_mutation = False
        orm_mode = True
