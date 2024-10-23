import backtrader as bt
import numpy as np
import dash
from dash import dash_table
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import psutil
import socket
from ffquant.plot.dash_ports import get_available_port
import getpass
import pytz
import threading
from ffquant.plot.dash_graph import show_perf_live_graph, show_perf_bt_graph
from ffquant.observers.MyBkr import MyBkr
from ffquant.observers.MyBuySell import MyBuySell
from ffquant.observers.MyDrawDown import MyDrawDown
from ffquant.observers.MyTimeReturn import MyTimeReturn
from ffquant.analyzers.OrderAnalyzer import OrderAnalyzer
from ffquant.utils.Logger import stdout_log

__ALL__ = ['run_and_show_performance']

def run_and_show_performance(cerebro, riskfree_rate = 0.01, use_local_dash_url=False, debug=False):
    if hasattr(cerebro, 'runstrats'):
        raise Exception('Cerebro already run. Cannot run again')

    add_observers(cerebro, debug)
    add_analyzers(cerebro, debug)

    is_live_trade = False
    for data in cerebro.datas:
        if data.islive():
            is_live_trade = True

    if is_live_trade:
        threading.Thread(target=lambda: cerebro.run()).start()
        show_perf_live_graph(riskfree_rate, use_local_dash_url, debug)
    else:
        cerebro.run()
        show_perf_bt_graph(riskfree_rate, use_local_dash_url)

def add_observers(cerebro, debug=False):
    cerebro.addobserver(MyBkr)
    cerebro.addobserver(MyBuySell)
    cerebro.addobserver(MyDrawDown)
    cerebro.addobserver(MyTimeReturn,
                        timeframe=bt.TimeFrame.Minutes, 
                        compression=1)

def add_analyzers(cerebro, debug=False):
    cerebro.addanalyzer(OrderAnalyzer)

def add_metrics_plot(strat, views, riskfree_rate = 0.01, debug=False):
    days_in_year = 252
    minutes_in_day = 6.5 * 60
    total_return = 0
    annual_return = 0
    for observer in strat.observers:
        if isinstance(observer, bt.observers.Broker):
            portfolio_values = []
            length = observer.lines.value.__len__()
            for i in range(0, length):
                portfolio_values.append(observer.lines.value.__getitem__(0 -(length - 1 - i)))
            total_return = portfolio_values[-1] / portfolio_values[0] - 1
            annual_return = (1 + total_return / (length / minutes_in_day)) ** days_in_year - 1
    if debug:
        stdout_log(f"Total Return: {total_return:.8%}, Annualized Return: {annual_return:.8%}")

    std_annual = "NaN"
    sharpe = "NaN"
    for observer in strat.observers:
        if isinstance(observer, bt.observers.TimeReturn):
            timereturn = []
            length = observer.lines.timereturn.__len__()
            for i in range(0, length):
                timereturn.append(observer.lines.timereturn.__getitem__(0 -(length - 1 - i)))

            std_per_minute = np.std(timereturn)
            std_annual = std_per_minute * np.sqrt(days_in_year * minutes_in_day)
            if std_annual != 0:
                sharpe = (annual_return - riskfree_rate) / std_annual
            if debug:
                stdout_log(f"std_per_minute: {std_per_minute}, std_annual: {std_annual}, sharpe: {sharpe}")

    # Metrics Table
    metrics_data = {
        "Metrics": [
            "Total Return",
            "Annualized Return",
            "Annual Return Volatility",
            "Sharpe Ratio"
        ],
        "Result": [
            f"{total_return:.8%}",
            f"{annual_return:.8%}",
            f"{std_annual:.8%}" if std_annual != "NaN" else std_annual,
            f"{sharpe:.8f}" if sharpe != "NaN" else sharpe,
        ]
    }
    metrics_df = pd.DataFrame(metrics_data)
    views.append(html.H2("Overall Metrics"))
    views.append(dash_table.DataTable(
            data=metrics_df.to_dict('records'),
            style_cell={'textAlign': 'left'},
            style_header={
                'backgroundColor': 'lightgrey',
                'fontWeight': 'bold'
            },
            style_cell_conditional=[
                {'if': {'column_id': 'Metrics'}, 'width': '50%'},
                {'if': {'column_id': 'Result'}, 'width': '50%'}
            ]
    ))

def add_portfolio_plot(strat, views, debug=False):
    # Portfolio Value
    for observer in strat.observers:
        if isinstance(observer, bt.observers.Broker):
            portfolio_values = []
            length = observer.lines.value.__len__()
            for i in range(0, length):
                portfolio_values.append(observer.lines.value.__getitem__(0 -(length - 1 - i)))
            dates = [bt.num2date(d).replace(tzinfo=pytz.utc).astimezone() for d in strat.datas[0].datetime.get(size=len(portfolio_values))]

            df = pd.DataFrame({'Date': dates, 'Portfolio Value': portfolio_values})
            if debug:
                stdout_log(f"portfolio df: {df}")
            fig = px.line(df, x='Date', y='Portfolio Value')
            views.append(html.H2("Portfolio Value(Including Cash)"))
            views.append(dcc.Graph(figure=fig))

