#
# "도서" 도메인의 기본에 대한 테스트코드
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/03/25 22:54 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


import datetime

from functools import partial
from typing import Any, Dict

import pytest

from pydantic import ValidationError

from tests.utils.asserts import assert_validation_error
from src.modules.book.entities import Book
from src.modules.book.isbn import Isbn

DataType = Dict[str, Any]


@pytest.fixture(name="valid_book_data")
def valid_admin_user_fixture() -> DataType:
    return {
        "id": 1,
        "isbn": Isbn(value="978-0132350884"),
        "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "page": 464,
        "revision": 1,
        "dt_released_in": datetime.date(2008, 8, 1),
    }


@pytest.fixture(name="invalid_book_data")
def invalid_admin_user_fixture() -> DataType:
    return {
        "id": -1,
        "isbn": "abccdd",
        "title": "a" * 500,
        "page": -1,
        "revision": -1,
        "dt_released_in": None,
    }


@pytest.mark.unit
class TestBook:
    class TestBookModel:
        def test_validation(self, valid_book_data):
            assert Book(**valid_book_data)

        def test_invalidation(self, invalid_book_data):
            with pytest.raises(ValidationError):
                Book(**invalid_book_data)

        def test_immutability(self, valid_book_data):
            data = Book(**valid_book_data)
            for key in data.dict().keys():
                with pytest.raises(TypeError):
                    setattr(data, key, "ERROR VALUE")

    class TestBookId:
        assert_validation_error = partial(assert_validation_error, 1, "id")

        def test_id_should_be_number_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.update({"id": "invalid value"})
                Book(**valid_book_data)

            self.assert_validation_error("type_error.integer", excinfo)

        def test_id_should_be_positive_value_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.update({"id": -1})
                Book(**valid_book_data)

            self.assert_validation_error("value_error.number.not_ge", excinfo)

        def test_id_is_required_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.pop("id")
                Book(**valid_book_data)

            self.assert_validation_error("value_error.missing", excinfo)

    class TestBookTitle:
        """

        TODO: 다국어 지원

        """
        assert_validation_error = partial(assert_validation_error, 1, "title")

        def test_book_title_should_be_string_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.update({"title": None})
                Book(**valid_book_data)

            self.assert_validation_error("type_error.none.not_allowed", excinfo)

        def test_book_title_length_is_greater_than_1(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.update({"title": "a" * 0})
                Book(**valid_book_data)

            self.assert_validation_error("value_error.any_str.min_length", excinfo)

        def test_book_title_length_is_less_than_128(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.update({"title": "a" * 129})
                Book(**valid_book_data)

            self.assert_validation_error("value_error.any_str.max_length", excinfo)

        def test_book_title_is_required_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.pop("title")
                Book(**valid_book_data)

            self.assert_validation_error("value_error.missing", excinfo)

    class TestBookPage:
        assert_validation_error = partial(assert_validation_error, 1, "page")

        def test_book_page_should_be_number_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.update({"page": "invalid value"})
                Book(**valid_book_data)

            self.assert_validation_error("type_error.integer", excinfo)

        def test_book_page_should_be_positive_value_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.update({"page": -1})
                Book(**valid_book_data)

            self.assert_validation_error("value_error.number.not_gt", excinfo)

        def test_book_page_is_required_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.pop("page")
                Book(**valid_book_data)

            self.assert_validation_error("value_error.missing", excinfo)

    class TestBookRevision:
        assert_validation_error = partial(assert_validation_error, 1, "revision")

        def test_book_revision_should_be_number_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.update({"revision": "invalid value"})
                Book(**valid_book_data)

            self.assert_validation_error("type_error.integer", excinfo)

        def test_book_revision_should_be_positive_value_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.update({"revision": -1})
                Book(**valid_book_data)

            self.assert_validation_error("value_error.number.not_ge", excinfo)

        def test_book_revision_is_required_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.pop("revision")
                Book(**valid_book_data)

            self.assert_validation_error("value_error.missing", excinfo)

    class TestBookDTReleasedIn:
        assert_validation_error = partial(assert_validation_error, 1, "dt_released_in")

        def test_book_datetime_released_in_should_be_datetime_object_when_initialized(
                self,
                valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.update({"dt_released_in": "invalid value"})
                Book(**valid_book_data)

            self.assert_validation_error("value_error.date", excinfo)

        def test_book_datetime_is_required_when_initialized(
            self,
            valid_book_data,
        ):
            with pytest.raises(ValidationError) as excinfo:
                valid_book_data.pop("dt_released_in")
                Book(**valid_book_data)

            self.assert_validation_error("value_error.missing", excinfo)
