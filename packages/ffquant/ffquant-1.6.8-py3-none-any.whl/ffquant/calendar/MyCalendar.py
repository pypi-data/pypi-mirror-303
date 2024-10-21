import os
import requests
from datetime import datetime
from ffquant.utils.Logger import stdout_log

__ALL__ = ['MyCalendar']

class MyCalendar:
    def __init__(self):
        self.base_url = f"{os.environ.get('FINTECHFF_CALENDAR_BASE_URL', 'http://192.168.25.98')}"
        pass

    """
    Checks if a given stock symbol is tradable at a specific date and time.

    Parameters:
        symbol (str): The stock symbol to check.
        dt (str): The date and time to check. Format: 'YYYY-MM-DD HH:MM:SS'.

    Returns:
        bool: True if the symbol is tradable, False otherwise.
    """
    def isSymbolTradable(self, symbol: str, dt: str):
        url = f"{self.base_url}/stocktradetime?code={symbol}&ts={int(datetime.strptime(dt, '%Y-%m-%d %H:%M:%S').astimezone().timestamp())}"
        response = requests.get(url).json()
        if response['code'] == 0:
            return response['isopen'] == 1
        return False

    """
    Retrieves the trade time ranges for a given stock symbol and date.

    Parameters:
        symbol (str): The stock symbol to retrieve trade time ranges for.
        dt (str): The date to retrieve trade time ranges for. Format: 'YYYY-MM-DD'.

    Returns:
        list: A list of trade time ranges.
    """
    def getTradeTimeRanges(self, symbol: str, dt: str):
        url = f"{self.base_url}/stocktradetimes?code={symbol}&date={datetime.strptime(dt, '%Y-%m-%d').strftime('%Y%m%d')}"
        response = requests.get(url).json()
        time_ranges = []
        if response['code'] == 0:
            time_ranges = response["results"]

        return time_ranges


if __name__ == "__main__":
    calendar = MyCalendar()
    stdout_log(calendar.isSymbolTradable('CAPITALCOM:HK50', '2024-09-24 09:30:00'))
    stdout_log(calendar.getTradeTimeRanges('CAPITALCOM:HK50', '2024-09-24'))