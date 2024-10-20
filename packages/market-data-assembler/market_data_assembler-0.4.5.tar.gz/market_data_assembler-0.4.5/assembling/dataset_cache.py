import json
import os
from typing import List

from assembling.dataset_labeler_abstract import BaseDatasetLabeler
from common.common import prepare_directory
from indicators.indicator_abstract import BaseIndicator


class DatasetCache:
    CONFIG_FILE_PREFIX = '_dataset_config.json'

    def __init__(self, dataset_out_root_folder: str, instruments: List[str], aggregation_window: int,
                 dataset_labeler: BaseDatasetLabeler, indicators: List[BaseIndicator], dataset_unique_name: str):
        self.dataset_out_root_folder = dataset_out_root_folder
        self.instruments = instruments
        self.aggregation_window = aggregation_window
        self.dataset_labeler = dataset_labeler
        self.indicators = indicators
        self.dataset_unique_name = dataset_unique_name
        self.dataset_out_folder = os.path.join(self.dataset_out_root_folder, self.dataset_unique_name)

    def load(self):
        config = self._generate_dataset_config()
        for file in os.listdir(self.dataset_out_root_folder):
            if file.endswith(self.CONFIG_FILE_PREFIX):
                with open(os.path.join(self.dataset_out_root_folder, file), 'r') as f:
                    existing_config = json.load(f)
                    if existing_config == config:
                        dataset_folder = file.replace(self.CONFIG_FILE_PREFIX, '')
                        dataset_path = os.path.join(self.dataset_out_root_folder, dataset_folder)
                        return self._load_existing_datasets(dataset_path)
        return None

    def save(self, datasets):
        prepare_directory(self.dataset_out_folder)
        config = self._generate_dataset_config()
        config_path = os.path.join(self.dataset_out_root_folder, f'{self.dataset_unique_name}{self.CONFIG_FILE_PREFIX}')
        with open(config_path, 'w') as config_file:
            json.dump(config, config_file, indent=1)
        print(f"Config saved at: {config_path}")

        for dataset in datasets:
            instrument = dataset['instrument']
            dataset_filename = f"{instrument}_{dataset['timestamp']}.json"
            dataset_filepath = os.path.join(self.dataset_out_folder, dataset_filename)
            with open(dataset_filepath, 'w') as f:
                json.dump(dataset, f, indent=1)
        print(f"Saved {len(datasets)} datasets")

    @staticmethod
    def _load_existing_datasets(dataset_path):
        all_datasets = []
        for file in os.listdir(dataset_path):
            if file.endswith('.json'):
                with open(os.path.join(dataset_path, file), 'r') as f:
                    dataset = json.load(f)
                    all_datasets.append(dataset)
        print(f"Loaded {len(all_datasets)} datasets from {dataset_path}")
        return all_datasets

    def _generate_dataset_config(self):
        config = {
            "instruments": self.instruments,
            "aggregation_window": self.aggregation_window,
            "labeling": {
                "name": self.dataset_labeler.get_name(),
                "training_window_length": self.dataset_labeler.training_window_length,
                "prediction_window_length": self.dataset_labeler.prediction_window_length,
            },
            "indicators": [
                {
                    "name": indicator.get_name(),
                    "window_length": indicator.window_length
                } for indicator in self.indicators
            ]
        }
        return config
