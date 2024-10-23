from eth_abi.codec import ABICodec
from eth_abi.registry import registry
from typing import List, Any, Dict, Optional
from .base_decoder import BaseDecoder
from ..utils.data_structures import IndexableTransactionInput

abi_codec = ABICodec(registry)

class RawDataDecoder(BaseDecoder):
    def __init__(self, name: str):
        self.name = name

    def can_decode(self, data: Any) -> bool:
        return isinstance(data, (str, bytes))

    def decode(self, data: str, types: List[str], param_names: Optional[List[str]] = None) -> Dict[str, Any]:
        try:
            # Remove '0x' prefix if present
            if isinstance(data, str) and data.startswith('0x'):
                data = data[2:]
            
            # Convert to bytes if it's a string
            if isinstance(data, str):
                data = bytes.fromhex(data)
            
            # Decode the data
            decoded = abi_codec.decode(types, data)
            
            # If param_names are provided, use them; otherwise, use generic names
            if param_names and len(param_names) == len(types):
                result = dict(zip(param_names, decoded))
            else:
                result = dict(zip([f"param{i}" for i in range(len(types))], decoded))
            
            return {
                "decoder": self.name,
                "params": IndexableTransactionInput(list(decoded), {name: i for i, name in enumerate(result.keys())})
            }
        except Exception as e:
            return {"error": f"Failed to decode raw data: {str(e)}"}
