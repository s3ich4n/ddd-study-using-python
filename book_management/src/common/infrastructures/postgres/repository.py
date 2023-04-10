#
# PostgreSQL Repository 에 기본적으로 사용되는 클래스
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/08 01:29 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


from typing import Any, Protocol


class AsyncPostgresRepository(Protocol):

    async def fetch_by_id(
            self,
            id_,
    ):
        ...

    async def persist(
            self,
            data: Any,
    ):
        ...
