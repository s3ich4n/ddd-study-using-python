#
# SQLAlchemy - 모델 간 매핑에 사용되는 베이스 클래스
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/08 01:29 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


from abc import abstractmethod
from typing import Protocol

from . import D, P


class ModelMapper(Protocol[D, P]):
    @staticmethod
    @abstractmethod
    def map_to_domain_entity(model: P) -> D:
        ...

    @staticmethod
    @abstractmethod
    def map_to_persistence_entity(model: D) -> P:
        ...
