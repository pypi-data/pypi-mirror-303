import binascii

def ensure_hex_string(value):
    if value is None:
        return None
    if isinstance(value, str):
        return value if value.startswith('0x') else '0x' + value
    elif isinstance(value, bytes):
        return '0x' + binascii.hexlify(value).decode('ascii')
    elif isinstance(value, int):
        return hex(value)  # This will return a string starting with '0x'
    else:
        raise ValueError(f"Unexpected type for value: {type(value)}")