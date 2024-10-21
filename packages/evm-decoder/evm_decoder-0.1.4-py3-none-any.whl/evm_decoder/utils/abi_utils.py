import json
from eth_abi.codec import ABICodec
from eth_abi.registry import registry
from eth_utils import function_signature_to_4byte_selector, event_abi_to_log_topic, decode_hex
from typing import Dict, Any, List, Tuple
from web3 import Web3
from .data_structures import IndexableEventLog

abi_codec = ABICodec(registry)
w3 = Web3()

def load_abi(abi_path: str) -> List[Dict[str, Any]]:
    with open(abi_path, 'r') as abi_file:
        return json.load(abi_file)

def get_function_selector(function_signature: str) -> str:
    return "0x" + function_signature_to_4byte_selector(function_signature).hex()

def get_event_topic(event_abi: Dict[str, Any]) -> str:
    return "0x" + event_abi_to_log_topic(event_abi).hex()

def decode_abi(types: List[str], data: str) -> List[Any]:
    return list(abi_codec.decode(types, bytes.fromhex(data[2:] if data.startswith('0x') else data)))

def decode_single(type_str: str, data: str) -> Any:
    return abi_codec.decode_single(type_str, decode_hex(data))

def encode_abi(types: List[str], values: List[Any]) -> str:
    return "0x" + abi_codec.encode(types, values).hex()

def encode_single(type_str: str, value: Any) -> str:
    return "0x" + abi_codec.encode_single(type_str, value).hex()

def decode_function_input(abi: List[Dict[str, Any]], input_data: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    selector = input_data[:10]
    print(selector, abi)
    for item in abi:
        if item['type'] == 'function' and get_function_selector(item['name']) == selector:
            types = [input['type'] for input in item['inputs']]
            names = [input['name'] for input in item['inputs']]
            print(types, names)
            decoded = abi_codec.decode(types, input_data[10:])
            return item, dict(zip(names, decoded))
    raise ValueError("Function not found in ABI")

def decode_input(params: List[Dict[str, Any]], input_data: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    data = input_data[10:]
    types = [param['type'] if isinstance(param, dict) else param for param in params]
    names = [param['name'] for param in params]
    try:
        decoded = abi_codec.decode(types, bytes.fromhex(data))
    except Exception as e:
        print(e)
    return dict(zip(names, decoded))


def decode_event_log(abi: List[Dict[str, Any]], log: Dict[str, Any]) -> Dict[str, Any]:
    topics = log['topics']
    data = log['data']
    
    for event in abi:
        if event['type'] == 'event':
            event_id = get_event_topic(event)
            if event_id == topics[0]:
                indexed_inputs = [i for i in event['inputs'] if i['indexed']]
                non_indexed_inputs = [i for i in event['inputs'] if not i['indexed']]
                
                decoded_topics = [decode_single(inp['type'], topic) for inp, topic in zip(indexed_inputs, topics[1:])]
                decoded_data = decode_abi([inp['type'] for inp in non_indexed_inputs], data)
                
                decoded_args = {}
                for inp, value in zip(indexed_inputs, decoded_topics):
                    decoded_args[inp['name']] = value
                for inp, value in zip(non_indexed_inputs, decoded_data):
                    decoded_args[inp['name']] = value
                
                return {
                    'event': event['name'],
                    'args': decoded_args
                }
    
    raise ValueError("Event not found in ABI")

def decode_log(params: List[Dict[str, Any]], log: Dict[str, Any]) -> Dict[str, Any]:
    indexed_params = [p for p in params if p['indexed']]
    non_indexed_params = [p for p in params if not p['indexed']]
    decoded_topics = []
    # for i, param in enumerate(indexed_params):
    #     print(f"param: {param}")
    #     topic_value = log.get(f'topic{i+1}', '0x0') if f'topic{i+1}' in log else log['topics'][i+1]
    #     print(f"topic_value: {topic_value}")
    #     decoded_topics.append(abi_codec.decode([param['type']], decode_hex(topic_value)))
    if indexed_params:
        indexed_types = [param['type'] for param in indexed_params]
        topics = log['topics'][1:] if ('topics' in log and len(log['topics']) > 1) else [t for t in [log.get('topic1'), log.get('topic2'), log.get('topic3')] if t is not None]
        # topics = log['topics'][1:] if len(log['topics']) > 1 else [log.get('topic1'), log.get('topic2'), log.get('topic3')]
        concatenated_topics = ''.join(topic[2:] for topic in topics)  # Remove '0x' prefix and concatenate
        decoded_topics = list(abi_codec.decode(indexed_types, bytes.fromhex(concatenated_topics)))
        # print(f"decoded_topics: {decoded_topics}")

    decoded_data = []
    if non_indexed_params:
        non_indexed_types = [p['type'] for p in non_indexed_params]
        decoded_data = list(abi_codec.decode(non_indexed_types, bytes.fromhex(log['data'][2:])))

    param_names = {p['name']: i for i, p in enumerate(params) if 'name' in p}
    indexed_args = IndexableEventLog(decoded_topics, decoded_data, param_names)


    return indexed_args