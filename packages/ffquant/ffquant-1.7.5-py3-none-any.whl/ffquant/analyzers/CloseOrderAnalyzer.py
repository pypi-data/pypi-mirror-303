import backtrader as bt
import pytz

__ALL__ = ['CloseOrderAnalyzer']

class CloseOrderAnalyzer(bt.Analyzer):
    def __init__(self):
        self.close_orders = []
        self.last_avg_prices = {}
    
    def notify_order(self, order):
        if order.status == order.Submitted:
            print(f"position size: {self.strategy.position.size}")
            if self.strategy.position.size != 0:
                self.last_avg_prices[order.ref] = self.strategy.position.price
                print(f"save average price {order.ref}: {self.last_avg_prices[order.ref]}")

        elif order.status == order.Completed:
            if self.strategy.position.size == 0:
                dt = self.data.datetime.datetime(0).replace(tzinfo=pytz.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S")
                order_info = {
                    'datetime': dt,
                    'side': bt.Order.OrdTypes[order.ordtype],
                    'executed_price': order.executed.price,
                    'executed_size': order.executed.size,
                    'last_avg_price': self.last_avg_prices[order.ref],
                }
                self.close_orders.append(order_info)
            else:
                print(f"not a close order, order: {order}")
    
    def get_analysis(self):
        return self.close_orders