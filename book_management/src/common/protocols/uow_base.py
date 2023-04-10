#
# 모든 UoW의 기반이 되는 베이스 클래스
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/08 01:28 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


from abc import ABC, abstractmethod
from typing import Optional, Protocol, Type, TypeVar, Union


class AsyncBaseUnitOfWork(ABC):
    @abstractmethod
    async def __aenter__(self) -> None:
        raise NotImplementedError("required __aenter__ call for UoW Pattern")

    async def __aexit__(
            self,
            exc_type: Optional[Type[Exception]],
            exc_val: Optional[Exception],
            traceback,
    ):
        if exc_type:
            await self.rollback()

    @abstractmethod
    async def commit(self):
        raise NotImplementedError("Choice ORM commit func")

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError("Choice ORM rollback func")


_UT = TypeVar("_UT", bound=Union[AsyncBaseUnitOfWork])


class BaseUseCase(Protocol[_UT]):
    _uow: _UT

    @property
    def uow(self) -> _UT:
        assert self._uow is not None
        return self._uow
