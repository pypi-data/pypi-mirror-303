from ffquant.indicators.BaseIndicator import BaseIndicator
from datetime import datetime, timedelta
import pytz
from ffquant.utils.Logger import stdout_log

__ALL__ = ['ShortTermDirection']

class ShortTermDirection(BaseIndicator):
    (BEARISH, NA, BULLISH) = (-1, 0, 1)

    lines = ('std',)

    def __init__(self):
        self.addminperiod(1)
        self.cache = {}

    def handle_api_resp(self, item):
        result_time_str = datetime.fromtimestamp(item['openTime']/ 1000).strftime('%Y-%m-%d %H:%M:%S')
        if item.get('SHORT_TERM_DIR', None) is not None and item['SHORT_TERM_DIR'] == 'BULLISH':
            self.cache[result_time_str] = self.BULLISH
        elif item.get('SHORT_TERM_DIR', None) is not None and item['SHORT_TERM_DIR'] == 'BEARISH':
            self.cache[result_time_str] = self.BEARISH
        elif item.get('SHORT_TERM_DIR', None) is not None and item['SHORT_TERM_DIR'] == 'NA':
            self.cache[result_time_str] = self.NA

        if self.p.debug:
            stdout_log(f"{self.__class__.__name__}, result_time_str: {result_time_str}, short_term_dir: {item.get('SHORT_TERM_DIR', None)}")

    def determine_final_result(self):
        current_bar_time = self.data.datetime.datetime(0).replace(tzinfo=pytz.utc).astimezone()
        current_bar_time_str = current_bar_time.strftime('%Y-%m-%d %H:%M:%S')
        self.lines.std[0] = self.cache[current_bar_time_str]