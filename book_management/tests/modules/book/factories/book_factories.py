#
# (코드의 전반적인 내용을 설명해 주세요)
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/08 02:37 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


import factory
from faker import Faker

from src.modules.books.domain.aggregate.model import Book

from polyfactory.factories import DataclassFactory

from src.modules.books.domain.value_objects import Isbn


class IsbnFactory(DataclassFactory[Isbn]):
    __model__ = Isbn
    __faker__ = Faker()

    @classmethod
    def value(cls) -> str:
        return cls.__faker__.isbn13()


a = IsbnFactory.build()
isbn_instance = Isbn(value=a.value)


class BookFactoryImpl(DataclassFactory[Book]):
    __model__ = Book

    isbn = isbn_instance


# class BookFactory(factory.Factory):
#
#     class Meta:
#         model = Book
#
#     id = factory.Faker("uuid4", cast_to=None)
#     isbn = factory.Faker("isbn10")
#     title = factory.Faker("sentence")
#     page = factory.Faker("pyint", min_value=1, max_value=10000)
#     revision = factory.Faker("pyint", min_value=1, max_value=100)
#     dt_released_in = factory.Faker("date_object")
