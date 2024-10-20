from abc import ABC, abstractmethod
from typing import Dict, Any


class IndicatorInterface(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_window_length(self) -> int:
        pass

    @abstractmethod
    def apply(self, candle: Dict) -> Any:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass
