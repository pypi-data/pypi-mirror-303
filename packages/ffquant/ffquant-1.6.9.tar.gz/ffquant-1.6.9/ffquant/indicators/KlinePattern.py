from ffquant.indicators.BaseIndicator import BaseIndicator
from datetime import datetime, timedelta
import pytz
from ffquant.utils.Logger import stdout_log

__ALL__ = ['KlinePattern']

class KlinePattern(BaseIndicator):
    (DECREASING, STABLE, INCREASING) = (-1, 0, 1)

    lines = ('kp',)

    def __init__(self):
        self.addminperiod(1)
        self.cache = {}

    def handle_api_resp(self, item):
        result_time_str = datetime.fromtimestamp(item['openTime']/ 1000).strftime('%Y-%m-%d %H:%M:%S')
        if item.get('TYPE_TREND', None) is not None and item['TYPE_TREND'] == 'BULLISH':
            self.cache[result_time_str] = self.INCREASING
        elif item.get('TYPE_TREND', None) is not None and item['TYPE_TREND'] == 'BEARISH':
            self.cache[result_time_str] = self.DECREASING
        elif item.get('TYPE_TREND', None) is not None and item['TYPE_TREND'] == 'NA':
            self.cache[result_time_str] = self.STABLE

        if self.p.debug:
            stdout_log(f"{self.__class__.__name__}, result_time_str: {result_time_str}, type_trend: {item.get('TYPE_TREND', None)}")

    def determine_final_result(self):
        current_bar_time = self.data.datetime.datetime(0).replace(tzinfo=pytz.utc).astimezone()
        current_bar_time_str = current_bar_time.strftime('%Y-%m-%d %H:%M:%S')
        self.lines.kp[0] = self.cache[current_bar_time_str]