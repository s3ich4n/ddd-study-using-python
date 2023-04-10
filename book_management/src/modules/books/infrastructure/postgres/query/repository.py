from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.infrastructures.postgres.repository import AsyncPostgresRepository
from src.modules.books.infrastructure.postgres.models.book_orm import BookORM


class BookQueryRepository(AsyncPostgresRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def fetch_by_id(self, id_):
        stmt = select(BookORM).where(BookORM.id == id_)
        result = await self._session.execute(stmt)

        return result.unique().scalars().one_or_none()

    async def fetch_all(self):
        result = await self._session.scalars(select(BookORM))
        return result.fetchall()
