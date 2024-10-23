from typing import Dict, Any, List, Optional
from .base_decoder import BaseDecoder
from .transaction_decoder import TransactionDecoder
from .event_decoder import EventDecoder

class DecoderFactory:
    DECODER_TYPES = {
        "transaction": TransactionDecoder,
        "event": EventDecoder,
    }

    @classmethod
    def get_decoder(cls, decoder_type: str, name: str, abi_path: Optional[str] = None, fixed_types: Optional[Dict[str, List[Any]]] = None) -> BaseDecoder:
        decoder_class = cls.DECODER_TYPES.get(decoder_type)
        if not decoder_class:
            raise ValueError(f"Unknown decoder type: {decoder_type}")
        
        return decoder_class(name, abi_path, fixed_types)

    @classmethod
    def register_decoder(cls, decoder_type: str, decoder_class: type):
        cls.DECODER_TYPES[decoder_type] = decoder_class