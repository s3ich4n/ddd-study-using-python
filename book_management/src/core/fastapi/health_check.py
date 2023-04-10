#
# 루트 디렉토리의 라우터
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/078 15:02 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


from enum import Enum

from dependency_injector.wiring import inject
from fastapi import status
from fastapi.routing import APIRouter
from pydantic import BaseModel, Field

from src.core.api_config import Settings
from src.core.container import Container


router = APIRouter()


class StatusEnum(str, Enum):
    OK = "OK"
    FAILURE = "FAILURE"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"


class HealthCheck(BaseModel):
    title: str = Field(..., description="API title")
    description: str = Field(..., description="Brief description of the API")
    version: str = Field(..., description="API semver version number")
    status: StatusEnum = Field(..., description="API current status")


@router.get(
    "/status",
    response_model=HealthCheck,
    status_code=status.HTTP_200_OK,
    tags=["Health Check"],
    summary="Performs health check",
    description="Performs health check and returns information about running service.",
)
@inject
def health_check():
    container = Container()
    container.config.from_pydantic(Settings())

    return {
        "title": container.config.desc.REST_SERVICE_NAME(),
        "description": container.config.desc.REST_SERVICE_DESCRIPTION(),
        "version": container.config.desc.REST_SERVICE_VERSION(),
        "status": StatusEnum.OK,
    }
