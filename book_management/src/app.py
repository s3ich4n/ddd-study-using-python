#
# RESTful API 어댑터
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/07 17:44 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import clear_mappers

from src.core.api_config import Settings
from src.core.container import Container
from src.core.fastapi.errors import init_error_handler
from src.core.fastapi.responses import ORJSONResponse

from src.core.fastapi.routes import add_routes
from src.core.fastapi.health_check import router as status_router
# from src.modules.papers.infrastructure.postgres.models import mapper as paper_mapper
# from src.modules.users.infrastructure.postgres.models import mapper as paper_user_mapper
# from src.modules.users.presentation.rest import router as paper_user_router
# from src.modules.users.presentation.rest import register as api_register
# from src.modules.users.presentation.rest import auth as api_auth


container = Container()
container.config.from_pydantic(Settings())
container.wire(
    modules=[
        # api_auth,
        # api_register,
    ],
)

app: FastAPI = FastAPI(
    default_response_class=ORJSONResponse,
    description=container.config.desc.REST_SERVICE_DESCRIPTION(),
    openapi_url=container.config.desc.OPENAPI_URL(),
    title=container.config.desc.REST_SERVICE_NAME(),
    version=container.config.desc.REST_SERVICE_VERSION(),
)

all_routers = [
    status_router,
]
add_routes(all_routers, app)
app.container = container
db = container.db()


# FIXME
#   가변적으로 로드할 수 있게 만들자
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods="*",
    allow_headers="*",
)
init_error_handler(app, 'admin@test.com')


@app.on_event("startup")
async def on_startup():
    await db.connect(echo=True)
    await db.create_database()


@app.on_event("shutdown")
async def on_shutdown():
    clear_mappers()

    await db.disconnect()
