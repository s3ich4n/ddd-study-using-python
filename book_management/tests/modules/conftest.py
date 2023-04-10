import datetime

import pytest

from faker import Faker
from sqlalchemy.orm import clear_mappers

from src.core.container import Container


@pytest.fixture(scope="session", name="db")
async def get_database_session(client):
    db = Container.db()
    await db.connect()
    db.init_session_factory()
    yield db
    clear_mappers()
    await db.disconnect()


today = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)

fake = Faker()
