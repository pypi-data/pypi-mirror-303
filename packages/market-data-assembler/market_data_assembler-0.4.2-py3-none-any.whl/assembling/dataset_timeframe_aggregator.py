from datetime import datetime, timedelta, timezone

class DatasetTimeframeAggregator:
    def __init__(self, aggregation_window_sec):
        self.aggregation_window_sec = aggregation_window_sec
        self.current_window_candles = []
        self.start_time = None

    @staticmethod
    def _parse_datetime(timestamp_ms):
        return datetime.utcfromtimestamp(timestamp_ms / 1000).replace(tzinfo=timezone.utc)

    def _aggregate_candles(self, end_time):
        open_price = self.current_window_candles[0]['o']
        close_price = self.current_window_candles[-1]['c']
        high_price = max(candle['h'] for candle in self.current_window_candles)
        low_price = min(candle['l'] for candle in self.current_window_candles)
        volume = sum(candle['v'] for candle in self.current_window_candles)
        total_trades = sum(candle['n'] for candle in self.current_window_candles)

        aggregated_trades = []
        for candle in self.current_window_candles:
            aggregated_trades.extend(candle['trades'])

        aggregated_trades.sort(key=lambda trade: trade['t'])
        t = int(end_time.timestamp() * 1000)
        aggregated_time = end_time.strftime('%Y-%m-%d %H:%M:%S')

        aggregated_candle = {
            "datetime": aggregated_time,
            "t": t,
            "o": open_price,
            "h": high_price,
            "l": low_price,
            "c": close_price,
            "v": volume,
            "n": total_trades,
            "trades": aggregated_trades
        }

        if len(aggregated_candle['trades']) != aggregated_candle['n']:
            candle_time = datetime.utcfromtimestamp(aggregated_candle['t'] / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Warning: The number of trades for candle at {candle_time} does not match. "
                  f"Expected: {aggregated_candle['n']}, Found: {len(aggregated_candle['trades'])}")

        return aggregated_candle

    def aggregate(self, new_candle):
        candle_time = self._parse_datetime(new_candle["t"])

        if self.start_time is None:
            self.start_time = candle_time - timedelta(seconds=candle_time.second % self.aggregation_window_sec,
                                                      microseconds=candle_time.microsecond)

        window_end_time = self.start_time + timedelta(seconds=self.aggregation_window_sec)

        while candle_time >= window_end_time:
            if self.current_window_candles:
                aggregated_candle = self._aggregate_candles(window_end_time)
                self.start_time = window_end_time
                self.current_window_candles = []
                self.current_window_candles.append(new_candle)
                return aggregated_candle
            self.start_time += timedelta(seconds=self.aggregation_window_sec)

        self.current_window_candles.append(new_candle)
        return None

    def get_aggregated_tail(self):
        if self.current_window_candles:
            end_time = self.start_time + timedelta(seconds=self.aggregation_window_sec)
            aggregated_candle = self._aggregate_candles(end_time)
            self.current_window_candles = []
            return aggregated_candle
        return None