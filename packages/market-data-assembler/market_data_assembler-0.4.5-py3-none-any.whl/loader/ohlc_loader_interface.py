from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Any


class IOhlcLoader(ABC):

    @abstractmethod
    def __init__(self, selected_date: datetime, instrument: str):
        pass

    @abstractmethod
    def get_ohlc_series(self) -> List[Dict[str, Any]]:
        pass