def add_buysell_plot(strat, views, debug=False):
    # Buy/Sell Points
    market_data = strat.datas[0]
    market_data_length = len(market_data)
    market_data_df = pd.DataFrame({
        'Date': [market_data.datetime.datetime(0 - (market_data_length - 1 - i)).replace(tzinfo=pytz.utc).astimezone() for i in range(market_data_length)],
        'Open': [market_data.open[0 - (market_data_length - 1 - i)] for i in range(market_data_length)],
        'High': [market_data.high[0 - (market_data_length - 1 - i)] for i in range(market_data_length)],
        'Low': [market_data.low[0 - (market_data_length - 1 - i)] for i in range(market_data_length)],
        'Close': [market_data.close[0 - (market_data_length - 1 - i)] for i in range(market_data_length)]
    })
    if debug:
        stdout_log(f"candlestick df: {market_data_df}")
    fig = go.Figure(
        go.Candlestick(
            x = market_data_df["Date"],
            open = market_data_df["Open"],
            high = market_data_df["High"],
            low = market_data_df["Low"],
            close = market_data_df["Close"],
        )
    )
    fig.update_layout(
        xaxis_title = 'Date',
        yaxis_title = 'Price',
        xaxis_rangeslider_visible = True
    )
    for observer in strat.observers:
        if isinstance(observer, bt.observers.BuySell):
            dates = [bt.num2date(d).replace(tzinfo=pytz.utc).astimezone() for d in strat.datas[0].datetime.get(size=market_data_length)]

            # Buy Points
            length = observer.lines.buy.__len__()
            buy_prices = []
            buy_dates = []
            for i in range(0, length):
                p = observer.lines.buy.__getitem__(0 - (length - 1 - i))
                if isinstance(p, (int, float)):
                    buy_prices.append(p)
                    buy_dates.append(dates[i])
            fig.add_trace(
                go.Scatter(
                    x = buy_dates,
                    y = buy_prices,
                    mode = "markers",
                    marker = dict(symbol="triangle-up", color="blue", size=10),
                    name = "Buy Points"
                )
            )

            # Sell Points
            length = observer.lines.sell.__len__()
            sell_prices = []
            sell_dates = []
            for i in range(0, length):
                p = observer.lines.sell.__getitem__(0 - (length - 1 - i))
                if isinstance(p, (int, float)):
                    sell_prices.append(p)
                    sell_dates.append(dates[i])
            fig.add_trace(
                go.Scatter(
                    x=sell_dates, 
                    y=sell_prices, 
                    mode="markers", 
                    marker=dict(symbol="triangle-down", color="orange", size=10),
                    name="Sell Points"
                )
            )
    views.append(html.H2("Buy/Sell Points"))
    views.append(dcc.Graph(figure=fig))

def add_drawdown_plot(strat, views, debug=False):
    for observer in strat.observers:
        if isinstance(observer, bt.observers.DrawDown):
            # Drawdown
            length = observer.lines.drawdown.__len__()
            dates = [bt.num2date(d).replace(tzinfo=pytz.utc).astimezone() for d in strat.datas[0].datetime.get(size=length)]
            drawdowns = []
            for i in range(0, length):
                drawdowns.append(observer.lines.drawdown.__getitem__(0 -(length - 1 - i)))

            drawdown_df = pd.DataFrame({'Date': dates, 'Drawdown': drawdowns})
            if debug:
                stdout_log(f"drawdown df: {drawdown_df}")
            fig = px.line(drawdown_df, x='Date', y='Drawdown')
            views.append(html.H2("Drawdown"))
            views.append(dcc.Graph(figure=fig))

def add_risk_exposure_plot(strat, views, debug=False):
    pass


def get_self_ip():
    addrs = psutil.net_if_addrs()
    for _, interface_addresses in addrs.items():
        for address in interface_addresses:
            if address.family == socket.AF_INET and address.address.startswith('192.168.25.'):
                return address.address

def show_performance(strats, riskfree_rate = 0.01, debug=False):
    for strat in strats:
        views = []
        add_metrics_plot(strat, views, riskfree_rate, debug)
        add_portfolio_plot(strat, views, debug)
        add_buysell_plot(strat, views, debug)
        add_drawdown_plot(strat, views, debug)
        add_risk_exposure_plot(strat, views, debug)

        app = dash.Dash(__name__)
        app.layout = html.Div(views)

        port = get_available_port(debug)
        if debug:
            stdout_log(f"Assigned port for user {getpass.getuser()}: {port}")

        app.run_server(host = '0.0.0.0',
            port = int(port),
            jupyter_mode = "jupyterlab",
            jupyter_server_url = f"https://strategyuser.sqdtrade.com?port={port}",
        )