#
# "도서" - 인프라스트럭처 (RDBMS)
#   ORM 코드
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/08 01:53 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


import datetime
from typing import Union

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from src.common.infrastructures.postgres.sqlalchemy import Base


class BookORM(Base):
    __tablename__ = "book"

    id: Union[int, Column] = Column(Integer, primary_key=True)
    isbn: Union[str, Column] = Column(String(15), nullable=False, unique=True)
    title: Union[str, Column] = Column(String(128), nullable=False, unique=True)
    page: Union[int, Column] = Column(Integer, nullable=False, default=1)
    revision: Union[int, Column] = Column(Integer, nullable=False, default=1)
    dt_released_in: Union[datetime.datetime, Column] = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
