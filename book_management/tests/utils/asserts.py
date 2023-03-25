#
# pytest의 에러 캐치 후 로그 작성
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/03/25 23:41 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


def assert_validation_error(len_, loc, type_, excinfo):
    def write_message(expected, gotten):
        return f"expected: '{expected}', got: '{gotten}'"

    errors = excinfo.value.errors()
    assert len(errors) == len_, write_message(len_, len(errors))

    error, *_ = errors
    assert error["loc"] == (loc,), write_message(loc, error.get("loc", None))
    assert error["type"] == type_, write_message(type_, error.get("type", None))
