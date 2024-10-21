import json
import unittest

from assembling.dataset_timeframe_aggregator import DatasetTimeframeAggregator


class TestDatasetTimeframeAggregator(unittest.TestCase):

    def test_aggregation_1m(self):
        self.aggregator = DatasetTimeframeAggregator(aggregation_window_sec=60)
        with open('raw_candles.json', 'r') as file:
            raw_candles_data = json.load(file)

        aggregated_results = []

        for candle in raw_candles_data:
            result = self.aggregator.aggregate(candle)
            if result:
                aggregated_results.append(result)

        final_aggregated_candle = self.aggregator.get_aggregated_tail()
        if final_aggregated_candle:
            aggregated_results.append(final_aggregated_candle)

        with open('aggregated_candles_1m.json', 'r') as file:
            expected_data = json.load(file)

        for agg_candle, expected_candle in zip(aggregated_results, expected_data):
            self.assertEqual(agg_candle['t'], expected_candle['t'])
            self.assertEqual(agg_candle['o'], expected_candle['o'])
            self.assertEqual(agg_candle['h'], expected_candle['h'])
            self.assertEqual(agg_candle['l'], expected_candle['l'])
            self.assertEqual(agg_candle['c'], expected_candle['c'])
            self.assertEqual(agg_candle['v'], expected_candle['v'])
            self.assertEqual(agg_candle['n'], expected_candle['n'])

    def test_aggregation_5m(self):
        self.aggregator = DatasetTimeframeAggregator(aggregation_window_sec=300)
        with open('raw_candles.json', 'r') as file:
            raw_candles_data = json.load(file)

        aggregated_results = []

        for candle in raw_candles_data:
            result = self.aggregator.aggregate(candle)
            if result:
                aggregated_results.append(result)

        final_aggregated_candle = self.aggregator.get_aggregated_tail()
        if final_aggregated_candle:
            aggregated_results.append(final_aggregated_candle)

        with open('aggregated_candles_5m.json', 'r') as file:
            expected_data = json.load(file)

        for agg_candle, expected_candle in zip(aggregated_results, expected_data):
            self.assertEqual(agg_candle['t'], expected_candle['t'])
            self.assertEqual(agg_candle['o'], expected_candle['o'])
            self.assertEqual(agg_candle['h'], expected_candle['h'])
            self.assertEqual(agg_candle['l'], expected_candle['l'])
            self.assertEqual(agg_candle['c'], expected_candle['c'])
            self.assertEqual(agg_candle['v'], expected_candle['v'])
            self.assertEqual(agg_candle['n'], expected_candle['n'])


if __name__ == '__main__':
    unittest.main()
