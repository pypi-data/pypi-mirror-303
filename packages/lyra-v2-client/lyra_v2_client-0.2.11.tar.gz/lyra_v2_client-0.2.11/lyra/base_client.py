"""
Base Client for the lyra dex.
"""
import json
import random
import time
from datetime import datetime

import eth_abi
import requests
from eth_account.messages import encode_defunct
from rich import print
from web3 import Web3
from websocket import WebSocketConnectionClosedException, create_connection

from lyra.constants import CONTRACTS, PUBLIC_HEADERS, TEST_PRIVATE_KEY
from lyra.enums import (
    ActionType,
    CollateralAsset,
    Environment,
    InstrumentType,
    OrderSide,
    OrderStatus,
    OrderType,
    RfqStatus,
    SubaccountType,
    TimeInForce,
    UnderlyingCurrency,
)
from lyra.utils import get_logger


class BaseClient:
    """Client for the lyra dex."""

    def __init__(
        self,
        private_key: str = TEST_PRIVATE_KEY,
        env: Environment = Environment.TEST,
        logger=None,
        verbose=False,
        subaccount_id=None,
        wallet=None,
    ):
        """
        Initialize the LyraClient class.
        """
        self.verbose = verbose
        self.env = env
        self.contracts = CONTRACTS[env]
        self.logger = logger or get_logger()
        self.web3_client = Web3()
        self.signer = self.web3_client.eth.account.from_key(private_key)
        self.wallet = self.signer.address if not wallet else wallet
        print(f"Signing address: {self.signer.address}")
        if wallet:
            print(f"Using wallet: {wallet}")
        if not subaccount_id:
            self.subaccount_id = self.fetch_subaccounts()['subaccount_ids'][0]
        else:
            self.subaccount_id = subaccount_id
        print(f"Using subaccount id: {self.subaccount_id}")

    def sign_authentication_header(self):
        timestamp = str(int(time.time() * 1000))
        msg = encode_defunct(
            text=timestamp,
        )
        signature = self.web3_client.eth.account.sign_message(
            msg, private_key=self.signer._private_key
        ).signature.hex()  # pylint: disable=protected-access
        return {
            'wallet': self.wallet,
            'timestamp': str(timestamp),
            'signature': signature,
        }

    def connect_ws(self):
        ws = create_connection(self.contracts['WS_ADDRESS'], enable_multithread=True, timeout=60)
        return ws

    def create_account(self, wallet):
        """Call the create account endpoint."""
        payload = {"wallet": wallet}
        url = f"{self.contracts['BASE_URL']}/public/create_account"
        result = requests.post(
            headers=PUBLIC_HEADERS,
            url=url,
            json=payload,
        )
        result_code = json.loads(result.content)

        if "error" in result_code:
            raise Exception(result_code["error"])
        return True

    def fetch_instruments(
        self,
        expired=False,
        instrument_type: InstrumentType = InstrumentType.PERP,
        currency: UnderlyingCurrency = UnderlyingCurrency.BTC,
    ):
        """
        Return the tickers.
        First fetch all instrucments
        Then get the ticket for all instruments.
        """
        url = f"{self.contracts['BASE_URL']}/public/get_instruments"
        payload = {
            "expired": expired,
            "instrument_type": instrument_type.value,
            "currency": currency.name,
        }
        response = requests.post(url, json=payload, headers=PUBLIC_HEADERS)
        results = response.json()["result"]
        return results

    def fetch_subaccounts(self):
        """
        Returns the subaccounts for a given wallet
        """
        url = f"{self.contracts['BASE_URL']}/private/get_subaccounts"
        payload = {"wallet": self.wallet}
        headers = self._create_signature_headers()
        response = requests.post(url, json=payload, headers=headers)
        results = json.loads(response.content)["result"]
        return results

    def fetch_subaccount(self, subaccount_id):
        """
        Returns information for a given subaccount
        """
        url = f"{self.contracts['BASE_URL']}/private/get_subaccount"
        payload = {"subaccount_id": subaccount_id}
        headers = self._create_signature_headers()
        response = requests.post(url, json=payload, headers=headers)
        results = response.json()["result"]
        return results

    def create_order(
        self,
        price,
        amount,
        instrument_name: str,
        reduce_only=False,
        side: OrderSide = OrderSide.BUY,
        order_type: OrderType = OrderType.LIMIT,
        time_in_force: TimeInForce = TimeInForce.GTC,
    ):
        """
        Create the order.
        """
        if side.name.upper() not in OrderSide.__members__:
            raise Exception(f"Invalid side {side}")
        order = self._define_order(
            instrument_name=instrument_name,
            price=price,
            amount=amount,
            side=side,
        )
        _currency = UnderlyingCurrency[instrument_name.split("-")[0]]
        if instrument_name.split("-")[1] == "PERP":
            instruments = self.fetch_instruments(instrument_type=InstrumentType.PERP, currency=_currency)
            instruments = {i['instrument_name']: i for i in instruments}
            base_asset_sub_id = instruments[instrument_name]['base_asset_sub_id']
            instrument_type = InstrumentType.PERP
        else:
            instruments = self.fetch_instruments(instrument_type=InstrumentType.OPTION, currency=_currency)
            instruments = {i['instrument_name']: i for i in instruments}
            base_asset_sub_id = instruments[instrument_name]['base_asset_sub_id']
            instrument_type = InstrumentType.OPTION

        signed_order = self._sign_order(order, base_asset_sub_id, instrument_type, _currency)
        response = self.submit_order(signed_order)
        return response

    def _define_order(
        self,
        instrument_name: str,
        price: float,
        amount: float,
        side: OrderSide,
        time_in_force: TimeInForce = TimeInForce.GTC,
    ):
        """
        Define the order, in preparation for encoding and signing
        """
        ts = int(datetime.now().timestamp() * 1000)
        return {
            'instrument_name': instrument_name,
            'subaccount_id': self.subaccount_id,
            'direction': side.name.lower(),
            'limit_price': price,
            'amount': amount,
            'signature_expiry_sec': int(ts) + 3000,
            'max_fee': '200.01',
            'nonce': int(f"{int(ts)}{random.randint(100, 999)}"),
            'signer': self.signer.address,
            'order_type': 'limit',
            'mmp': False,
            'time_in_force': time_in_force.value,
            'signature': 'filled_in_below',
        }

    def submit_order(self, order):
        id = str(int(time.time()))
        self.ws.send(json.dumps({'method': 'private/order', 'params': order, 'id': id}))
        while True:
            message = json.loads(self.ws.recv())
            if message['id'] == id:
                try:
                    return message['result']['order']
                except KeyError as error:
                    print(message)
                    raise Exception(f"Unable to submit order {message}") from error

    def _encode_trade_data(self, order, base_asset_sub_id, instrument_type, currency):
        encoded_data = eth_abi.encode(
            ['address', 'uint256', 'int256', 'int256', 'uint256', 'uint256', 'bool'],
            [
                self.contracts[f'{currency.name}_{instrument_type.name}_ADDRESS'],
                int(base_asset_sub_id),
                self.web3_client.to_wei(order['limit_price'], 'ether'),
                self.web3_client.to_wei(order['amount'], 'ether'),
                self.web3_client.to_wei(order['max_fee'], 'ether'),
                order['subaccount_id'],
                order['direction'] == 'buy',
            ],
        )

        return self.web3_client.keccak(encoded_data)

    def _sign_order(self, order, base_asset_sub_id, instrument_type, currency):
        trade_module_data = self._encode_trade_data(order, base_asset_sub_id, instrument_type, currency)
        encoded_action_hash = eth_abi.encode(
            ['bytes32', 'uint256', 'uint256', 'address', 'bytes32', 'uint256', 'address', 'address'],
            [
                bytes.fromhex(self.contracts['ACTION_TYPEHASH'][2:]),
                order['subaccount_id'],
                order['nonce'],
                self.contracts['TRADE_MODULE_ADDRESS'],
                trade_module_data,
                order['signature_expiry_sec'],
                self.wallet,
                order['signer'],
            ],
        )

        action_hash = self.web3_client.keccak(encoded_action_hash)
        encoded_typed_data_hash = "".join(['0x1901', self.contracts['DOMAIN_SEPARATOR'][2:], action_hash.hex()[2:]])
        typed_data_hash = self.web3_client.keccak(hexstr=encoded_typed_data_hash)
        order['signature'] = self.signer.signHash(typed_data_hash).signature.hex()
        return order

    def _sign_quote(self, quote):
        """
        Sign the quote
        """
        rfq_module_data = self._encode_quote_data(quote)
        return self._sign_quote_data(quote, rfq_module_data)

    def _encode_quote_data(self, quote, underlying_currency: UnderlyingCurrency = UnderlyingCurrency.ETH):
        """
        Convert the quote to encoded data.
        """
        instruments = self.fetch_instruments(instrument_type=InstrumentType.OPTION, currency=underlying_currency)
        ledgs_to_subids = {i['instrument_name']: i['base_asset_sub_id'] for i in instruments}
        dir_sign = 1 if quote['direction'] == 'buy' else -1
        quote['price'] = '10'

        def encode_leg(leg):
            print(quote)
            sub_id = ledgs_to_subids[leg['instrument_name']]
            leg_sign = 1 if leg['direction'] == 'buy' else -1
            signed_amount = self.web3_client.to_wei(leg['amount'], 'ether') * leg_sign * dir_sign
            return [
                self.contracts[f"{underlying_currency.name}_OPTION_ADDRESS"],
                sub_id,
                self.web3_client.to_wei(quote['price'], 'ether'),
                signed_amount,
            ]

        encoded_legs = [encode_leg(leg) for leg in quote['legs']]
        rfq_data = [self.web3_client.to_wei(quote['max_fee'], 'ether'), encoded_legs]

        encoded_data = eth_abi.encode(
            # ['uint256(address,uint256,uint256,int256)[]'],
            [
                'uint256',
                'address',
                'uint256',
                'int256',
            ],
            [rfq_data],
        )
        return self.web3_client.keccak(encoded_data)

    @property
    def ws(self):
        if not hasattr(self, '_ws'):
            self._ws = self.connect_ws()
        if not self._ws.connected:
            self._ws = self.connect_ws()
        return self._ws

    def login_client(
        self,
        retries=3,
    ):
        login_request = {
            'method': 'public/login',
            'params': self.sign_authentication_header(),
            'id': str(int(time.time())),
        }
        try:
            self.ws.send(json.dumps(login_request))
            # we need to wait for the response
            while True:
                message = json.loads(self.ws.recv())
                if message['id'] == login_request['id']:
                    if "result" not in message:
                        raise Exception(f"Unable to login {message}")
                    break
        except (WebSocketConnectionClosedException, Exception) as error:
            if retries:
                time.sleep(1)
                self.login_client(retries=retries - 1)
            raise error

    def fetch_ticker(self, instrument_name):
        """
        Fetch the ticker for a given instrument name.
        """
        url = f"{self.contracts['BASE_URL']}/public/get_ticker"
        payload = {"instrument_name": instrument_name}
        response = requests.post(url, json=payload, headers=PUBLIC_HEADERS)
        results = json.loads(response.content)["result"]
        return results

    def fetch_orders(
        self,
        instrument_name: str = None,
        label: str = None,
        page: int = 1,
        page_size: int = 100,
        status: OrderStatus = None,
    ):
        """
        Fetch the orders for a given instrument name.
        """
        url = f"{self.contracts['BASE_URL']}/private/get_orders"
        payload = {"instrument_name": instrument_name, "subaccount_id": self.subaccount_id}
        for key, value in {"label": label, "page": page, "page_size": page_size, "status": status}.items():
            if value:
                payload[key] = value
        headers = self._create_signature_headers()
        response = requests.post(url, json=payload, headers=headers)
        results = response.json()["result"]['orders']
        return results

    def cancel(self, order_id, instrument_name):
        """
        Cancel an order
        """

        id = str(int(time.time()))
        payload = {"order_id": order_id, "subaccount_id": self.subaccount_id, "instrument_name": instrument_name}
        self.ws.send(json.dumps({'method': 'private/cancel', 'params': payload, 'id': id}))
        while True:
            message = json.loads(self.ws.recv())
            if message['id'] == id:
                return message['result']

    def cancel_all(self):
        """
        Cancel all orders
        """
        id = str(int(time.time()))
        payload = {"subaccount_id": self.subaccount_id}
        self.login_client()
        self.ws.send(json.dumps({'method': 'private/cancel_all', 'params': payload, 'id': id}))
        while True:
            message = json.loads(self.ws.recv())
            if message['id'] == id:
                return message['result']

    def get_positions(self):
        """
        Get positions
        """
        url = f"{self.contracts['BASE_URL']}/private/get_positions"
        payload = {"subaccount_id": self.subaccount_id}
        headers = self._create_signature_headers()
        response = requests.post(url, json=payload, headers=headers)
        results = response.json()["result"]['positions']
        return results

    def get_collaterals(self):
        """
        Get collaterals
        """
        url = f"{self.contracts['BASE_URL']}/private/get_collaterals"
        payload = {"subaccount_id": self.subaccount_id}
        headers = self._create_signature_headers()
        response = requests.post(url, json=payload, headers=headers)
        results = response.json()["result"]['collaterals']
        return results.pop()

    def fetch_tickers(
        self,
        instrument_type: InstrumentType = InstrumentType.OPTION,
        currency: UnderlyingCurrency = UnderlyingCurrency.BTC,
    ):
        """
        Fetch tickers using the ws connection
        """
        instruments = self.fetch_instruments(instrument_type=instrument_type, currency=currency)
        instrument_names = [i['instrument_name'] for i in instruments]
        id_base = str(int(time.time()))
        ids_to_instrument_names = {
            f'{id_base}_{enumerate}': instrument_name for enumerate, instrument_name in enumerate(instrument_names)
        }
        for id, instrument_name in ids_to_instrument_names.items():
            payload = {"instrument_name": instrument_name}
            self.ws.send(json.dumps({'method': 'public/get_ticker', 'params': payload, 'id': id}))
            time.sleep(0.05)  # otherwise we get rate limited...
        results = {}
        while ids_to_instrument_names:
            message = json.loads(self.ws.recv())
            if message['id'] in ids_to_instrument_names:
                results[message['result']['instrument_name']] = message['result']
                del ids_to_instrument_names[message['id']]
        return results

    def create_subaccount(
        self,
        amount=0,
        subaccount_type: SubaccountType = SubaccountType.STANDARD,
        collateral_asset: CollateralAsset = CollateralAsset.USDC,
        underlying_currency: UnderlyingCurrency = UnderlyingCurrency.ETH,
    ):
        """
        Create a subaccount.
        """
        url = f"{self.contracts['BASE_URL']}/private/create_subaccount"
        _, nonce, expiration = self.get_nonce_and_signature_expiry()
        if subaccount_type is SubaccountType.STANDARD:
            contract_key = f"{subaccount_type.name}_RISK_MANAGER_ADDRESS"
        elif subaccount_type is SubaccountType.PORTFOLIO:
            if not collateral_asset:
                raise Exception("Underlying currency must be provided for portfolio subaccounts")
            contract_key = f"{underlying_currency.name}_{subaccount_type.name}_RISK_MANAGER_ADDRESS"
        else:
            raise Exception(f"Invalid subaccount type {subaccount_type}")
        payload = {
            "amount": f"{amount}",
            "asset_name": collateral_asset.name,
            "margin_type": "SM" if subaccount_type is SubaccountType.STANDARD else "PM",
            'nonce': nonce,
            "signature": "string",
            "signature_expiry_sec": expiration,
            "signer": self.signer.address,
            "wallet": self.wallet,
        }
        if subaccount_type is SubaccountType.PORTFOLIO:
            payload['currency'] = underlying_currency.name
        encoded_deposit_data = self._encode_deposit_data(
            amount=amount,
            contract_key=contract_key,
        )
        action_hash = self._generate_action_hash(
            subaccount_id=0,  # as we are depositing to a new subaccount.
            nonce=nonce,
            expiration=expiration,
            encoded_deposit_data=encoded_deposit_data,
        )

        typed_data_hash = self._generate_typed_data_hash(
            action_hash=action_hash,
        )

        signature = self.signer.signHash(typed_data_hash).signature.hex()
        payload['signature'] = signature
        print(f"Payload: {payload}")

        headers = self._create_signature_headers()
        response = requests.post(url, json=payload, headers=headers)

        if "error" in response.json():
            raise Exception(response.json()["error"])
        print(response.text)
        if "result" not in response.json():
            raise Exception(f"Unable to create subaccount {response.json()}")
        return response.json()["result"]

    def _encode_deposit_data(self, amount: int, contract_key: str):
        """Encode the deposit data"""

        encoded_data = eth_abi.encode(
            ['uint256', 'address', 'address'],
            [
                int(amount * 1e6),
                self.contracts["CASH_ASSET"],
                self.contracts[contract_key],
            ],
        )
        print(f"Encoded data: {encoded_data}")
        return self.web3_client.keccak(encoded_data)

    def get_nonce_and_signature_expiry(self):
        """
        Returns the nonce and signature expiry
        """
        ts = int(datetime.now().timestamp() * 1000)
        nonce = int(f"{int(ts)}{random.randint(100, 999)}")
        expiration = int(ts) + 6000
        return ts, nonce, expiration

    def _generate_typed_data_hash(
        self,
        action_hash: bytes,
    ):
        """Generate the typed data hash."""

        encoded_typed_data_hash = "".join(['0x1901', self.contracts['DOMAIN_SEPARATOR'][2:], action_hash.hex()[2:]])
        typed_data_hash = self.web3_client.keccak(hexstr=encoded_typed_data_hash)
        return typed_data_hash

    def transfer_collateral(self, amount: int, to: str, asset: CollateralAsset):
        """
        Transfer collateral
        """

        ts = int(datetime.now().timestamp() * 1000)
        nonce = int(f"{int(ts)}{random.randint(100, 499)}")
        nonce_2 = int(f"{int(ts)}{random.randint(500, 999)}")
        expiration = int(datetime.now().timestamp() + 10000)

        url = f"{self.contracts['BASE_URL']}/private/transfer_erc20"
        _, nonce, expiration = self.get_nonce_and_signature_expiry()
        transfer = {
            "address": self.contracts["CASH_ASSET"],
            "amount": int(amount),
            "sub_id": 0,
        }
        print(f"Transfering to {to} amount {amount} asset {asset.name}")

        encoded_data = self.encode_transfer(
            amount=amount,
            to=to,
        )

        action_hash_1 = self._generate_action_hash(
            subaccount_id=self.subaccount_id,
            nonce=nonce,
            expiration=expiration,
            encoded_deposit_data=encoded_data,
            action_type=ActionType.TRANSFER,
        )

        from_signed_action_hash = self._generate_signed_action(
            action_hash=action_hash_1,
            nonce=nonce,
            expiration=expiration,
        )

        print(f"from_signed_action_hash: {from_signed_action_hash}")
        print(f"From action hash: {action_hash_1.hex()}")

        action_hash_2 = self._generate_action_hash(
            subaccount_id=to,
            nonce=nonce_2,
            expiration=expiration,
            encoded_deposit_data=self.web3_client.keccak(bytes.fromhex('')),
            action_type=ActionType.TRANSFER,
        )
        to_signed_action_hash = self._generate_signed_action(
            action_hash=action_hash_2,
            nonce=nonce_2,
            expiration=expiration,
        )

        print(f"To action hash: {action_hash_2.hex()}")
        print(f"To signed action hash: {to_signed_action_hash}")
        payload = {
            "subaccount_id": self.subaccount_id,
            "recipient_subaccount_id": to,
            "sender_details": {
                "nonce": nonce,
                "signature": "string",
                "signature_expiry_sec": expiration,
                "signer": self.signer.address,
            },
            "recipient_details": {
                "nonce": nonce_2,
                "signature": "string",
                "signature_expiry_sec": expiration,
                "signer": self.signer.address,
            },
            "transfer": transfer,
        }
        payload['sender_details']['signature'] = from_signed_action_hash['signature']
        payload['recipient_details']['signature'] = to_signed_action_hash['signature']

        print(payload)
        headers = self._create_signature_headers()
        response = requests.post(url, json=payload, headers=headers)

        print(response.json())

        if "error" in response.json():
            raise Exception(response.json()["error"])
        if "result" not in response.json():
            raise Exception(f"Unable to transfer collateral {response.json()}")
        return response.json()["result"]

    def encode_transfer(self, amount: int, to: str, asset_sub_id=0, signature_expiry=300):
        """
        Encode the transfer
        const encoder = ethers.AbiCoder.defaultAbiCoder();
        const TransferDataABI = ['(uint256,address,(address,uint256,int256)[])'];
        const signature_expiry = getUTCEpochSec() + 300;

        const fromTransfers = [
          [
            assetAddress,
            assetSubId,
            ethers.parseUnits(amount, 18), // Amount in wei
          ],
        ];

        const fromTransferData = [
          toAccount.subaccountId,
          "0x0000000000000000000000000000000000000000", // manager (if new account)`
          fromTransfers,
        ];

        const fromEncodedData = encoder.encode(TransferDataABI, [fromTransferData]);
        """
        transfer_data_abi = ["(uint256,address,(address,uint256,int256)[])"]

        from_transfers = [
            [
                self.contracts["CASH_ASSET"],
                asset_sub_id,
                self.web3_client.to_wei(amount, 'ether'),
            ]
        ]

        from_transfer_data = [
            int(to),
            "0x0000000000000000000000000000000000000000",
            from_transfers,
        ]

        from_encoded_data = eth_abi.encode(transfer_data_abi, [from_transfer_data])
        print(f"From transfers: {from_transfers}")
        print(f"From transfer data: {from_transfer_data}")
        print(f"From encoded data: {from_encoded_data.hex()}")

        # need to add the signature expiry
        return self.web3_client.keccak(from_encoded_data)

    def _generate_action_hash(
        self,
        subaccount_id: int,
        nonce: int,
        expiration: int,
        encoded_deposit_data: bytes,
        action_type: ActionType = ActionType.DEPOSIT,
    ):
        """Handle the deposit to a new subaccount."""
        encoded_action_hash = eth_abi.encode(
            ['bytes32', 'uint256', 'uint256', 'address', 'bytes32', 'uint256', 'address', 'address'],
            [
                bytes.fromhex(self.contracts['ACTION_TYPEHASH'][2:]),
                subaccount_id,
                nonce,
                self.contracts[f'{action_type.name}_MODULE_ADDRESS'],
                encoded_deposit_data,
                expiration,
                self.wallet,
                self.signer.address,
            ],
        )
        return self.web3_client.keccak(encoded_action_hash)

    def _generate_signed_action(self, action_hash: bytes, nonce: int, expiration: int):
        """Generate the signed action."""
        encoded_typed_data_hash = "".join(['0x1901', self.contracts['DOMAIN_SEPARATOR'][2:], action_hash.hex()[2:]])
        typed_data_hash = self.web3_client.keccak(hexstr=encoded_typed_data_hash)
        signature = self.signer.signHash(typed_data_hash).signature.hex()
        return {
            "nonce": nonce,
            "signature": signature,
            "signature_expiry_sec": expiration,
            "signer": self.signer.address,
        }

    def get_mmp_config(self, subaccount_id: int, currency: UnderlyingCurrency = None):
        """Get the mmp config."""
        url = f"{self.contracts['BASE_URL']}/private/get_mmp_config"
        payload = {"subaccount_id": self.subaccount_id}
        if currency:
            payload['currency'] = currency.name
        headers = self._create_signature_headers()
        response = requests.post(url, json=payload, headers=headers)
        results = response.json()["result"]
        return results

    def set_mmp_config(
        self,
        subaccount_id,
        currency: UnderlyingCurrency,
        mmp_frozen_time: int,
        mmp_interval: int,
        mmp_amount_limit: str,
        mmp_delta_limit: str,
    ):
        """Set the mmp config."""
        url = f"{self.contracts['BASE_URL']}/private/set_mmp_config"
        payload = {
            "subaccount_id": subaccount_id,
            "currency": currency.name,
            "mmp_frozen_time": mmp_frozen_time,
            "mmp_interval": mmp_interval,
            "mmp_amount_limit": mmp_amount_limit,
            "mmp_delta_limit": mmp_delta_limit,
        }
        headers = self._create_signature_headers()
        response = requests.post(url, json=payload, headers=headers)
        results = response.json()["result"]
        return results

    def send_rfq(self, rfq):
        """Send an RFQ."""
        url = f"{self.contracts['BASE_URL']}/private/send_rfq"
        headers = self._create_signature_headers()
        response = requests.post(url, json=rfq, headers=headers)
        results = response.json()["result"]
        return results

    def poll_rfqs(self):
        """
        Poll RFQs.
            type RfqResponse = {
              subaccount_id: number,
              creation_timestamp: number,
              last_update_timestamp: number,
              status: string,
              cancel_reason: string,
              rfq_id: string,
              valid_until: number,
              legs: Array<RfqLeg>
            }
        """
        url = f"{self.contracts['BASE_URL']}/private/poll_rfqs"
        headers = self._create_signature_headers()
        params = {
            "subaccount_id": self.subaccount_id,
            "status": RfqStatus.OPEN.value,
        }
        response = requests.post(url, headers=headers, params=params)
        results = response.json()["result"]
        return results

    def send_quote(self, quote):
        """Send a quote."""
        url = f"{self.contracts['BASE_URL']}/private/send_quote"
        headers = self._create_signature_headers()
        response = requests.post(url, json=quote, headers=headers)
        results = response.json()["result"]
        return results

    #   pricedLegs[0].price = direction == 'buy' ? '160' : '180';
    #   pricedLegs[1].price = direction == 'buy' ? '70' : '50';
    #   return {
    #     subaccount_id: subaccount_id_maker,
    #     rfq_id: rfq_response.rfq_id,
    #     legs: pricedLegs,
    #     direction: direction,
    #     max_fee: '10',
    #     nonce: Number(`${Date.now()}${Math.round(Math.random() * 999)}`),
    #     signer: wallet.address,
    #     signature_expiry_sec: Math.floor(Date.now() / 1000 + 350),
    #     signature: "filled_in_below"
    #   };
    # }

    def create_quote_object(
        self,
        rfq_id,
        legs,
        direction,
    ):
        """Create a quote object."""
        _, nonce, expiration = self.get_nonce_and_signature_expiry()
        return {
            "subaccount_id": self.subaccount_id,
            "rfq_id": rfq_id,
            "legs": legs,
            "direction": direction,
            "max_fee": '10.0',
            "nonce": nonce,
            "signer": self.signer.address,
            "signature_expiry_sec": expiration,
            "signature": "filled_in_below",
        }
