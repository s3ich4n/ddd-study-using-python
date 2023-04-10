#
# Book 객체 - ORM 객체 간 매퍼
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/08 02:49 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#
from dataclasses import asdict

from src.common.infrastructures.postgres.sqlalchemy import mapper_registry
from src.common.protocols.model_mapper import ModelMapper

from src.modules.books.domain.aggregate.model import Book
from src.modules.books.infrastructure.postgres.models.book_orm import BookORM


class BookMapper(ModelMapper[Book, BookORM]):
    @staticmethod
    def map_to_domain_entity(model: BookORM) -> Book:
        return Book(
            id=model.id,
            isbn=model.isbn.value,
            title=model.title,
            page=model.page,
            revision=model.revision,
            dt_released_in=model.dt_released_in,
        )

    @staticmethod
    def map_to_persistence_entity(model: Book) -> BookORM:
        return BookORM(asdict(model))


def start_mapper():
    _book = BookORM.__table__

    mapper_registry.map_imperatively(Book, _book)
