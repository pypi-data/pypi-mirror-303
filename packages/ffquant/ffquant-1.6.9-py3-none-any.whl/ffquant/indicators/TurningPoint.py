from ffquant.indicators.BaseIndicator import BaseIndicator
from datetime import datetime, timedelta
import pytz
from ffquant.utils.Logger import stdout_log

__ALL__ = ['TurningPoint']

class TurningPoint(BaseIndicator):
    (TURNING_DN, NA, TURNING_UP) = (-1, 0, 1)

    lines = ('tp',)

    def __init__(self):
        self.addminperiod(1)
        self.cache = {}

    def handle_api_resp(self, item):
        result_time_str = datetime.fromtimestamp(item['openTime']/ 1000).strftime('%Y-%m-%d %H:%M:%S')
        if item.get('TYPE_TURNING_POINT', None) is not None and item['TYPE_TURNING_POINT'] == 'TURNING_UP':
            self.cache[result_time_str] = self.TURNING_UP
        elif item.get('TYPE_TURNING_POINT', None) is not None and item['TYPE_TURNING_POINT'] == 'TURNING_DN':
            self.cache[result_time_str] = self.TURNING_DN
        elif item.get('TYPE_TURNING_POINT', None) is not None and item['TYPE_TURNING_POINT'] == 'NA':
            self.cache[result_time_str] = self.NA

        if self.p.debug:
            stdout_log(f"{self.__class__.__name__}, result_time_str: {result_time_str}, type_turning_point: {item.get('TYPE_TURNING_POINT', None)}")

    def determine_final_result(self):
        current_bar_time = self.data.datetime.datetime(0).replace(tzinfo=pytz.utc).astimezone()
        current_bar_time_str = current_bar_time.strftime('%Y-%m-%d %H:%M:%S')
        self.lines.tp[0] = self.cache[current_bar_time_str]