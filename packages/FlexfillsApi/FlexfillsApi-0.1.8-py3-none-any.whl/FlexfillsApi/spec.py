import os
import ccxt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import nest_asyncio
import asyncio
import logging
import functools
import platform
from flexfillsapi import initialize, FlexfillsConnectException


# Fixing RuntimeError on Windows
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Apply nest_asyncio to handle nested event loops
nest_asyncio.apply()

global_instrument_cd = 'BTC/USDT'
flexfills_exchanges = ["FLEXFILLS",
                       "BITFINEX",
                       "GEMINI",
                       "OKEX",
                       "HUOBI",
                       "GITGET",
                       "HITBTC",
                       "LMAX",
                       "BITCOM"]
flexfills_order_types = ["LIMIT", "MARKET"]

max_tries = 5
retry_delay = 5  # Seconds between reconnection attempts


# *************************************
# Decorator for handling Exceptions
# *************************************


def handleFlexfillsAPIException(max_retries=max_tries, delay=retry_delay):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0

            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except FlexfillsConnectException as e:
                    # Handling API connection error
                    attempts += 1
                    print(
                        f"Flexfills API connection was closed, retrying: {attempts}")
                    logging.warning(
                        f"Flexfills API connection was closed, retrying: {attempts}")

                    # Reset connection on FlexfillsConnectException and relogin

                    time.sleep(delay)
                    RenkoTraderApp.login_flexfills()

                except Exception as e:
                    attempts += 1
                    print(f"Failed to execute {
                        func.__name__}, retrying: {attempts}")
                    logging.warning(f"Failed to execute {
                                    func.__name__}, retrying: {attempts}")

                    time.sleep(delay)

            # Reset connection after failure and start over instead of crashing
            print(
                f"Failed after {max_retries} attempts while executing {func.__name__}. Dropping connection and starting over.")
            logging.error(
                f"Failed after {max_retries} attempts while executing {func.__name__}. Dropping connection and starting over.")

            # Drop the connection and reinitialize
            RenkoTraderApp.login_flexfills()

            # Start the process again
            return wrapper(*args, **kwargs)

        return wrapper

    return decorator_retry


