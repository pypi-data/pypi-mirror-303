import backtrader as bt
import os
import pytz
import requests
from datetime import datetime, timedelta
import time
from ffquant.utils.Logger import stdout_log

__ALL__ = ['BaseIndicator']

class BaseIndicator(bt.Indicator):

    params = (
        ('url', f"{os.environ.get('FINTECHFF_INDICATOR_BASE_URL', 'http://192.168.25.98:8088')}/signal/list"),
        ('symbol', 'CAPITALCOM:HK50'),
        ('max_retries', 30),
        ('prefetch_size', 60),
        ('debug', False)
    )

    def __init__(self):
        pass

    def handle_api_resp(self, result):
        pass

    def determine_final_result(self):
        pass

    def next(self):
        # skip the starting empty bars
        if len(self.data.close.array) == 0:
            return
        current_bar_time = self.data.datetime.datetime(0).replace(tzinfo=pytz.utc).astimezone()
        current_bar_time_str = current_bar_time.strftime('%Y-%m-%d %H:%M:%S')

        is_live = self.data.islive()
        if is_live:
            if current_bar_time_str not in self.cache:
                start_time = current_bar_time
                start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
                end_time = current_bar_time + timedelta(minutes=1)
                end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')

                params = {
                    'startTime' : start_time_str,
                    'endTime' : end_time_str,
                    'symbol' : self.p.symbol
                }

                # fill with -inf
                self.cache[current_bar_time_str] = float('-inf')

                retry_count = 0
                max_retry_count = self.p.max_retries
                while retry_count < max_retry_count:
                    retry_count += 1
                    if self.p.debug:
                        stdout_log(f"{self.__class__.__name__}, fetch data params: {params}")

                    response = requests.get(self.p.url, params=params).json()
                    if self.p.debug:
                        stdout_log(f"{self.__class__.__name__}, fetch data response: {response}")

                    if response.get('code') != 0:
                        raise ValueError(f"{self.__class__.__name__}, API request failed: {response}")

                    if response.get('results') is not None and len(response['results']) > 0:
                        for result in response['results']:
                            self.handle_api_resp(result)
                        break
                    time.sleep(1)
            else:
                if self.p.debug:
                    stdout_log(f"{self.__class__.__name__}, current_time_str: {current_bar_time_str}, hit cache: {self.cache[current_bar_time_str]}")
        else:
            if current_bar_time_str not in self.cache:
                start_time = current_bar_time
                start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
                end_time = current_bar_time + timedelta(minutes=self.p.prefetch_size)
                now = datetime.now().astimezone()
                if end_time > now:
                    end_time = now.replace(second=0, microsecond=0)
                end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
                params = {
                    'startTime' : start_time_str,
                    'endTime' : end_time_str,
                    'symbol' : self.p.symbol
                }

                # fill with -inf value in this range
                for i in range(0, int((end_time.timestamp() - start_time.timestamp()) / 60)):
                    self.cache[(start_time + timedelta(minutes=i)).strftime('%Y-%m-%d %H:%M:%S')] = float('-inf')

                retry_count = 0
                max_retry_count = 1
                while retry_count < max_retry_count:
                    retry_count += 1
                    if self.p.debug:
                        stdout_log(f"{self.__class__.__name__}, fetch data params: {params}")

                    response = requests.get(self.p.url, params=params).json()
                    if self.p.debug:
                        stdout_log(f"{self.__class__.__name__}, fetch data response: {response}")

                    if response.get('code') != 0:
                        raise ValueError(f"{self.__class__.__name__}, API request failed: {response}")

                    if response.get('results') is not None and len(response['results']) > 0:
                        for result in response['results']:
                            self.handle_api_resp(result)
                        break
                    time.sleep(1)
            else:
                if self.p.debug:
                    stdout_log(f"{self.__class__.__name__}, current_time_str: {current_bar_time_str}, hit cache: {self.cache[current_bar_time_str]}")

        self.determine_final_result()