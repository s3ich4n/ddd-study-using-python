#
# Dependency Injector의 컨테이너
#   참고: https://github.com/ets-labs/python-dependency-injector
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/078 18:28 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


from dependency_injector import containers, providers

from src.common.infrastructures.postgres.sqlalchemy import AsyncSQLAlchemy
from src.core.api_config import Settings
from src.core.fastapi.login.auth_service import AuthService

# from src.modules.users.application.command.login.impl import PaperUserLoginUseCase
# from src.modules.users.application.command.signup.impl import PaperUserSignUpUseCase
# from src.modules.users.application.uow import PaperUserUnitOfWork


class Container(containers.DeclarativeContainer):
    __self__ = providers.Self()

    config = providers.Configuration()
    config.from_pydantic(Settings())

    #
    # Basic
    #
    db = providers.Singleton(
        AsyncSQLAlchemy,
        db_uri=config.data.DB_URI,
    )

    auth_service = providers.Factory(
        AuthService,
        security_config=config.security,
    )

    #
    # UoW
    #
    # paper_user_unit_of_work = providers.Factory(
    #     PaperUserUnitOfWork,
    #     engine=db.provided.engine,
    # )
    #
    # #
    # # Usecases
    # #
    # signup_command = providers.Factory(
    #     PaperUserSignUpUseCase,
    #     uow=paper_user_unit_of_work,
    #     engine=db.provided.engine,
    #     auth_service=auth_service,
    # )
    #
    # login_command = providers.Factory(
    #     PaperUserLoginUseCase,
    #     uow=paper_user_unit_of_work,
    #     engine=db.provided.engine,
    #     auth_service=auth_service,
    # )
