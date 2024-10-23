import os
import json
import asyncio
import websockets
from websockets.exceptions import InvalidStatusCode, ConnectionClosedError
import http.client
import ssl

# Define Auth Urls

AUTH_STEP_1_TEST = 'https://uat.flexfills.com/auth/login'
AUTH_STEP_2_TEST = 'https://uat.flexfills.com/auth/auth/jwt/clients/{}/token'

AUTH_STEP_1_PROD = 'https://flexfills.com/auth/login'
AUTH_STEP_2_PROD = 'https://flexfills.com/auth/auth/jwt/clients/{}/token'

BASE_DOMAIN_TEST = "uat.flexfills.com"
BASE_DOMAIN_PROD = "flexfills.com"

# Define public and private channels

CH_ASSET_LIST = 'ASSET_LIST'
CH_INSTRUMENT_LIST = 'INSTRUMENT_LIST'
CH_ORDER_BOOK_PUBLIC = 'ORDER_BOOK_PUBLIC'
CH_TRADE_PUBLIC = 'TRADE_PUBLIC'
CH_ACTIVE_SUBSCRIPTIONS = 'ACTIVE_SUBSCRIPTIONS'

CH_PRV_BALANCE = 'BALANCE'
CH_PRV_TRADE_PRIVATE = 'TRADE_PRIVATE'
CH_PRV_TRADE_POSITIONS = 'TRADE_POSITIONS'

# Define available constants

ORDER_DIRECTIONS = ['SELL', 'BUY']
ORDER_TYPES = ['MARKET', 'LIMIT', 'POST_ONLY']
TIME_IN_FORCES = ['GTC', 'GTD', 'GTT', 'FOK', 'IOC']


class FlexfillsConnectException(Exception):
    "Raised when unauthorized access to Flexfills API"
    pass


class FlexfillsParamsException(Exception):
    "Raised when parameters are not valid"
    pass


def initialize(username, password, is_test=False):
    auth_token = get_auth_token(username, password, is_test)

    if not auth_token:
        raise Exception('Flexfills API authentication failed!')

    flexfills = FlexfillsApi(auth_token, is_test)

    return flexfills


def get_auth_token(username, password, is_test=False):
    conn_url = BASE_DOMAIN_TEST if is_test else BASE_DOMAIN_PROD
    # context = ssl.create_default_context()
    context = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(conn_url, context=context)

    payload = f"username={username}&password={password}"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Send first request to get JSESSIONID

    conn.request("POST", "/auth/login", payload, headers)
    session_res = conn.getresponse()
    session_data = session_res.read()

    cookies = session_res.getheader('Set-Cookie')

    jsession_id = None
    if cookies:
        for cookie in cookies.split(';'):
            if 'JSESSIONID' in cookie:
                jsession_id = cookie.strip()

    if not jsession_id:
        raise Exception('Could not authenticate.')

    payload = ''
    headers = {
        'Accept': '*/*',
        'Cookie': jsession_id,
        'clientSecret': password,
    }

    # Send second request to get auth token

    conn.request(
        "POST", f"/auth/auth/jwt/clients/{username}/token", payload, headers)
    token_res = conn.getresponse()
    token_data = token_res.read()

    if token_res.status != 200 or not token_data:
        raise Exception('Could not authenticate.')

    conn.close()

    auth_token = token_data.decode("utf-8")

    return auth_token


