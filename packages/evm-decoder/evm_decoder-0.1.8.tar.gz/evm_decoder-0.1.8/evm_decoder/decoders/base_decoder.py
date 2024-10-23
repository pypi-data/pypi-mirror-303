from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseDecoder(ABC):
    @abstractmethod
    def can_decode(self, data: Any) -> bool:
        pass

    @abstractmethod
    def decode(self, data: Any) -> Dict[str, Any]:
        pass