import os
from flexfillsapi import initialize

# creds to test enviroment 100000_german, password abc123

username = '100000_german'
password = 'abc123'

instruments = ["BTC/USDT"]
currencies = ["USD", "ETH"]
statues = ["COMLETED", "REJECTED", "PARTIALLY_FILLED", "FILLED", "EXPIRED"]

date_from = "2022-12-01T00:00:00"
date_to = "2022-12-14T22:30:00"

order_data = {
    "globalInstrumentCd": "BTC/USDT",
    "exchange": "HUOBI",
    "orderType": "POST_ONLY",
    "direction": "BUY",
    "timeInForce": "GTC",
    "amount": "0.001",
    "price": "56547.42636363636"
}

direct_order_data = {
    "globalInstrumentCd": "BTC/USD",
    "exchangeName": "BITFINEX",
    "requestType": "DIRECT",
    "clientOrderId": "unique_order_id_005",
    "orderType": "LIMIT",
    "direction": "SELL",
    "timeInForce": "GTC",
    "amount": "0.001",
    "clientId": "100000",
    "price": "58000"
}

cancel_order_data = {
    "class": "Order",
    "globalInstrumentCd": "BTC/USDT",
    "clientOrderId": "11726203210011",
    "direction": "BUY",
    "orderType": "LIMIT",
    "price": "56547.42636363636",
    "amount": "0.001",
    "exchange": "HUOBI",
    "timeInForce": None
}


def get_order_books_stream(resp):
    print(resp)


def main():
    flexfills = initialize(username, password, is_test=True)
    # resp = flexfills.get_balance(["USD", "ETH"])

    # resp = flexfills.get_order_history(
    #     date_from, date_to, instruments, statues)
    # resp = flexfills.subscribe_order_books(
    #     ["BTC/USDT"], get_order_books_stream)
    # resp = flexfills.get_trade_positions()

    flexfills.subscribe_private_trades(instruments)
    resp = flexfills.create_order(order_data)
    resp = flexfills.cancel_order(cancel_order_data)
    # resp = flexfills.get_open_orders_list(['BTC/USDT'])
    # resp = flexfills.get_balance(currencies)

    # resp = flexfills.get_private_trades(instruments)

    print(resp)


if __name__ == "__main__":
    main()
