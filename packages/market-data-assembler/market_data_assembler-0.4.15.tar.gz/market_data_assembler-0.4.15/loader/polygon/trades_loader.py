import datetime
import os
from abc import ABC
from datetime import datetime
from typing import Dict, List, Any

import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

from loader.trades_loader_interface import ITradesLoader


class PolygonTradesLoader(ITradesLoader, ABC):
    def __init__(self, selected_date: datetime, instrument: str):
        self.api_token = os.getenv('POLYGON_API_TOKEN')
        if not self.api_token:
            raise EnvironmentError(
                "POLYGON_API_TOKEN is required to access the API. Please set the environment variable.")
        self.selected_date = selected_date
        self.instrument = instrument

    @staticmethod
    def _map_trades(trades_data) -> List[Dict[str, Any]]:
        return [
            {
                't': int(trade['participant_timestamp']) // 1_000_000,
                'p': trade['price'],
                's': trade['size'],
                'c': "s" if 1 in trade['conditions'] else "b" if 2 in trade['conditions'] else "unknown"
            }
            for trade in trades_data
        ]

    @retry(stop=stop_after_attempt(15), wait=wait_fixed(10),
           retry=retry_if_exception_type((ConnectionError, Timeout, HTTPError, RequestException)))
    def _download_trades(self):
        formatted_date = self.selected_date.strftime("%Y-%m-%d")
        url = f"https://api.polygon.io/v3/trades/X:{self.instrument}"
        params = {
            "timestamp": formatted_date,
            "limit": 50000,
            "apiKey": self.api_token
        }

        trades_data = []
        while url:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            trades_data.extend(data.get('results', []))
            url = data.get('next_url', None)
            params = {
                "apiKey": self.api_token
            }

        trades_data = sorted(trades_data, key=lambda x: x['participant_timestamp'])
        return trades_data

    def get_trades(self) -> List[Dict[str, Any]]:
        trades = self._download_trades()
        trades = self._map_trades(trades)
        trades = sorted(trades, key=lambda x: x['t'])

        if trades:
            start_time_ns = trades[0]['t']
            end_time_ns = trades[-1]['t']

            start_time = datetime.utcfromtimestamp(start_time_ns / 1_000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            end_time = datetime.utcfromtimestamp(end_time_ns / 1_000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

            print(f"Total trades loaded from {start_time} to {end_time}, size {len(trades)}")

        return trades
