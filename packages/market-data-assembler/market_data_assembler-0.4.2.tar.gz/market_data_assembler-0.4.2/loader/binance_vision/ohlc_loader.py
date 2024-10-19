import csv
import os
import zipfile
from abc import ABC
from datetime import datetime
from typing import List, Dict, Any

import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

from loader.ohlc_loader_interface import IOhlcLoader


class BinanceVisionOhlcLoader(IOhlcLoader, ABC):
    def __init__(self, selected_date: datetime, instrument: str):
        self.selected_date = selected_date.strftime('%Y-%m-%d')
        self.instrument = instrument
        self.temp_folder = f'./out/temp/klines/{self.instrument}/'
        self.extracted_folder = os.path.join(self.temp_folder, 'extracted')
        os.makedirs(self.temp_folder, exist_ok=True)

    @retry(stop=stop_after_attempt(15), wait=wait_fixed(10),
           retry=retry_if_exception_type((ConnectionError, Timeout, HTTPError, RequestException)))
    def _download_ohlc_archive(self) -> str:
        local_zip_path = os.path.join(self.temp_folder, f"{self.instrument}-1m-{self.selected_date}.zip")

        if not os.path.exists(local_zip_path):
            url = f"https://data.binance.vision/data/futures/um/daily/klines/{self.instrument}/1m/{self.instrument}-1m-{self.selected_date}.zip"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()

                with open(local_zip_path, 'wb') as f:
                    f.write(response.content)
            except (ConnectionError, Timeout, HTTPError, RequestException) as e:
                print(f"Failed to download the ohlc archive from {url}: {e}")
                raise

        return local_zip_path

    def _extract_ohlc(self, zip_path: str) -> str:
        os.makedirs(self.extracted_folder, exist_ok=True)
        extracted_file = os.path.join(self.extracted_folder, f"{self.instrument}-1m-{self.selected_date}.csv")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.extracted_folder)

        return extracted_file

    def _map_ohlc(self, ohlc_row: Dict[str, Any]) -> Dict[str, Any]:
        mapped_ohlc = {
            't': int(ohlc_row['open_time']),
            'o': float(ohlc_row['open']),
            'h': float(ohlc_row['high']),
            'l': float(ohlc_row['low']),
            'c': float(ohlc_row['close']),
            'v': float(ohlc_row['volume'])
        }
        return mapped_ohlc

    def get_ohlc_series(self) -> List[Dict[str, Any]]:
        zip_path = self._download_ohlc_archive()
        csv_path = self._extract_ohlc(zip_path)
        ohlc_series = []
        with open(csv_path, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=['open_time', 'open', 'high', 'low', 'close', 'volume',
                                                      'close_time', 'quote_volume', 'count',
                                                      'taker_buy_volume', 'taker_buy_quote_volume', 'ignore'])
            next(reader, None)
            for row in reader:
                ohlc_series.append(self._map_ohlc(row))

        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(csv_path):
            os.remove(csv_path)

        print(
            f'{self.instrument}:{self.selected_date}:{len(ohlc_series)}:ohlc')
        return ohlc_series
