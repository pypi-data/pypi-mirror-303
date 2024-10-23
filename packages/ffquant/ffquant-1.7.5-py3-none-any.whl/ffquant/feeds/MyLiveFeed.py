import pandas as pd
import backtrader as bt
import requests
import os
from datetime import datetime, timedelta, timezone
import time
import pytz
import queue
from ffquant.utils.Logger import stdout_log

__ALL__ = ['MyLiveFeed']

class MyLiveFeed(bt.feeds.DataBase):
    params = (
        ('url', f"{os.environ.get('FINTECHFF_FEED_BASE_URL', 'http://192.168.25.127:8288')}/symbol/info/list"),
        ('fromdate', None),
        ('todate', None),
        ('symbol', None),
        ('timeframe', bt.TimeFrame.Minutes),
        ('compression', 1),
        ('debug', False),
        ('max_retries', 15),
        ('backpeek_size', 60),
        ('backfill_size', 0),
    )

    lines = (('turnover'),)

    def __init__(self):
        self._timeframe = self.p.timeframe
        self._compression = self.p.compression
        super(MyLiveFeed, self).__init__()
        self.cache = {}
        self.history_data_queue = queue.Queue()

    def islive(self):
        return True

    def start(self):
        super().start()

        if self.p.backfill_size > 0:
            now = datetime.now()
            end_time = now.replace(second=0, microsecond=0)
            end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')

            start_time = (end_time - timedelta(minutes=self.p.backfill_size)).replace(second=0, microsecond=0)
            start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')

            params = {
                'startTime': start_time_str,
                'endTime': end_time_str,
                'symbol': self.p.symbol
            }

            if self.p.debug:
                stdout_log(f"MyLiveFeed, backfill params: {params}")

            response = requests.get(self.p.url, params=params).json()
            if self.p.debug:
                stdout_log(f"MyLiveFeed, backfill response: {response}")

            if response.get('code') != '200':
                raise ValueError(f"API request failed: {response}")

            results = response.get('results', [])
            results.sort(key=lambda x: x['timeOpen'])
            for result in results:
                self.history_data_queue.put(result)


    def _load(self):
        if not self.history_data_queue.empty():
            if self.p.debug:
                stdout_log(f"MyLiveFeed, history_data_queue size: {self.history_data_queue.qsize()}, backfill from history")
            history_item = self.history_data_queue.get()
            self.lines.datetime[0] = bt.date2num(datetime.fromtimestamp(history_item['timeOpen'] / 1000.0, timezone.utc))
            self.lines.open[0] = history_item['open']
            self.lines.high[0] = history_item['high']
            self.lines.low[0] = history_item['low']
            self.lines.close[0] = history_item['close']
            self.lines.volume[0] = history_item['vol']
            self.lines.turnover[0] = history_item['turnover']
            return True

        now = datetime.now()
        current_time = (now.replace(second=0, microsecond=0) - timedelta(minutes=1)).astimezone(pytz.utc)
        current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

        # _load method of live feed is invoked frequently
        # so only in following case we need to fetch data
        # 1. the very first bar
        # 2. the very first _load invoke in a new minute
        if self.lines.datetime.idx == 0 or self.lines.datetime.datetime(-1).strftime('%Y-%m-%d %H:%M:%S') != current_time_str:
            start_time = (now - timedelta(minutes=1)).replace(second=0, microsecond=0)
            end_time = now.replace(second=0, microsecond=0)
            start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
            end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')

            retry_count = 0
            while retry_count < self.p.max_retries:
                retry_count += 1

                key = f"{current_time_str}"
                if key not in self.cache:
                    params = {
                        'startTime': start_time_str,
                        'endTime': end_time_str,
                        'symbol': self.p.symbol
                    }

                    if self.p.debug:
                        stdout_log(f"MyLiveFeed, fetch data params: {params}")

                    response = requests.get(self.p.url, params=params).json()
                    if self.p.debug:
                        stdout_log(f"MyLiveFeed, fetch data response: {response}")

                    if response.get('code') != '200':
                        raise ValueError(f"API request failed: {response}")

                    results = response.get('results', [])
                    if results is not None and len(results) > 0:
                        self.cache[key] = results[0]

                bar = self.cache.get(key, None)
                if bar is not None:
                    self.lines.datetime[0] = bt.date2num(datetime.fromtimestamp(bar['timeOpen'] / 1000.0, timezone.utc))
                    self.lines.open[0] = bar['open']
                    self.lines.high[0] = bar['high']
                    self.lines.low[0] = bar['low']
                    self.lines.close[0] = bar['close']
                    self.lines.volume[0] = bar['vol']
                    self.lines.turnover[0] = bar['turnover']
                    return True
                else:
                    time.sleep(1)

            # no available data for current minute, so we backpeek for the most recent data
            self.backpeek_for_result(current_time)
            return True

    def backpeek_for_result(self, current_time):

        # preset the default values
        self.lines.datetime[0] = bt.date2num(datetime.fromtimestamp(current_time.timestamp(), timezone.utc))
        self.lines.open[0] = 0.0
        self.lines.high[0] = 0.0
        self.lines.low[0] = 0.0
        self.lines.close[0] = 0.0
        self.lines.volume[0] = 0.0
        self.lines.turnover[0] = 0.0

        for i in range(0, self.p.backpeek_size):
            k = (current_time - timedelta(minutes=i)).strftime('%Y-%m-%d %H:%M:%S')
            v = self.cache.get(k, None)
            if v is not None:
                new_v = {
                    'timeOpen': int(current_time.timestamp()) * 1000,
                    'timeClose': (int(current_time.timestamp()) + 60) * 1000,
                    'updateTime': int(current_time.timestamp()),
                    'symbol': v['symbol'],
                    'open': v['close'],
                    'high': v['close'],
                    'low': v['close'],
                    'close': v['close'],
                    'vol': 0.0,
                    'turnover': 0.0,
                    'type': v['type']
                }

                if self.p.debug:
                    stdout_log(f"{self.__class__.__name__}, backpeek index: {i}, v: {v}, new_v: {new_v}")

                self.lines.datetime[0] = bt.date2num(datetime.fromtimestamp(new_v['timeOpen'] / 1000.0, timezone.utc))
                self.lines.open[0] = new_v['close']
                self.lines.high[0] = new_v['close']
                self.lines.low[0] = new_v['close']
                self.lines.close[0] = new_v['close']
                self.lines.volume[0] = 0.0
                self.lines.turnover[0] = 0.0

                self.cache[current_time.strftime('%Y-%m-%d %H:%M:%S')] = new_v
                break