import csv
import os
import zipfile
from abc import ABC
from datetime import datetime, timezone
from typing import List, Dict, Any

import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

from loader.book_dept_loader_interface import IBookDeptLoader


class BinanceVisionBookDepthLoader(IBookDeptLoader, ABC):
    def __init__(self, selected_date: datetime, instrument: str):
        self.selected_date = selected_date.strftime('%Y-%m-%d')
        self.instrument = instrument
        self.temp_folder = f'./out/temp/book_depth/{self.instrument}/'
        self.extracted_folder = os.path.join(self.temp_folder, 'extracted')
        os.makedirs(self.temp_folder, exist_ok=True)

    @retry(stop=stop_after_attempt(15), wait=wait_fixed(10),
           retry=retry_if_exception_type((ConnectionError, Timeout, HTTPError, RequestException)))
    def _download_book_depth_archive(self) -> str:
        local_zip_path = os.path.join(self.temp_folder, f"{self.instrument}-bookDepth-{self.selected_date}.zip")

        if not os.path.exists(local_zip_path):

            url = f"https://data.binance.vision/data/futures/um/daily/bookDepth/{self.instrument}/{self.instrument}-bookDepth-{self.selected_date}.zip"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()

                with open(local_zip_path, 'wb') as f:
                    f.write(response.content)
            except (ConnectionError, Timeout, HTTPError, RequestException) as e:
                print(f"Failed to download the book_depth archive from {url}: {e}")
                raise

        return local_zip_path

    def _extract_book_depth(self, zip_path: str) -> str:
        os.makedirs(self.extracted_folder, exist_ok=True)
        extracted_file = os.path.join(self.extracted_folder, f"{self.instrument}-bookDepth-{self.selected_date}.csv")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.extracted_folder)

        return extracted_file

    @staticmethod
    def _map_book_depth(row: Dict[str, Any]) -> Dict[str, Any]:
        return {
            't': int(datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S').replace(
                tzinfo=timezone.utc).timestamp()) * 1000,
            'p': int(row['percentage']),
            'd': float(row['depth']),
            'n': float(row['notional'])
        }

    def get_book_depths(self) -> List[Dict[str, Any]]:
        zip_path = self._download_book_depth_archive()
        csv_path = self._extract_book_depth(zip_path)
        book_depth_data = []

        with open(csv_path, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=['timestamp', 'percentage', 'depth', 'notional'])
            next(reader, None)
            for row in reader:
                book_depth_data.append(self._map_book_depth(row))

        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(csv_path):
            os.remove(csv_path)

        return book_depth_data
