from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class BaseIndicator(ABC):
    def __init__(self, window_length: int):
        self.window_length = window_length
        self.candles: List[Dict] = []

    def apply(self, candle: Dict) -> Optional[float]:
        self.candles.append(candle)
        if len(self.candles) < self.window_length:
            return None

        if len(self.candles) > self.window_length:
            self.candles.pop(0)

        return self.calculate_value()

    @abstractmethod
    def calculate_value(self) -> float:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    def reset(self) -> None:
        self.candles = []