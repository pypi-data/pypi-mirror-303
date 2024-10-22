from abc import ABC, abstractmethod
from typing import Any, Optional


class IEntityExtractor(ABC):
    @abstractmethod
    def extract(self, entity: Any) -> Optional[str]:
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError
