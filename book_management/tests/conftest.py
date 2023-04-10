#
# 프로젝트 전체에 널리 사용되는 conftest
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/07 12:45 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


import asyncio
from typing import Generator

import pytest

from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from sqlalchemy.orm import clear_mappers

from src.app import app


#
# FYI
#   https://pytest-asyncio.readthedocs.io/en/latest/reference/fixtures.html#fixtures
#
@pytest.fixture(scope="session")
@pytest.mark.asyncio
def event_loop(request) -> Generator:  # noqa: indirect usage
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    clear_mappers()
    loop.close()


@pytest.fixture(scope="session", name="client")
async def test_client() -> AsyncClient:
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url='http://localhost:13370/',
        ) as client:
            yield client
