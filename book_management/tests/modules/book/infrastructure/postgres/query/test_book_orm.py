#
# "도서" 인프라 스트럭처 - Postgres Query 테스트
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/08 02:43 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


import pytest
import pytest_factoryboy
from sqlalchemy import select


from src.modules.books.infrastructure.postgres.models.book_orm import BookORM
from src.modules.books.infrastructure.postgres.models.mapper import BookMapper
from src.modules.books.infrastructure.postgres.query.repository import BookQueryRepository

from tests.modules.book.factories.book_factories import (
    # BookFactory,
    BookFactoryImpl,
)

# FACTORIES = [
#     BookFactory,
# ]
#
# for factory in FACTORIES:
#     pytest_factoryboy.register(factory)


# @pytest.fixture(name="book")
# def book_fixture(book_factory):
#     return book_factory()


@pytest.fixture(name="book")
def book_fixture():
    yield BookFactoryImpl.build()


@pytest.mark.integration
class TestBookQuery:
    async def test_query_books(
            self,
            db,
            book,
    ):
        # Arrange
        async with db.session() as session:
            repo = BookQueryRepository(session)

            # Act
            await repo.fetch_all()

            stmt = select(BookORM)
            rows = await session.scalars(stmt)

        assert BookMapper.map_to_domain_entity(rows.fetchall()) == book

    async def test_query_book_by_id(
            self,
            db,
            book,
    ):
        # Arrange
        async with db.session() as session:
            repo = BookQueryRepository(session)

            # Act
            await repo.fetch_by_id(id_=book.id)

            stmt = select(BookORM)
            rows = await session.scalars(stmt)

        assert BookMapper.map_to_domain_entity(rows.first()) == book
