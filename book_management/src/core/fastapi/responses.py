#
# ORJSON을 통한 JSONResponse 구현
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/079 15:23 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


from starlette.responses import JSONResponse
from sqlalchemy.ext.associationproxy import _AssociationList
from typing import Any

try:
    import orjson
except ImportError:  # pragma: nocover
    orjson = None  # type: ignore


def default(obj):
    if isinstance(obj, _AssociationList):
        return list(obj)
    raise TypeError


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed to use ORJSONResponse"
        return orjson.dumps(content, default=default)
