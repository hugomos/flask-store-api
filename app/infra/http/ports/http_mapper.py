from typing import Any, Optional
from abc import ABC, abstractmethod


class HttpMapper(ABC):
    @abstractmethod
    def map(self, input: Optional[Any]) -> Any:
        pass
