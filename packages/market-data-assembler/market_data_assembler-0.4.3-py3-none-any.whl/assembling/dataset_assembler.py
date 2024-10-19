import os
from datetime import datetime
from typing import List

from assembling.dataset_cache import DatasetCache
from assembling.dataset_labeler_abstract import BaseDatasetLabeler
from assembling.dataset_timeframe_aggregator import DatasetTimeframeAggregator
from common.common import load_json, random_string
from indicators.indicator_abstract import BaseIndicator


class CryptoSeriesDatasetAssembler:
    dataset_out_root_folder = './out/datasets'

    def __init__(self,
                 instruments: List[str],
                 aggregation_window: int,
                 dataset_labeler: BaseDatasetLabeler,
                 raw_series_folder: str,
                 indicators: List[BaseIndicator] = None,
                 dataset_cleanup_keys: List[str] = None):
        self.instruments = instruments
        self.aggregation_window = aggregation_window
        self.indicators: List[BaseIndicator] = indicators
        self.dataset_labeler: BaseDatasetLabeler = dataset_labeler
        self.raw_series_folder = raw_series_folder
        self.dataset_unique_name = random_string()
        self.dataset_cleanup_keys = set(dataset_cleanup_keys) if dataset_cleanup_keys else None

        self.cache_handler = DatasetCache(
            self.dataset_out_root_folder,
            self.instruments,
            self.aggregation_window,
            self.dataset_labeler,
            self.indicators,
            self.dataset_unique_name
        )

    def generate_dataset(self):
        all_datasets = self.cache_handler.load()
        if all_datasets is not None:
            return all_datasets

        all_datasets = []
        for instrument in self.instruments:
            labeled_series = []
            self.dataset_labeler.reset()
            [indicator.reset() for indicator in self.indicators]
            timeframe_aggregator = DatasetTimeframeAggregator(60 * self.aggregation_window)
            aggregated_candles = []
            loaded_candles = 0
            for file in self._filter_and_sort_files(instrument):
                series = load_json(file)
                for candle in series:
                    loaded_candles += 1
                    aggregated_candle = timeframe_aggregator.aggregate(candle)
                    if aggregated_candle:
                        aggregated_candles.append(aggregated_candle)
            aggregated_candle = timeframe_aggregator.get_aggregated_tail()
            if aggregated_candle:
                aggregated_candles.append(aggregated_candle)
            print(
                f'Instrument: {instrument}, loaded candles: {loaded_candles}, aggregated candles: {len(aggregated_candles)}')

            for i, candle in enumerate(aggregated_candles):
                for indicator in self.indicators:
                    indicator_value = indicator.apply(candle)
                    candle[indicator.get_name()] = indicator_value

            aggregated_candles = [candle for candle in aggregated_candles if
                                  all(value is not None for value in candle.values())]
            aggregated_candles = sorted(aggregated_candles, key=lambda x: x['t'])

            indicator_names = [indicator.get_name() for indicator in self.indicators]
            print(f"Instrument: {instrument}, indicators applied: {', '.join(indicator_names)}")

            for candle in aggregated_candles:
                labeled_window = self.dataset_labeler.apply(candle)
                if labeled_window:
                    labeled_series.append(labeled_window)

            print(f'{instrument}: {len(labeled_series)} examples assembled')

            self._cleanup_series(labeled_series)
            datasets = self._map_to_datasets(labeled_series, instrument)
            all_datasets.extend(datasets)

        self.cache_handler.save(all_datasets)

        return all_datasets

    @staticmethod
    def _map_to_datasets(labeled_series: List[dict], instrument: str):
        datasets = []
        for labeled in labeled_series:
            series = labeled['series']
            labels = labeled['labels']
            timestamp = series[0]['t']
            datasets.append({
                'instrument': instrument,
                'timestamp': timestamp,
                'series': series,
                'labels': labels
            })
        return datasets

    def _cleanup_series(self, labeled_series):
        if not self.dataset_cleanup_keys:
            return
        for labeled in labeled_series:
            for candle in labeled['series']:
                for key in list(candle.keys()):
                    if key in self.dataset_cleanup_keys:
                        del candle[key]

    def _filter_and_sort_files(self, instrument):
        all_files = os.listdir(self.raw_series_folder)
        instrument_files = [f for f in all_files if f.startswith(instrument)]
        instrument_files.sort(key=lambda x: datetime.strptime(x.split('_')[1].split('.')[0], '%Y-%m-%d'))
        return [os.path.join(self.raw_series_folder, f) for f in instrument_files]
