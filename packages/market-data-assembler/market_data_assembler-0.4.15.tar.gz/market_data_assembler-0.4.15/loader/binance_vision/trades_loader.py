import csv
import os
import zipfile
from abc import ABC
from datetime import datetime
from typing import List, Dict, Any

import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

from loader.trades_loader_interface import ITradesLoader


class BinanceVisionTradesLoader(ITradesLoader, ABC):
    def __init__(self, selected_date: datetime, instrument: str):
        self.selected_date = selected_date.strftime('%Y-%m-%d')
        self.instrument = instrument
        self.temp_folder = f'./out/temp/trades/{self.instrument}/'
        self.extracted_folder = os.path.join(self.temp_folder, 'extracted')
        os.makedirs(self.temp_folder, exist_ok=True)

    @retry(stop=stop_after_attempt(15), wait=wait_fixed(10),
           retry=retry_if_exception_type((ConnectionError, Timeout, HTTPError, RequestException)))
    def _download_trades_archive(self) -> str:
        local_zip_path = os.path.join(self.temp_folder, f"{self.instrument}-trades-{self.selected_date}.zip")

        if not os.path.exists(local_zip_path):
            url = f"https://data.binance.vision/data/futures/um/daily/trades/{self.instrument}/{self.instrument}-trades-{self.selected_date}.zip"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()

                with open(local_zip_path, 'wb') as f:
                    f.write(response.content)
            except (ConnectionError, Timeout, HTTPError, RequestException) as e:
                print(f"Failed to download the trades archive from {url}: {e}")
                raise

        return local_zip_path

    def _extract_trades(self, zip_path: str) -> str:
        os.makedirs(self.extracted_folder, exist_ok=True)
        extracted_file = os.path.join(self.extracted_folder, f"{self.instrument}-trades-{self.selected_date}.csv")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.extracted_folder)

        return extracted_file

    @staticmethod
    def _map_trade(trade_row: Dict[str, Any]) -> Dict[str, Any]:
        mapped_trade = {
            'c': 'b' if trade_row['is_buyer_maker'] == 'true' else 's',
            's': float(trade_row['qty']),
            'p': float(trade_row['price']),
            't': int(trade_row['time'])
        }
        return mapped_trade

    def get_trades(self) -> List[Dict[str, Any]]:
        zip_path = self._download_trades_archive()
        csv_path = self._extract_trades(zip_path)
        trades = []
        with open(csv_path, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=['id', 'price', 'qty', 'quote_qty', 'time', 'is_buyer_maker'])
            next(reader, None)
            for row in reader:
                trades.append(self._map_trade(row))

        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(csv_path):
            os.remove(csv_path)

        return trades
