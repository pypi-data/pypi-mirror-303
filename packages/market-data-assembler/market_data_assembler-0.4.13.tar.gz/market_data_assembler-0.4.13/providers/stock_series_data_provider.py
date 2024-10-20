import os
from datetime import datetime
from typing import List, Dict

import pytz
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from tenacity import retry, wait_fixed, stop_after_attempt, retry_if_exception_type

from common.common import generate_date_range
from indicators.indicator_interface import IndicatorInterface


class StockSeriesDataProvider:
    def __init__(self, instruments: List[str], day_from: datetime, day_to: datetime, use_us_session: bool = False,
                 interval: int = 1, interval_type: str = 'minute', indicators: List[IndicatorInterface] = None):
        self.api_token = os.getenv('POLYGON_API_TOKEN')
        if not self.api_token:
            raise EnvironmentError(
                "POLYGON_API_TOKEN is required to access the API. Please set the environment variable.")
        self.interval = interval
        self.interval_type = interval_type
        self.use_us_session = use_us_session
        self.selected_days = generate_date_range(day_from, day_to)
        self.ohlc_data = {instrument: [] for instrument in instruments}
        self.indicators = indicators

    @retry(stop=stop_after_attempt(15), wait=wait_fixed(10),
           retry=retry_if_exception_type((ConnectionError, Timeout, HTTPError, RequestException)))
    def _download_ohlc_series(self, selected_date: datetime, instrument: str) -> Dict:
        formatted_date = selected_date.strftime("%Y-%m-%d")
        print(f'{instrument} {formatted_date}')
        url = (f"https://api.polygon.io/v2/aggs/ticker/{instrument}/range/{self.interval}/{self.interval_type}/"
               f"{formatted_date}/{formatted_date}?adjusted=true&sort=asc&limit=50000&apiKey={self.api_token}")
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _filter_us_trading_session(target_date: datetime, ohlc_series: List[Dict]) -> List[Dict]:
        ny_tz = pytz.timezone('America/New_York')
        target_date_ny = ny_tz.localize(target_date)

        session_start = target_date_ny.replace(hour=9, minute=30, second=0)
        session_end = target_date_ny.replace(hour=16, minute=0, second=0)

        session_start_utc = session_start.astimezone(pytz.utc)
        session_end_utc = session_end.astimezone(pytz.utc)

        return [
            entry for entry in ohlc_series
            if session_start_utc <= datetime.strptime(entry['datetime'], "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=pytz.utc) <= session_end_utc
        ]

    def _filter_by_trading_session(self, ohlc_series: List[Dict]) -> List[Dict]:
        filtered_series = []
        for target_day in self.selected_days:
            daily_filtered_series = self._filter_us_trading_session(target_day, ohlc_series)
            filtered_series.extend(daily_filtered_series)
        filtered_series = sorted(filtered_series, key=lambda x: x['t'])

        return filtered_series

    def _map_ohlc_series(self, target_date: datetime, instrument: str) -> List[Dict[str, float]]:
        stock_data = self._download_ohlc_series(target_date, instrument)
        return [
            {
                'datetime': datetime.utcfromtimestamp(point['t'] / 1000.0).strftime("%Y-%m-%d %H:%M:%S"),
                't': point['t'],
                'o': point['o'],
                'h': point['h'],
                'l': point['l'],
                'c': point['c'],
                'v': point['v'],
            }
            for point in stock_data.get('results', [])
        ]

    def _populate_ohlc_series(self) -> None:
        for instrument in self.ohlc_data:
            series = []
            for target_day in self.selected_days:
                series.extend(self._map_ohlc_series(target_day, instrument))
            series = sorted(series, key=lambda x: x['t'])

            if self.indicators:
                for i, candle in enumerate(series):
                    for indicator in self.indicators:
                        window_length = indicator.get_window_length()

                        if i + 1 >= window_length:
                            indicator_value = indicator.apply(candle)
                        else:
                            indicator_value = None
                        candle[indicator.get_name()] = indicator_value

            if self.use_us_session:
                series = self._filter_by_trading_session(series)

            series = [candle for candle in series if all(value is not None for value in candle.values())]
            self.ohlc_data[instrument] = sorted(series, key=lambda x: x['t'])

    def get_all_instruments_sliced_by_window(self, window: int) -> List[List[Dict]]:
        if not any(self.ohlc_data[instrument] for instrument in self.ohlc_data):
            self._populate_ohlc_series()

        dataset = []
        for ohlc_series in self.ohlc_data.values():
            if len(ohlc_series) < window:
                raise ValueError("Window size is too large for the given datasets.")
            for i in range(len(ohlc_series) - window + 1):
                dataset.append(ohlc_series[i:i + window])
        return dataset

    def get_series(self, instrument: str) -> List[Dict]:
        if not any(self.ohlc_data[instrument] for instrument in self.ohlc_data):
            self._populate_ohlc_series()

        ohlc_series = self.ohlc_data.get(instrument)
        return ohlc_series
