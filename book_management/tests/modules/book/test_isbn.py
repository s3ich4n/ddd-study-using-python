#
# ISBN 자체코드 테스트
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/03/25 23:21 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


import pytest


from src.modules.book.isbn import Isbn


@pytest.mark.unit
class TestIsbn:
    def test_isbn_10(self):
        assert Isbn(value="9780132350884").value == "9780132350884"

    def test_isbn_13(self):
        assert Isbn(value="978-0132350884").value == "978-0132350884"
