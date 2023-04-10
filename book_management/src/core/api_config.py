#
# FastAPI의 컨픽 관련 설정을 모아놓음
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/078 18:29 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


from pydantic import BaseSettings, Field, PostgresDsn


class ServerDescriptionSettings(BaseSettings):
    API_STR: str = "/v1"

    OPENAPI_URL: str = f"/{API_STR}/openapi.json"

    REST_SERVICE_NAME: str = "도서 관리 API 서비스"
    REST_SERVICE_DESCRIPTION: str = "도서관리에 사용되는 API 서비스"
    REST_SERVICE_VERSION: str = "0.1.0"


class DataSettings(BaseSettings):
    DB_URI: PostgresDsn = Field(env="DATABASE_PG_URL")


class SecuritySettings(BaseSettings):
    PASSWORD_ALGORITHMS: str = Field("argon2")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)
    JWT_ALGORITHMS: str = Field("HS256")
    JWT_SECRET: str = Field(
        env="JWT_SECRET",
        default="b1f23f1479aa91c79720ce2fd1f3694c0aa7a3e0ebad5802ec09a9c867e9788f",
    )


class Settings(BaseSettings):
    DEBUG: bool = Field(env="DEBUG", default=True)

    desc: ServerDescriptionSettings = ServerDescriptionSettings()
    data: DataSettings = DataSettings()
    security: SecuritySettings = SecuritySettings()

    class Config:
        case_sensitive = True


settings = Settings()
