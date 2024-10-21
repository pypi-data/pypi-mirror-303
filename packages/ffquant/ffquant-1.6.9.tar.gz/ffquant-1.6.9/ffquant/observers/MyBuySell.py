import backtrader as bt
import pytz
import ffquant.utils.observer_data as observer_data

__ALL__ = ['MyBuySell']

class MyBuySell(bt.observers.BuySell):

    def __init__(self):
        super(MyBuySell, self).__init__()
        self.output_list = observer_data.buysell

    def start(self):
        super(MyBuySell, self).start()
        self.output_list.clear()

    def next(self):
        super(MyBuySell, self).next()
        msg = {
            "datetime": self.data.datetime.datetime(0).replace(tzinfo=pytz.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S"),
            "price": self.data.close[0],
            "buy": self.lines.buy[0],
            "sell": self.lines.sell[0]
        }
        self.output_list.append(msg)