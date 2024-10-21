# EVM Decoder

EVM Decoder is a Python package for decoding and analyzing Ethereum Virtual Machine (EVM) transactions and logs. It provides tools to help developers and researchers understand and work with EVM-based blockchain data.

## Features

- Decode EVM transaction input data
- Decode EVM event logs
- Analyze balance changes in transactions
- Support for custom ABI and fixed types
- Retrieve chain information for various EVM-compatible networks

## Installation

You can install the EVM Decoder package using pip:
```
bash
pip install evm-decoder
```


## Usage

Here's a quick example of how to use EVM Decoder:

python
from evm_decoder import DecoderManager, AnalyzerManager
Initialize managers
decoder_manager = DecoderManager()
analyzer_manager = AnalyzerManager()
Example transaction data
transaction_data = {
'input': '0x23b872dd000000000000000000000000...',
'from': '0xb8faa80fe04a4afd30c89f40e4fcdc6dafb274d9',
'to': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
'value': '0',
'chain_id': 1,
'logs': [...]
}
Decode the transaction
decode_result = decoder_manager.decode(transaction_data)
print("Transaction decode result:", decode_result)
Analyze the transaction
analysis_result = analyzer_manager.analyze_transaction(transaction_data, {})
print("Transaction analysis result:", analysis_result)


For more detailed examples, check the `examples` directory in the repository.

## Configuration

EVM Decoder uses a configuration file to set up decoders. You can customize this file to add support for specific contracts or event types. The default configuration file is located at `evm_decoder/config/decoder_config.json`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who have helped to improve this project.
- This project makes use of several open-source libraries, including Web3.py and eth-abi.

## Contact

If you have any questions or feedback, please open an issue on the GitHub repository.