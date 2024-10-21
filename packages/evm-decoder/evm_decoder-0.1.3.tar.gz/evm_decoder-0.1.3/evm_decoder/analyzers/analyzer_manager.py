from typing import Dict, Any, List
from web3 import Web3
from chain_index import get_chain_info
from ..utils.constants import TRANSFER_TOPIC, WITHDRAWAL_TOPIC, DEPOSIT_TOPIC
from ..utils.hex_utils import ensure_hex_string
import logging
import binascii

logger = logging.getLogger(__name__)

class AnalyzerManager:
    def __init__(self):
        pass

    def analyze_transaction(self, tx_with_logs: Dict[str, Any], receipt: Dict[str, Any]) -> Dict[str, Any]:
        # Combine results from different analyzers
        return {
            "balance_analysis": self.analyze_balance_changes(tx_with_logs),
            "token_transfers": self.analyze_token_transfers(tx_with_logs),
            # Add other analysis results here
        }
    
    def analyze_token_transfers(self, tx_with_logs: Dict[str, Any]) -> List[Dict[str, Any]]:
        token_transfers: List[Dict[str, Any]] = []
        chain_info = get_chain_info(tx_with_logs['chain_id'])
        weth_address = chain_info.wrapperNativeCurrency.contract.lower()
        tx_from = tx_with_logs['from'].lower()
        tx_to = tx_with_logs['to'].lower()

        for log in tx_with_logs['logs']:
            if 'topics' in log:
                topic0 = ensure_hex_string(log['topics'][0])
                if topic0 == TRANSFER_TOPIC:
                    try:
                        from_address = ensure_hex_string(log['topics'][1][-40:])
                        to_address = ensure_hex_string(log['topics'][2][-40:])
                        value = int(ensure_hex_string(log['data']), 16)
                        token_address = log['address'].lower()
                        # Update balance for sender
                        token_transfers.append({
                            'from_address': from_address,
                            'to_address': to_address,
                            'value': value,
                            'token_address': token_address
                        })
                    except Exception as e:
                        # logger.error(f"Error processing event in get_balance_change: {str(e)}")
                        continue
                elif topic0 == WITHDRAWAL_TOPIC and log['address'].lower() == weth_address:
                    try:
                        destination = ensure_hex_string(log['topics'][1][-40:])
                        value = int(ensure_hex_string(log['data']), 16)
                        token_transfers.append({
                            'from_address': weth_address,
                            'to_address': destination,
                            'value': value,
                            'token_address': "native"
                        })
                        # token_transfers.append({
                        #     'from_address': operator,
                        #     'to_address': weth_address,
                        #     'value': value,
                        #     'token_address': weth_address
                        # })
                    except Exception as e:
                        logger.error(f"Error processing WETH withdrawal event: {str(e)}")
                        continue
                elif topic0 == DEPOSIT_TOPIC and log['address'].lower() == weth_address:
                    try:
                        to_address = ensure_hex_string(log['topics'][1][-40:])
                        value = int(ensure_hex_string(log['data']), 16)
                        token_transfers.append({
                            'from_address': weth_address,
                            'to_address': to_address,
                            'value': value,
                            'token_address': weth_address
                        })
                    except Exception as e:
                        logger.error(f"Error processing WETH deposit event: {str(e)}")
                        continue
        token_transfers.append({
            'from_address': tx_from,
            'to_address': tx_to,
            'value': int(tx_with_logs['value']),
            'token_address': "native"
        })
        return token_transfers

    def analyze_balance_changes(self, tx_with_logs: Dict[str, Any]) -> Dict[str, Dict[str, int]]:
        balance_changes: Dict[str, Dict[str, int]] = {}

        token_transfers = self.analyze_token_transfers(tx_with_logs)

        for transfer in token_transfers:
            from_address = transfer['from_address']
            to_address = transfer['to_address']
            value = transfer['value']
            token_address = transfer['token_address']
            if from_address not in balance_changes:
                balance_changes[from_address] = {}
            balance_changes[from_address][token_address] = balance_changes[from_address].get(token_address, 0) - value

            # Update balance for receiver
            if to_address not in balance_changes:
                balance_changes[to_address] = {}
            balance_changes[to_address][token_address] = balance_changes[to_address].get(token_address, 0) + value


        return balance_changes
        # for log in tx_with_logs['logs']:
        #     if log.topics:
        #         topic0 = self.ensure_hex_string(log.topics[0])
        #         if topic0 == TRANSFER_TOPIC:
        #             try:
        #                 from_address = '0x' + self.ensure_hex_string(log.topics[1])[-40:]
        #                 to_address = '0x' + self.ensure_hex_string(log.topics[2])[-40:]
        #                 value = int(self.ensure_hex_string(log.data), 16)
        #                 token_address = log.address.lower()

        #                 # Update balance for sender
        #                 if from_address not in balance_changes:
        #                     balance_changes[from_address] = {}
        #                 balance_changes[from_address][token_address] = balance_changes[from_address].get(token_address, 0) - value

        #                 # Update balance for receiver
        #                 if to_address not in balance_changes:
        #                     balance_changes[to_address] = {}
        #                 balance_changes[to_address][token_address] = balance_changes[to_address].get(token_address, 0) + value
        #             except Exception as e:
        #                 # logger.error(f"Error processing event in get_balance_change: {str(e)}")
        #                 continue
        #         elif topic0 == WITHDRAWAL_TOPIC and log.address.lower() == weth_address:
        #             try:
        #                 value = int(self.ensure_hex_string(log.data), 16)
        #                 if operator not in balance_changes:
        #                     balance_changes[operator] = {}
        #                 balance_changes[operator]['native'] = balance_changes[operator].get('native', 0) + value
        #             except Exception as e:
        #                 # logger.error(f"Error processing WETH withdrawal event: {str(e)}")
        #                 continue

        # # Account for native token transfer in the transaction
        # if operator not in balance_changes:
        #     balance_changes[operator] = {}
        # balance_changes[operator]['native'] = balance_changes[operator].get('native', 0) - int(tx_with_logs['value'])

        return balance_changes

    def analyze_from_balance_change(self, tx_with_logs: Dict[str, Any]) -> Dict[str, Any]:
        balance_changes: Dict[str, Dict[str, int]] = {}

        chain_info = get_chain_info(tx_with_logs['chain_id'])
        weth_address = chain_info.wrapperNativeCurrency.contract.lower()
        operator = tx_with_logs['from'].lower()
        value = int(tx_with_logs['value'])

        for log in tx_with_logs['logs']:
            if 'topics' in log:
                topic0 = ensure_hex_string(log['topics'][0])
                if topic0 == TRANSFER_TOPIC:
                    try:
                        from_address = ensure_hex_string(log['topics'][1][-40:])
                        to_address = ensure_hex_string(log['topics'][2][-40:])
                        value = int(ensure_hex_string(log['data']), 16)
                        token_address = log['address'].lower()
                        print("transfer from ", from_address, " to ", to_address, " value ", value, " token_address ", token_address)
                        # Update balance for sender
                        if from_address not in balance_changes:
                            balance_changes[from_address] = {}
                        balance_changes[from_address][token_address] = balance_changes[from_address].get(token_address, 0) - value

                        # Update balance for receiver
                        if to_address not in balance_changes:
                            balance_changes[to_address] = {}
                        balance_changes[to_address][token_address] = balance_changes[to_address].get(token_address, 0) + value
                    except Exception as e:
                        # logger.error(f"Error processing event in get_balance_change: {str(e)}")
                        continue
                elif topic0 == WITHDRAWAL_TOPIC and log['address'].lower() == weth_address:
                    try:
                        destination = ensure_hex_string(log['topics'][1][-40:])
                        value = int(ensure_hex_string(log['data']), 16)
                        balance_changes[operator]['native'] = balance_changes[operator].get('native', 0) - value
                    except Exception as e:
                        logger.error(f"Error processing WETH withdrawal event: {str(e)}")
                        continue
        if operator not in balance_changes:
            balance_changes[operator] = {}
        balance_changes[operator]['native'] = balance_changes[operator].get('native', 0) - int(tx_with_logs['value'])
        return balance_changes[operator]

    def analyze_transaction_type(self, transaction: Dict[str, Any]) -> Dict[str, Any]:
        pass