class RenkoTraderApp:
    flexfills_username = ''
    flexfills_password = ''

    def __init__(self, root):
        self.root = root
        self.root.title("Live Renko Trading Strategy")

        # Initialize variables
        self.exchange = None
        self.symbol = tk.StringVar(value='BTC-PERPETUAL')
        self.amount = tk.IntVar(value=20)
        self.api_key = tk.StringVar(value='')
        self.api_secret = tk.StringVar(value='')
        self.file_path = tk.StringVar(value='F:/RENKO Trader')
        self.timeframe = tk.StringVar(value='15m')
        self.ema_span = tk.IntVar(value=6)
        self.sma_window = tk.IntVar(value=6)

        self.flexfills_user = tk.StringVar(value='')
        self.flexfills_pwd = tk.StringVar(value='')
        self.flexfills_exchange = tk.StringVar(value='FLEXFILLS')
        self.flexfills_order_type = tk.StringVar(value='LIMIT')

        self.is_running = False
        self.thread = None

        self.flexfills_api = None

        self.root.protocol("WM_DELETE_WINDOW", self.destroy_gui)

        self.create_widgets()

    @staticmethod
    def _create_widget(parent, widget_type, **options):
        return widget_type(parent, **options)

    def create_widgets(self):
        self.set_log("creating widgets...", "info")
        self.root.grid_columnconfigure(0, weight=1, uniform="flex")
        self.root.grid_columnconfigure(1, weight=1, uniform="flex")

        frame_l = self._create_widget(self.root, tk.Frame)
        frame_l.grid(row=0, column=0, padx=10, pady=10, sticky='nesw')

        # Input fields
        tk.Label(frame_l, text="API Key").grid(row=0, column=0, padx=10)
        tk.Entry(frame_l, textvariable=self.api_key).grid(row=0, column=1)

        tk.Label(frame_l, text="API Secret").grid(row=1, column=0, padx=10)
        tk.Entry(frame_l, textvariable=self.api_secret).grid(row=1, column=1)

        tk.Label(frame_l, text="Symbol").grid(row=2, column=0, padx=10)
        tk.Entry(frame_l, textvariable=self.symbol).grid(row=2, column=1)

        tk.Label(frame_l, text="Amount").grid(row=3, column=0, padx=10)
        tk.Entry(frame_l, textvariable=self.amount).grid(row=3, column=1)

        tk.Label(frame_l, text="File Path").grid(row=4, column=0, padx=10)
        tk.Entry(frame_l, textvariable=self.file_path).grid(row=4, column=1)

        tk.Label(frame_l, text="Timeframe").grid(row=5, column=0, padx=10)
        tk.Entry(frame_l, textvariable=self.timeframe).grid(row=5, column=1)

        tk.Label(frame_l, text="EMA Span").grid(row=6, column=0, padx=10)
        tk.Entry(frame_l, textvariable=self.ema_span).grid(row=6, column=1)

        tk.Label(frame_l, text="SMA Window").grid(row=7, column=0, padx=10)
        tk.Entry(frame_l, textvariable=self.sma_window).grid(row=7, column=1)

        frame_r = self._create_widget(self.root, tk.Frame)
        frame_r.grid(row=0, column=1, padx=10, pady=10, sticky='nesw')

        tk.Label(frame_r, text="Flexfills Username").grid(
            row=0, column=0, padx=10)
        tk.Entry(frame_r, textvariable=self.flexfills_user).grid(
            row=0, column=1)

        tk.Label(frame_r, text="Flexfills Password").grid(
            row=1, column=0, padx=10)
        tk.Entry(frame_r, textvariable=self.flexfills_pwd).grid(
            row=1, column=1)

        tk.Label(frame_r, text="Exchange Name").grid(row=2, column=0, padx=10)
        tk.OptionMenu(frame_r, self.flexfills_exchange, *flexfills_exchanges).grid(
            row=2, column=1, sticky='NW')

        tk.Label(frame_r, text="Order Type").grid(row=3, column=0, padx=10)
        tk.OptionMenu(frame_r, self.flexfills_order_type, *flexfills_order_types).grid(
            row=3, column=1, sticky='NW')

        # Start/Stop buttons
        self.start_button = tk.Button(
            self.root, text="Start", width=20, command=self.start)
        self.start_button.grid(row=1, column=0)

        self.stop_button = tk.Button(
            self.root, text="Stop", width=20, command=self.stop, state=tk.DISABLED)
        self.stop_button.grid(row=1, column=1)

        # Create a figure and axis for the Renko chart
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def validate_parameters(self):
        if not self.api_key.get():
            messagebox.showerror("Error", "API Key is required.")
            return False
        if not self.api_secret.get():
            messagebox.showerror("Error", "API Secret is required.")
            return False
        if not self.symbol.get():
            messagebox.showerror("Error", "Symbol is required.")
            return False
        if not self.file_path.get():
            messagebox.showerror("Error", "File Path is required.")
            return False
        if not self.timeframe.get():
            messagebox.showerror("Error", "Timeframe is required.")
            return False
        if not self.ema_span.get() > 0:
            messagebox.showerror("Error", "EMA Span must be greater than 0.")
            return False
        if not self.sma_window.get() > 0:
            messagebox.showerror("Error", "SMA Window must be greater than 0.")
            return False
        if not self.flexfills_user.get():
            messagebox.showerror("Error", "Flexfills API user is required.")
            return False
        if not self.flexfills_pwd.get():
            messagebox.showerror("Error", "Flexfills Password is required.")
            return False
        if not self.flexfills_exchange.get():
            messagebox.showerror("Error", "Flexfills Exchange is required.")
            return False
        if not self.flexfills_order_type.get():
            messagebox.showerror("Error", "Flexfills Order Type is required.")
            return False

        return True

    def init_progress_logging(self):
        # Set up logging to file and console
        log_file_path = os.path.join(self.file_path.get(), "detailed_log.txt")

        logging.basicConfig(filename=log_file_path, level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        logging.getLogger().addHandler(console)

    @classmethod
    def login_flexfills(cls):
        # Initialize FlexfillsApi
        logging.info("Initializing FlexfillsApi with provided credentials...")
        flexfills_api = initialize(
            cls.flexfills_username, cls.flexfills_password, is_test=True)
        logging.info("FlexfillsApi initialized successfully!")

        return flexfills_api

    @classmethod
    def set_flexfills_credentials(cls, user, pwd):
        cls.flexfills_username = user
        cls.flexfills_password = pwd

    def init_flexfills(self):
        # Initialize FlexfillsApi
        RenkoTraderApp.set_flexfills_credentials(
            self.flexfills_user.get(), self.flexfills_pwd.get())
        self.flexfills_api = RenkoTraderApp.login_flexfills()

    def start(self):
        if not self.validate_parameters():
            self.set_log(
                "The parameters are not valid. Process is not started", "info")
            return

        self.set_log("Start processing...", "info")
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.thread = threading.Thread(target=self.run_strategy_v2)
        self.thread.start()

    def stop(self):
        self.set_log("Stop processing...", "info")
        self.is_running = False
        if self.thread:
            self.thread.join()

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def destroy_gui(self):
        self.stop()
        self.root.destroy()

    def initialize_log_files(self):
        try:
            with open(f"{self.file_path.get()}/trades_log.csv", 'w') as f:
                f.write('Timestamp,Trade Type,Price,Amount,PnL\n')
            with open(f"{self.file_path.get()}/atr_values.csv", 'w') as f:
                f.write('Timestamp,ATR\n')
        except Exception as e:
            self.set_log(f"Error initializing log files: {e}", "error")

    def log_atr(self, timestamp, atr_value):
        try:
            with open(f"{self.file_path.get()}/atr_values.csv", 'a') as f:
                f.write(f"{timestamp},{atr_value}\n")
        except Exception as e:
            self.set_log(f"Error logging ATR value: {e}", "error")

    def log_trade(self, timestamp, trade_type, price, amount, pnl):
        try:
            with open(f"{self.file_path.get()}/trades_log.csv", 'a') as f:
                f.write(f"{timestamp},{trade_type},{price},{amount},{pnl}\n")
        except Exception as e:
            self.set_log(f"Error logging trade: {e}", "error")

    def fetch_data(self):
        timeframe = self.timeframe.get()
        limit = 90

        ohlcv = self.exchange.fetch_ohlcv(
            self.symbol.get(), timeframe, limit=limit)
        data = pd.DataFrame(
            ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
        return data

    def calculate_atr(self, data, period=14):
        data['H-L'] = abs(data['high'] - data['low'])
        data['H-PC'] = abs(data['high'] - data['close'].shift(1))
        data['L-PC'] = abs(data['low'] - data['close'].shift(1))
        tr = data[['H-L', 'H-PC', 'L-PC']].max(axis=1)
        atr = tr.rolling(window=period).mean()
        return atr

    def generate_renko(self, data, atr, atr_multiplier=1.5):
        renko_df = pd.DataFrame(
            columns=['timestamp', 'open', 'close', 'uptrend'])
        box_size = atr.iloc[-1] * atr_multiplier
        prev_close = data['close'].iloc[0]
        uptrend = True
        for i in range(1, len(data)):
            if uptrend:
                if data['close'].iloc[i] > prev_close + box_size:
                    new_row = {'timestamp': data['timestamp'].iloc[i], 'open': prev_close,
                               'close': prev_close + box_size,
                               'uptrend': True}
                    renko_df = pd.concat(
                        [renko_df, pd.DataFrame([new_row])], ignore_index=True)
                    prev_close = prev_close + box_size
                elif data['close'].iloc[i] < prev_close - box_size:
                    uptrend = False
            else:
                if data['close'].iloc[i] < prev_close - box_size:
                    new_row = {'timestamp': data['timestamp'].iloc[i], 'open': prev_close,
                               'close': prev_close - box_size,
                               'uptrend': False}
                    renko_df = pd.concat(
                        [renko_df, pd.DataFrame([new_row])], ignore_index=True)
                    prev_close = prev_close - box_size
                elif data['close'].iloc[i] > prev_close + box_size:
                    uptrend = True
        return renko_df

    def plot_renko(self, renko_df, signals):
        self.ax.clear()
        renko_df['ema'] = renko_df['close'].ewm(
            span=self.ema_span.get(), adjust=False).mean()
        renko_df['sma_of_ema'] = renko_df['ema'].rolling(
            window=self.sma_window.get()).mean()

        timestamps = mdates.date2num(renko_df['timestamp'])
        box_width = (timestamps[-1] - timestamps[0]) / len(timestamps) * 0.8

        for i in range(len(renko_df)):
            color = 'green' if renko_df['uptrend'].iloc[i] else 'red'
            self.ax.add_patch(plt.Rectangle((timestamps[i] - box_width / 2, renko_df['open'].iloc[i]),
                                            box_width, renko_df['close'].iloc[i] -
                                            renko_df['open'].iloc[i],
                                            color=color, alpha=0.7))

        self.ax.plot(renko_df['timestamp'], renko_df['ema'],
                     label='EMA (6)', color='blue', linewidth=1)
        self.ax.plot(renko_df['timestamp'], renko_df['sma_of_ema'],
                     label='SMA of EMA (6)', color='orange', linewidth=1)

        for signal in signals:
            self.ax.annotate(signal['text'], (mdates.date2num(signal['timestamp']), signal['price']),
                             xytext=(10, 10), textcoords='offset points',
                             arrowprops=dict(arrowstyle='->',
                                             color=signal['color']),
                             color=signal['color'])

        self.ax.xaxis.set_major_formatter(
            mdates.DateFormatter('%Y-%m-%d %H:%M'))
        self.ax.set_title(
            'Renko Chart with EMA, SMA of EMA, and Trading Signals')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Price')
        self.ax.legend()
        self.ax.grid()
        self.canvas.draw()

    def calculate_drawdown(self, equity_curve):
        drawdown = equity_curve - equity_curve.cummax()
        return drawdown

    def place_order(self, order_type, amount, price):
        try:
            if order_type == 'buy':
                order = self.exchange.create_market_buy_order(
                    self.symbol.get(), amount)
            elif order_type == 'sell':
                order = self.exchange.create_market_sell_order(
                    self.symbol.get(), amount)
            print(f"{order_type.upper()} order placed: {order}")
        except Exception as e:
            print(f"Error placing {order_type} order: {e}")

    @handleFlexfillsAPIException(max_tries, retry_delay)
    def place_flexfills_orders(self, orders):
        if not orders:
            logging.info("No new orders found, Skipping order creation ...")
            return

        print(f"Sending orders...")
        try:
            order_responses = self.flexfills_api.create_order(orders)

            # order_responses = self.flexfills_api.create_order(orders)

            for order_response in order_responses:
                if order_response.get('event') != 'ERROR' or order_response.get('event') != 'ACK':
                    self.set_log(f"Order created successfully: {
                                 order_response}", "info")
                else:
                    self.set_log(f"Failed to create order: {
                                 order_response}", "info")

        except Exception as e:
            self.set_log(
                f"Exception during order placement: {e}", "error")
            raise e

    @handleFlexfillsAPIException(max_tries, retry_delay)
    def cancel_flexfills_orders(self, orders):
        if not orders:
            self.set_log(
                f"No active orders found, Skipping cancel ...", "info")
            return

        print(f"Cancelling orders...")

        order_responses = self.flexfills_api.cancel_order(orders)

        if order_responses:
            for order_response in order_responses:
                if order_response.get('event') != 'ERROR' or order_response.get('event') != 'ACK':
                    self.set_log(f"Order cancelled successfully: {
                                 order_response}", "info")
                else:
                    self.set_log(f"Failed to cancel order: {
                                 order_response}", "warning")

    @handleFlexfillsAPIException(max_tries, retry_delay)
    def get_flexfills_active_orders(self, instrument):
        active_orders = []

        self.set_log("Retrieving active orders ...", "info")

        orders_response = self.flexfills_api.get_open_orders_list([instrument])

        if 'data' in orders_response:
            print(f"Active Orders:")
            active_orders_data = orders_response.get('data', [])
            for order in active_orders_data:
                self.set_log(
                    f"* Order ID: {order.get('clientOrderId')}, Price: {order.get('price')}, Amount: {order.get('amount')}", "info")

                active_orders.append(order)
        else:
            self.set_log(f"No active orders found: {orders_response}", "error")

        return active_orders

    def run_strategy(self):
        self.exchange = ccxt.deribit({
            'apiKey': self.api_key.get(),
            'secret': self.api_secret.get(),
        })

        self.initialize_log_files()

        last_processed_timestamp = None
        position = None
        entry_price = 0
        pnl = 0
        equity_curve = []
        trades = []
        signals = []

        while self.is_running:
            data = self.fetch_data()
            atr = self.calculate_atr(data)
            renko_df = self.generate_renko(data, atr)

            latest_atr = atr.iloc[-1]
            self.log_atr(datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'), latest_atr)
            self.set_log(f"Latest ATR value: {latest_atr}")

            renko_df['ema'] = renko_df['close'].ewm(
                span=self.ema_span.get(), adjust=False).mean()
            renko_df['sma_of_ema'] = renko_df['ema'].rolling(
                window=self.sma_window.get()).mean()

            for i in range(1, len(renko_df)):
                if i < len(renko_df) - 1 and renko_df['timestamp'].iloc[i] == renko_df['timestamp'].iloc[i + 1]:
                    continue

                if last_processed_timestamp is not None and renko_df['timestamp'].iloc[i] <= last_processed_timestamp:
                    continue

                if position is None:
                    if renko_df['uptrend'].iloc[i] and renko_df['close'].iloc[i] > renko_df['sma_of_ema'].iloc[i]:
                        position = 'long'
                        entry_price = renko_df['close'].iloc[i]
                        signals.append(
                            {'timestamp': renko_df['timestamp'].iloc[i], 'price': renko_df['close'].iloc[i],
                             'text': 'BUY',
                             'color': 'green'})
                        self.place_order('buy', self.amount.get(), entry_price)
                        self.set_log(f"BUY signal at {renko_df['timestamp'].iloc[i]}: {
                            renko_df['close'].iloc[i]}")
                    elif not renko_df['uptrend'].iloc[i] and renko_df['close'].iloc[i] < renko_df['sma_of_ema'].iloc[i]:
                        position = 'short'
                        entry_price = renko_df['close'].iloc[i]
                        signals.append(
                            {'timestamp': renko_df['timestamp'].iloc[i], 'price': renko_df['close'].iloc[i],
                             'text': 'SELL',
                             'color': 'red'})
                        self.place_order(
                            'sell', self.amount.get(), entry_price)
                        self.set_log(f"SELL signal at {renko_df['timestamp'].iloc[i]}: {
                            renko_df['close'].iloc[i]}")
                elif position == 'long':
                    if not renko_df['uptrend'].iloc[i]:
                        position = None
                        exit_price = renko_df['close'].iloc[i]
                        trade_pnl = exit_price - entry_price
                        pnl += trade_pnl
                        equity_curve.append(pnl)
                        trades.append(trade_pnl)
                        signals.append({'timestamp': renko_df['timestamp'].iloc[i], 'price': renko_df['close'].iloc[i],
                                        'text': 'CLOSE BUY', 'color': 'blue'})
                        self.place_order('sell', self.amount.get(), exit_price)
                        self.set_log(f"CLOSE BUY signal at {renko_df['timestamp'].iloc[i]}: {
                            renko_df['close'].iloc[i]}")
                        self.set_log(f"PnL for this trade: {
                            trade_pnl} BTC, Total PnL: {pnl} BTC")
                        self.log_trade(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'CLOSE BUY', exit_price,
                                       self.amount.get(), trade_pnl)
                elif position == 'short':
                    if renko_df['uptrend'].iloc[i]:
                        position = None
                        exit_price = renko_df['close'].iloc[i]
                        trade_pnl = entry_price - exit_price
                        pnl += trade_pnl
                        equity_curve.append(pnl)
                        trades.append(trade_pnl)
                        signals.append({'timestamp': renko_df['timestamp'].iloc[i], 'price': renko_df['close'].iloc[i],
                                        'text': 'CLOSE SELL', 'color': 'orange'})
                        self.place_order('buy', self.amount.get(), exit_price)
                        self.set_log(f"CLOSE SELL signal at {renko_df['timestamp'].iloc[i]}: {
                            renko_df['close'].iloc[i]}")
                        self.set_log(f"PnL for this trade: {
                            trade_pnl} BTC, Total PnL: {pnl} BTC")
                        self.log_trade(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'CLOSE SELL', exit_price,
                                       self.amount.get(), trade_pnl)

                last_processed_timestamp = renko_df['timestamp'].iloc[i]

            num_positive_trades = len([trade for trade in trades if trade > 0])
            num_negative_trades = len([trade for trade in trades if trade < 0])
            avg_positive_pnl = np.mean(
                [trade for trade in trades if trade > 0]) if num_positive_trades > 0 else 0
            avg_negative_pnl = np.mean(
                [trade for trade in trades if trade < 0]) if num_negative_trades > 0 else 0
            max_drawdown = self.calculate_drawdown(
                pd.Series(equity_curve)).min()

            self.set_log(f"Number of positive trades: {num_positive_trades}")
            self.set_log(f"Number of negative trades: {num_negative_trades}")
            self.set_log(f"Average PnL on positive trades: {
                         avg_positive_pnl} USDT")
            self.set_log(f"Average PnL on negative trades: {
                         avg_negative_pnl} USDT")
            self.set_log(f"Maximum drawdown: {max_drawdown} USDT")
            self.set_log(f"Latest ATR value: {latest_atr}")

            self.plot_renko(renko_df, signals)

            if not self.is_running:
                break

            time.sleep(300)

    def run_strategy_v2(self):
        self.exchange = ccxt.deribit({
            'apiKey': self.api_key.get(),
            'secret': self.api_secret.get(),
        })

        # Initialize Logging and FlexfillsApi
        self.init_progress_logging()

        try:
            self.init_flexfills()
        except Exception as e:
            self.set_log(f"Flexfills login failed: {str(e)}", "error")
            self.stop()
            messagebox.showerror(
                "Error", "Flexfills login failed. Please try again.")

            return

        self.initialize_log_files()

        last_processed_timestamp = None
        position = None
        entry_price = 0
        pnl = 0
        equity_curve = []
        trades = []
        signals = []

        flexfills_exchange = self.flexfills_exchange.get()
        flexfills_order_type = self.flexfills_order_type.get()

        while self.is_running:
            data = self.fetch_data()
            atr = self.calculate_atr(data)
            renko_df = self.generate_renko(data, atr)

            latest_atr = atr.iloc[-1]
            self.log_atr(datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'), latest_atr)
            self.set_log(f"Latest ATR value: {latest_atr}")

            renko_df['ema'] = renko_df['close'].ewm(
                span=self.ema_span.get(), adjust=False).mean()
            renko_df['sma_of_ema'] = renko_df['ema'].rolling(
                window=self.sma_window.get()).mean()

            orders = []
            for i in range(1, len(renko_df)):
                if i < len(renko_df) - 1 and renko_df['timestamp'].iloc[i] == renko_df['timestamp'].iloc[i + 1]:
                    continue

                if last_processed_timestamp is not None and renko_df['timestamp'].iloc[i] <= last_processed_timestamp:
                    continue

                amount = self.amount.get()

                if position is None:
                    if renko_df['uptrend'].iloc[i] and renko_df['close'].iloc[i] > renko_df['sma_of_ema'].iloc[i]:
                        position = 'long'
                        entry_price = renko_df['close'].iloc[i]
                        signals.append(
                            {'timestamp': renko_df['timestamp'].iloc[i], 'price': entry_price,
                             'text': 'BUY',
                             'color': 'green'})
                        # self.place_order('buy', self.amount.get(), entry_price)
                        orders.append({
                            "globalInstrumentCd": global_instrument_cd,
                            "exchange": flexfills_exchange,
                            "orderType": flexfills_order_type,
                            "direction": "BUY",
                            "timeInForce": "GTC",
                            "amount": amount,
                            "price": entry_price
                        })

                        self.set_log(f"BUY signal at {
                            renko_df['timestamp'].iloc[i]}: {entry_price}")
                    elif not renko_df['uptrend'].iloc[i] and renko_df['close'].iloc[i] < renko_df['sma_of_ema'].iloc[i]:
                        position = 'short'
                        entry_price = renko_df['close'].iloc[i]
                        signals.append(
                            {'timestamp': renko_df['timestamp'].iloc[i], 'price': entry_price,
                             'text': 'SELL',
                             'color': 'red'})
                        # self.place_order(
                        #     'sell', self.amount.get(), entry_price)
                        orders.append({
                            "globalInstrumentCd": global_instrument_cd,
                            "exchange": flexfills_exchange,
                            "orderType": flexfills_order_type,
                            "direction": "SELL",
                            "timeInForce": "GTC",
                            "amount": amount,
                            "price": entry_price
                        })

                        self.set_log(f"SELL signal at {
                            renko_df['timestamp'].iloc[i]}: {entry_price}")
                elif position == 'long':
                    if not renko_df['uptrend'].iloc[i]:
                        position = None
                        exit_price = renko_df['close'].iloc[i]
                        trade_pnl = exit_price - entry_price
                        pnl += trade_pnl
                        equity_curve.append(pnl)
                        trades.append(trade_pnl)
                        signals.append({'timestamp': renko_df['timestamp'].iloc[i], 'price': exit_price,
                                        'text': 'CLOSE BUY', 'color': 'blue'})
                        # self.place_order('sell', self.amount.get(), exit_price)
                        orders.append({
                            "globalInstrumentCd": global_instrument_cd,
                            "exchange": flexfills_exchange,
                            "orderType": flexfills_order_type,
                            "direction": "SELL",
                            "timeInForce": "GTC",
                            "amount": amount,
                            "price": exit_price
                        })

                        self.set_log(f"CLOSE BUY signal at {renko_df['timestamp'].iloc[i]}: {
                            exit_price}")
                        self.set_log(f"PnL for this trade: {
                            trade_pnl} BTC, Total PnL: {pnl} BTC")
                        self.log_trade(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'CLOSE BUY', exit_price,
                                       self.amount.get(), trade_pnl)
                elif position == 'short':
                    if renko_df['uptrend'].iloc[i]:
                        position = None
                        exit_price = renko_df['close'].iloc[i]
                        trade_pnl = entry_price - exit_price
                        pnl += trade_pnl
                        equity_curve.append(pnl)
                        trades.append(trade_pnl)
                        signals.append({'timestamp': renko_df['timestamp'].iloc[i], 'price': exit_price,
                                        'text': 'CLOSE SELL', 'color': 'orange'})
                        # self.place_order('buy', self.amount.get(), exit_price)
                        orders.append({
                            "globalInstrumentCd": global_instrument_cd,
                            "exchange": flexfills_exchange,
                            "orderType": flexfills_order_type,
                            "direction": "BUY",
                            "timeInForce": "GTC",
                            "amount": amount,
                            "price": exit_price
                        })

                        self.set_log(f"CLOSE SELL signal at {
                            renko_df['timestamp'].iloc[i]}: {exit_price}")
                        self.set_log(f"PnL for this trade: {
                            trade_pnl} BTC, Total PnL: {pnl} BTC")

                        self.log_trade(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'CLOSE SELL', exit_price,
                                       self.amount.get(), trade_pnl)

                last_processed_timestamp = renko_df['timestamp'].iloc[i]

            # Placing orders on Flexfills

            if orders:
                self.place_flexfills_orders(orders)

            num_positive_trades = len([trade for trade in trades if trade > 0])
            num_negative_trades = len([trade for trade in trades if trade < 0])
            avg_positive_pnl = np.mean(
                [trade for trade in trades if trade > 0]) if num_positive_trades > 0 else 0
            avg_negative_pnl = np.mean(
                [trade for trade in trades if trade < 0]) if num_negative_trades > 0 else 0
            max_drawdown = self.calculate_drawdown(
                pd.Series(equity_curve)).min()

            self.set_log(f"Number of positive trades: {num_positive_trades}")
            self.set_log(f"Number of negative trades: {num_negative_trades}")
            self.set_log(f"Average PnL on positive trades: {
                         avg_positive_pnl} USDT")
            self.set_log(f"Average PnL on negative trades: {
                         avg_negative_pnl} USDT")
            self.set_log(f"Maximum drawdown: {max_drawdown} USDT")
            self.set_log(f"Latest ATR value: {latest_atr}")

            self.plot_renko(renko_df, signals)

            if not self.is_running:
                break

            # time.sleep(300)
            time.sleep(10)

            # Check active orders
            active_orders = self.get_flexfills_active_orders(
                global_instrument_cd)

            # Cancel unfilled orders
            self.cancel_flexfills_orders(active_orders)

    @staticmethod
    def set_log(msg, log_type='info'):
        _msg = ''
        if log_type == 'debug':
            logging.debug(msg)
            _msg = "[DEBUG] " + msg
        if log_type == 'warning':
            logging.warning(msg)
            _msg = "[WARNING] " + msg
        if log_type == 'error':
            logging.warning(msg)
            _msg = "[ERROR] " + msg
        else:
            logging.info(msg)
            _msg = "[INFO] " + msg

        print(_msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = RenkoTraderApp(root)
    root.mainloop()
