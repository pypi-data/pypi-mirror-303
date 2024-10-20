from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Any


class IBookDeptLoader(ABC):

    @abstractmethod
    def __init__(self, selected_date: datetime, instrument: str):
        pass

    @abstractmethod
    def get_book_depths(self) -> List[Dict[str, Any]]:
        pass
