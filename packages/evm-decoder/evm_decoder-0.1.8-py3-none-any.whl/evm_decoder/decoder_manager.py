from typing import Dict, Any, List
from .decoders.base_decoder import BaseDecoder
from .decoders.transaction_decoder import TransactionDecoder
from .decoders.event_decoder import EventDecoder
from .decoders.raw_data_decoder import RawDataDecoder
import json
import os

class DecoderManager:
    def __init__(self, config_path: str = None):
        if config_path is None:
            # Use a default path relative to this file
            config_path = os.path.join(os.path.dirname(__file__), 'config', 'decoder_config.json')
        self.decoders: Dict[str, BaseDecoder] = {}
        self.load_decoders(config_path)

    def load_decoders(self, config_path: str):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)

        for decoder_config in config.get('transaction_decoders', []) + config.get('event_decoders', []):
            decoder_type = decoder_config['type']
            name = decoder_config['name']
            abi_path = decoder_config.get('abi_path')
            fixed_types = decoder_config.get('fixed_types')

            if decoder_type == 'transaction':
                decoder = TransactionDecoder(name, abi_path, fixed_types)
            elif decoder_type == 'event':
                decoder = EventDecoder(name, abi_path, fixed_types)
            else:
                raise ValueError(f"Unknown decoder type: {decoder_type}")

            self.add_decoder(name, decoder)

    def add_decoder(self, name: str, decoder: BaseDecoder):
        self.decoders[name] = decoder

    def decode(self, data: Any) -> Dict[str, Any]:
        for decoder in self.decoders.values():
            if decoder.can_decode(data):
                return decoder.decode(data)
        return {"error": "No suitable decoder found for the input data"}

    def decode_with_specific_decoder(self, data: Any, decoder_name: str) -> Dict[str, Any]:
        if decoder_name in self.decoders:
            return self.decoders[decoder_name].decode(data)
        return {"error": f"Decoder '{decoder_name}' not found"}
