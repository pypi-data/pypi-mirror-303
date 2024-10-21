from .base_decoder import BaseDecoder
from ..utils.abi_utils import load_abi, decode_log
from ..utils.data_structures import IndexableEventLog
from eth_utils import event_abi_to_log_topic
from typing import Dict, Any, Optional, List, Tuple
from web3 import Web3
import json

class EventDecoder(BaseDecoder):
    def __init__(self, name: str, abi_path: Optional[str] = None, fixed_types: Optional[Dict[str, List[Dict[str, str]]]] = None):
        self.name = name
        self.abi = load_abi(abi_path) if abi_path else None
        self.fixed_types = fixed_types or {}
        self.name = name
        self.contract = None
        self.fixed_types: Dict[str, Tuple[str, List[Dict[str, Any]]]] = {}
        self.w3 = Web3()
        
        if abi_path:
            with open(abi_path, 'r') as abi_file:
                abi = json.load(abi_file)
            self.contract = self.w3.eth.contract(abi=abi)

        if fixed_types:
            for event_signature, params in fixed_types.items():
                abi_inputs = []
                for i, p in enumerate(params):
                    if isinstance(p, dict):
                        abi_inputs.append({
                            "name": p.get("name", f"param{i}"),
                            "type": p["type"],
                            "indexed": p.get("indexed", False)
                        })
                    else:
                        abi_inputs.append({
                            "name": f"param{i}",
                            "type": p,
                            "indexed": False
                        })
                
                event_abi = {
                    "type": "event",
                    "name": event_signature.split('(')[0] if not event_signature.startswith("0x") else "UnknownEvent",
                    "inputs": abi_inputs
                }
                topic = event_signature if event_signature.startswith("0x") else "0x" + event_abi_to_log_topic(event_abi).hex()
                
                self.fixed_types[topic] = (event_abi['name'], abi_inputs)

    def can_decode(self, data: Any) -> bool:
        if not isinstance(data, dict) or ('topics' not in data and 'topic0' not in data):
            return False
        topic0 = data['topic0'] if 'topic0' in data else data['topics'][0]
        return topic0 in self.fixed_types or (self.contract and any(topic0 == event_abi_to_log_topic(e).hex() for e in self.contract.abi if e['type'] == 'event'))


    def decode(self, event: Dict[str, Any]) -> Dict[str, Any]:
        try:
            if self.abi:
                decoded_event = decode_event_log(self.abi, event)
            elif self.fixed_types:
                decoded_event = self._decode_fixed_type(event)
            else:
                return {"error": "No suitable decoder found for the event data"}


            return decoded_event
        except Exception as e:
            return {"error": f"Failed to decode event data: {str(e)}"}


    def _decode_fixed_type(self, data: Dict[str, Any]) -> Dict[str, Any]:
        topic0 = data['topics'][0] if 'topics' in data else data['topic0']
        if topic0 in self.fixed_types:
            event_name, abi_inputs = self.fixed_types[topic0]
            decoded_log = decode_log(abi_inputs, data)

            return {
                "decoder": self.name,
                "event": event_name,
                "args": decoded_log
            }

        raise ValueError(f"Event with topic {topic0} not found in fixed types")