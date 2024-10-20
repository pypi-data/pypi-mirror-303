from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Any


class ITradesLoader(ABC):

    @abstractmethod
    def __init__(self, selected_date: datetime, instrument: str):
        pass

    @abstractmethod
    def get_trades(self) -> List[Dict[str, Any]]:
        pass
