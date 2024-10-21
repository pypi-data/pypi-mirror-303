from .base_decoder import BaseDecoder
from ..utils.abi_utils import load_abi, decode_function_input, decode_input
from ..utils.data_structures import IndexableTransactionInput
from typing import Dict, Any, Optional
from web3 import Web3
import pandas as pd

class TransactionDecoder(BaseDecoder):
    def __init__(self, name: str, abi_path: Optional[str] = None, fixed_types: Optional[Dict[str, Any]] = None):
        self.name = name
        self.fixed_types = fixed_types or {}
        self.abi = load_abi(abi_path) if abi_path else None
        self.contract = Web3().eth.contract(abi=self.abi) if self.abi else None

        if fixed_types:
            for signature, params in fixed_types.items():
                selector = signature
                self.fixed_types[selector] = (signature, params)

    def can_decode(self, data: Any) -> bool:
        if not isinstance(data, dict) or'input' not in data:
            return False
        input_data = self.get_input_data(data)
        selector = input_data[:10]
        return selector in self.fixed_types or (self.contract is not None)

    def get_input_data(self, data):
        if isinstance(data, dict):
            return data.get('input', None)
        
        elif isinstance(data, pd.DataFrame):
            if 'input' in data.columns:
                if len(data) == 1:
                    return data['input'].iloc[0]
                else:
                    return data['input']
            else:
                return None
        else:
            raise ValueError("Unsupported data type")

    def get_selector(self, data: Any) -> str:
        input_data = self.get_input_data(data)
        return input_data[:10]

    def decode(self, data: Any) -> Dict[str, Any]:
        input_data = self.get_input_data(data)
        selector = input_data[:10]
        if selector in self.fixed_types:
            print("fixed_types,", selector)
            return self._decode_fixed_type(input_data, selector)
        elif self.contract:
            return self._decode_abi(input_data)
        else:
            return {"error": "No suitable decoder found for the transaction data"}

    def _decode_fixed_type(self, input_data: str, selector: str) -> Dict[str, Any]:
        signature, params = self.fixed_types[selector]
        try:
            decoded = decode_input(params, input_data=input_data)
            func_name = signature.split('(')[0] if '(' in signature else signature
            indexed_params = IndexableTransactionInput(decoded, {p['name']: i for i, p in enumerate(params)})
            return {
                "decoder": self.name,
                "function": func_name,
                "params": indexed_params
            }
        except Exception as e:
            return {"error": f"Failed to decode fixed type data: {str(e)}"}

    def _decode_abi(self, input_data: str) -> Dict[str, Any]:
        try:
            func_obj, params = decode_function_input(self.abi, input_data)
            indexed_params = IndexableTransactionInput(list(params.values()), {name: i for i, name in enumerate(params.keys())})
            return {
                "decoder": self.name,
                "function": func_obj.fn_name,
                "params": indexed_params
            }
        except Exception as e:
            return {"error": f"Failed to decode ABI data: {str(e)}"}