class FlexfillsApi:
    """
    Flex Fills provides Quotes and Limit Order book for SPOT Crypto.
    """

    WS_URL_TEST = 'wss://uat.flexfills.com/exchange/ws'

    WS_URL_PROD = 'wss://flexfills.com/exchange/ws'

    def __init__(self, auth_token, is_test=False):
        self._is_test = is_test
        self._socket_url = self.WS_URL_TEST if self._is_test else self.WS_URL_PROD
        self._auth_token = auth_token
        self._auth_header = {"Authorization": self._auth_token}

        # SSL context for websockets connection
        self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE

    def get_asset_list(self):
        """ Provides a list of supported assets and their trading specifications.

        Parameters:
        ----------

        Returns:
        -------

        """

        message = {
            "command": "GET",
            "channel": CH_ASSET_LIST
        }

        resp = asyncio.get_event_loop().run_until_complete(self._send_message(message))

        return resp

    def get_instrument_list(self):
        """ Provides a list of supported Instruments and their trading specifications.
        When no symbol is provided, all Instruments are returned, a specific Instrument is provided only selected is returned.

        Parameters:
        ----------

        Returns:
        -------

        """

        message = {
            "command": "GET",
            "channel": CH_INSTRUMENT_LIST
        }

        resp = asyncio.get_event_loop().run_until_complete(self._send_message(message))

        return resp

    def subscribe_order_books(self, instruments, callback=None):
        """ Provides streaming services a trading book (public trades) for selected symbol.
        Once subscribed updates will be pushed to user as they appear at FlexFills.

        Parameters:
        ----------

        Returns:
        -------

        """

        message = {
            "command": "SUBSCRIBE",
            "channel": CH_ORDER_BOOK_PUBLIC,
            "channelArgs": [{"name": "instrument",
                             "value": f"[{', '.join(instruments)}]"}]
        }

        resp = asyncio.get_event_loop().run_until_complete(
            self._send_message(message, callback))

        return resp

    def unsubscribe_order_books(self, instruments):
        """ Provides streaming services a trading book (public trades) for selected symbol.
        Once subscribed updates will be pushed to user as they appear at FlexFills.

        Parameters:
        ----------

        Returns:
        -------

        """

        message = {
            "command": "UNSUBSCRIBE",
            "channel": CH_ORDER_BOOK_PUBLIC,
            "channelArgs": [{"name": "instrument",
                             "value": f"[{', '.join(instruments)}]"}]
        }

        resp = asyncio.get_event_loop().run_until_complete(self._send_message(message))

        return resp

    def trade_book_public(self, instruments, callback=None):
        """ Provides streaming services a trading book (public trades) for selected symbol.
        Once subscribed updates will be pushed to user as they appear at FlexFills.

        Parameters:
        ----------

        Returns:
        -------

        """

        message = {
            "command": "SUBSCRIBE",
            "channel": CH_TRADE_PUBLIC,
            "channelArgs": [{"name": "instrument",
                            "value": f"[{', '.join(instruments)}]"}]
        }

        resp = asyncio.get_event_loop().run_until_complete(
            self._send_message(message, callback))

        return resp

    def get_balance(self, currencies):
        """ Private trades subscription will provide a snapshot of
        currently open ACTIVE orders and then updates via WebSocket.

        Parameters:
        ----------

        Returns:
        -------
        Return open ACTIVE orders.

        """

        message = {
            "command": "SUBSCRIBE",
            "signature": self._auth_token,
            "channelArgs": [{"name": "currency", "value": f"[{', '.join(currencies)}]"}],
            "channel": CH_PRV_BALANCE
        }

        resp = asyncio.get_event_loop().run_until_complete(self._send_message(message))

        return resp

    def get_private_trades(self, instruments, callback=None):
        """ Private trades subscription will provide a snapshot of
        currently open ACTIVE orders and then updates via WebSocket.

        Parameters:
        ----------

        Returns:
        -------
        Return open ACTIVE orders.

        """

        message = {
            "command": "SUBSCRIBE",
            "signature": self._auth_token,
            "channel": CH_PRV_TRADE_PRIVATE,
            "channelArgs": [
                {
                    "name": "instrument",
                    "value": f"[{', '.join(instruments)}]"
                }
            ]
        }

        resp = asyncio.get_event_loop().run_until_complete(
            self._send_message(message, callback))

        return resp

    def get_open_orders_list(self, instruments=None):
        """ Get current list of open orders. One time request/response.

        Parameters:
        ----------

        Returns:
        -------
        Return current list of open orders.

        """

        message = {
            "command": "GET",
            "signature": self._auth_token,
            "channel": CH_PRV_TRADE_PRIVATE,
        }

        channel_args = [{
            "name": "category",
            "value": "ACTIVE_ORDERS"
        }]

        if instruments:
            channel_args.append({
                "name": "instrument",
                "value": f"[{', '.join(instruments)}]"
            })

        message["channelArgs"] = channel_args

        resp = asyncio.get_event_loop().run_until_complete(
            self._send_message(message))

        return resp

    def create_order(self, order_datas):
        """ Send new order

        Parameters:
        ----------
        order_data: List of order objects, including globalInstrumentCd, clientOrderId, direction
        orderType, timeInForce, price, amount

        Returns:
        -------
        Return current list of open orders.

        """

        if not order_datas:
            return None

        required_keys = ['globalInstrumentCd', 'exchange',
                         'direction', 'orderType', 'amount']

        optional_keys = ['exchangeName', 'orderSubType',
                         'price', 'clientOrderId', 'timeInForce', 'tradeSide']

        valid_datas = []
        for order_data in order_datas:
            valid_data = self._validate_payload(
                order_data, required_keys, optional_keys, 'order_data')

            valid_data['class'] = 'Order'

            if valid_data['orderType'] == 'LIMIT' and 'price' not in valid_data:
                raise FlexfillsParamsException(
                    "Price should be included in order_data.")

            valid_datas.append(valid_data)

        # Before sending the new order, request user must first be subscribed to desired pair, otherwise order will be rejected.

        subscribe_message = {
            "command": "SUBSCRIBE",
            "signature": self._auth_token,
            "channel": CH_PRV_TRADE_PRIVATE,
            "channelArgs": [
                {
                    "name": "instrument",
                    "value": f"[{str(valid_datas[0]['globalInstrumentCd'])}]"
                }
            ]
        }

        message = {
            "command": "CREATE",
            "signature": self._auth_token,
            "channel": CH_PRV_TRADE_PRIVATE,
            "data": valid_datas
        }

        resp = asyncio.get_event_loop().run_until_complete(
            self._subscribe_and_send_message(subscribe_message, message, None))

        return resp

    def cancel_order(self, order_datas):
        if not order_datas:
            return None

        required_keys = ['globalInstrumentCd', 'clientOrderId', 'direction',
                         'orderType', 'timeInForce', 'price', 'amount', 'exchange']

        valid_datas = []
        for order_data in order_datas:
            valid_data = self._validate_payload(
                order_data, required_keys, [], 'order_data')
            valid_data['class'] = "Order"
            valid_datas.append(valid_data)

        subscribe_message = {
            "command": "SUBSCRIBE",
            "signature": self._auth_token,
            "channel": CH_PRV_TRADE_PRIVATE,
            "channelArgs": [
                {
                    "name": "instrument",
                    "value": f"[{str(valid_datas[0]['globalInstrumentCd'])}]"
                }
            ]
        }

        message = {
            "command": "CANCEL",
            "signature": self._auth_token,
            "channel": CH_PRV_TRADE_PRIVATE,
            "data": valid_datas
        }

        resp = asyncio.get_event_loop().run_until_complete(
            self._subscribe_and_send_message(subscribe_message, message))

        return resp

    def modify_order(self, order_data):
        order_payload = {
            "class": "Order",
            "globalInstrumentCd": str(order_data['globalInstrumentCd']),
            "orderId": str(order_data['orderId']),
            "exchangeOrderId": str(order_data['exchangeOrderId'])
        }

        if 'price' in order_data:
            order_payload['price'] = str(order_data['price'])

        if 'amount' in order_data:
            order_payload['amount'] = str(order_data['amount'])

        message = {
            "command": "MODIFY",
            "signature": self._auth_token,
            "channel": CH_PRV_TRADE_PRIVATE,
            "data": [order_payload]
        }

        resp = asyncio.get_event_loop().run_until_complete(self._send_message(message))

        return resp

    def get_trade_history(self, date_from, date_to, instruments):
        message = {
            "command": "GET",
            "signature": self._auth_token,
            "channel": CH_PRV_TRADE_PRIVATE,
            "channelArgs": [
                {
                    "name": "category",
                    "value": "TRADES_HISTORY"
                },
                {
                    "name": "instrument",
                    "value": f"[{', '.join(instruments)}]"
                },
                {
                    "name": "date-from",
                    # "value": "2022-12-01T00:00:00"
                    "value": date_from
                },
                {
                    "name": "date-to",
                    "value": date_to
                }
            ]
        }

        resp = asyncio.get_event_loop().run_until_complete(self._send_message(message))

        return resp

    def get_order_history(self, date_from, date_to, instruments, statues):
        message = {
            "command": "GET",
            "signature": self._auth_token,
            "channel": CH_PRV_TRADE_PRIVATE,
            "channelArgs": [
                {
                    "name": "category",
                    "value": "ORDERS_HISTORY"
                },
                {
                    "name": "instrument",
                    # Example value: "[USD/ADA, ETH/BTC, BTC/USD, BTC/EUR]"
                    "value": f"[{', '.join(instruments)}]"
                },
                {
                    "name": "date-from",
                    # "value": "2022-12-01T00:00:00"
                    "value": date_from
                },
                {
                    "name": "date-to",
                    "value": date_to
                },
                {
                    "name": "status",
                    # Example value: "[COMLETED, REJECTED, PARTIALLY_FILLED, FILLED, EXPIRED]"
                    "value": f"[{', '.join(statues)}]"
                }
            ]
        }

        resp = asyncio.get_event_loop().run_until_complete(self._send_message(message))

        return resp

    def get_trade_positions(self):
        message = {
            "command": "GET",
            "channel": CH_PRV_TRADE_POSITIONS
        }

        resp = asyncio.get_event_loop().run_until_complete(self._send_message(message))

        return resp

    # Protected Methods

    async def _subscribe_and_send_message(self, subscriber, message, callback=None, is_onetime=False):
        try:
            async with websockets.connect(self._socket_url, extra_headers=self._auth_header, ssl=self.ssl_context) as websocket:
                await websocket.send(json.dumps(subscriber))

                subscribe_response = await websocket.recv()
                is_valid_subscribe, validated_subscribe_response = self._validate_response(
                    subscribe_response, subscriber)

                if validated_subscribe_response['event'] == 'ERROR':
                    return validated_subscribe_response

                datas = message.get('data')
                validated_resps = []
                _message = message

                for data in datas:
                    validated_resp = ''
                    _message['data'] = [data]

                    await websocket.send(json.dumps(_message))

                    while True:
                        response = await websocket.recv()

                        is_valid, validated_resp = self._validate_subscribe_response(
                            response, message)

                        if callback:
                            callback(validated_resp)
                        else:
                            if is_onetime is True:
                                break

                            if is_valid is True:
                                break

                    validated_resps.append(validated_resp)

                return validated_resps

        except (InvalidStatusCode, ConnectionClosedError) as e:
            print(f"Error while connecting FlexfillsApi: {str(e)}")
            raise FlexfillsConnectException

    async def _send_message(self, message, callback=None, is_onetime=False):
        try:
            async with websockets.connect(self._socket_url, extra_headers=self._auth_header, ssl=self.ssl_context) as websocket:
                await websocket.send(json.dumps(message))

                count = 0
                validated_resp = ''

                while True:
                    response = await websocket.recv()

                    is_valid, validated_resp = self._validate_response(
                        response, message)

                    if callback:
                        callback(validated_resp)
                    else:
                        if is_onetime is True:
                            break

                        if is_valid is True:
                            break

                        if count >= 10:
                            break

                        count += 1

                return validated_resp

        except (InvalidStatusCode, ConnectionClosedError) as e:
            print(f"Error while connecting FlexfillsApi: {str(e)}")
            raise FlexfillsConnectException

    def _validate_response(self, response, message):
        json_resp = json.loads(response)

        if not message or 'command' not in message:
            return True, json_resp

        # if message.get('command') == 'SUBSCRIBE':
        #     return True, json_resp

        if json_resp.get('event') == 'ERROR':
            return True, json_resp

        if json_resp.get('event') == 'ACK':
            return False, json_resp

        return True, json_resp

    def _validate_subscribe_response(self, response, message):
        json_resp = json.loads(response)

        if not message or 'command' not in message:
            return True, json_resp

        event = json_resp.get('event')

        if event == None or event == 'ERROR':
            return True, json_resp

        if event == 'ACK':
            return False, json_resp

        return False, json_resp

    def _validate_payload(self, payload, required_keys, optional_keys, data_type=''):
        valid_data = {}

        if required_keys:
            for k in required_keys:
                if k in payload:
                    valid_data[k] = str(payload.get(k))
                else:
                    raise FlexfillsParamsException(f"{k} field should be in the {
                        data_type if data_type else 'payload data'}")

        if optional_keys:
            for k in optional_keys:
                if k in payload:
                    valid_data[k] = str(payload.get(k))

        if 'direction' in payload:
            if str(payload['direction']).upper() in ORDER_DIRECTIONS:
                valid_data['direction'] = str(payload['direction']).upper()
            else:
                raise FlexfillsParamsException(
                    f"the direction field is not valid in {data_type if data_type else 'payload data'}")

        if 'orderType' in payload:
            if str(payload['orderType']).upper() in ORDER_TYPES:
                valid_data['orderType'] = str(payload['orderType']).upper()
            else:
                raise FlexfillsParamsException(
                    f"the orderType field is not valid in {data_type if data_type else 'payload data'}")

        if 'timeInForce' in payload:
            if payload.get('timeInForce') is None:
                valid_data['timeInForce'] = 'GTC'
            elif str(payload['timeInForce']).upper() in TIME_IN_FORCES:
                valid_data['timeInForce'] = str(payload['timeInForce']).upper()
            else:
                raise FlexfillsParamsException(
                    f"the timeInForce field is not valid in {data_type if data_type else 'payload data'}")

        return valid_data
