import unittest
from unittest.mock import patch, mock_open
import json
from src.evm_decoder.decoders.decoder_manager import DecoderManager
from src.evm_decoder.decoders.transaction_decoder import TransactionDecoder, EventDecoder

class TestDecoderManager(unittest.TestCase):
    def setUp(self):
        self.config_data = {
            "transaction_decoders": [
                {
                    "type": "transaction",
                    "name": "TestTransactionDecoder",
                    "abi_path": "test_abi.json",
                    "fixed_types": {"0x12345678": ["uint256", "address"]}
                }
            ],
            "event_decoders": [
                {
                    "type": "event",
                    "name": "TestEventDecoder",
                    "abi_path": "test_abi.json",
                    "fixed_types": {"TestEvent(uint256,address)": [{"name": "value", "type": "uint256", "indexed": True}, {"name": "addr", "type": "address", "indexed": False}]}
                }
            ]
        }

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"abi": "test"}))
    @patch("src.evm_decoder.decoders.transaction_decoder.DecoderFactory.get_decoder")
    def test_load_decoders(self, mock_get_decoder, mock_file):
        manager = DecoderManager("fake_config.json")
        
        self.assertEqual(len(manager.decoders), 2)
        self.assertIn("TestTransactionDecoder", manager.decoders)
        self.assertIn("TestEventDecoder", manager.decoders)
        
        mock_get_decoder.assert_any_call("transaction", "TestTransactionDecoder", "test_abi.json", {"0x12345678": ["uint256", "address"]})
        mock_get_decoder.assert_any_call("event", "TestEventDecoder", "test_abi.json", {"TestEvent(uint256,address)": [{"name": "value", "type": "uint256", "indexed": True}, {"name": "addr", "type": "address", "indexed": False}]})

    @patch("src.evm_decoder.decoders.transaction_decoder.DecoderFactory.get_decoder")
    def test_decode(self, mock_get_decoder):
        mock_decoder = unittest.mock.MagicMock()
        mock_decoder.can_decode.return_value = True
        mock_decoder.decode.return_value = {"result": "decoded_data"}
        mock_get_decoder.return_value = mock_decoder

        manager = DecoderManager("fake_config.json")
        result = manager.decode("test_data")

        self.assertEqual(result, {"result": "decoded_data"})
        mock_decoder.can_decode.assert_called_once_with("test_data")
        mock_decoder.decode.assert_called_once_with("test_data")

    @patch("src.evm_decoder.decoders.transaction_decoder.DecoderFactory.get_decoder")
    def test_decode_with_specific_decoder(self, mock_get_decoder):
        mock_decoder = unittest.mock.MagicMock()
        mock_decoder.decode.return_value = {"result": "decoded_data"}
        mock_get_decoder.return_value = mock_decoder

        manager = DecoderManager("fake_config.json")
        result = manager.decode_with_specific_decoder("test_data", "TestTransactionDecoder")

        self.assertEqual(result, {"result": "decoded_data"})
        mock_decoder.decode.assert_called_once_with("test_data")

    @patch("src.evm_decoder.decoders.transaction_decoder.DecoderFactory.get_decoder")
    def test_decode_with_nonexistent_decoder(self, mock_get_decoder):
        manager = DecoderManager("fake_config.json")
        result = manager.decode_with_specific_decoder("test_data", "NonexistentDecoder")

        self.assertEqual(result, {"error": "Decoder 'NonexistentDecoder' not found"})

if __name__ == "__main__":
    unittest.main()