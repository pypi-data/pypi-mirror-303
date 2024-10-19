# tests/test_decoder.py

import unittest
from main.decoder import decode_bytes


class TestDecoder(unittest.TestCase):
    def test_valid_data(self):
        test_data_1 = (
            b"S\xd4\xacGS\xac+\xa000\xb8950\xeb\xe7\x8d\n"  # Expected weight: 8950
        )
        test_data_2 = (
            b"US\xacGS\xac+\xa00\xb10300\xeb\xe7\x8d\n"  # Expected weight: 10300
        )
        test_data_3 = (
            b"S\xd4\xacGS\xac+\xa0000\xb1\xb70\xeb\xe7\x8d\n"  # Expected weight: 170
        )
        test_data_4 = (
            b"S\xd4\xacGS\xac+\xa003\xb15\xb70\xeb\xe7\x8d\n"  # Expected weight: 31570
        )

        self.assertEqual(decode_bytes(test_data_1), 8950)
        self.assertEqual(decode_bytes(test_data_2), 10300)
        self.assertEqual(decode_bytes(test_data_3), 170)
        self.assertEqual(decode_bytes(test_data_4), 31570)

    def test_invalid_data(self):
        # Test cases where no valid weight can be extracted
        invalid_data_1 = b"\x00\x00\x00"  # No valid digits
        invalid_data_2 = b"\xff\xff\xff"  # No valid digits, invalid encoding
        invalid_data_3 = b"S\xd4\xacGS\xac+\xa0@#\x00@\x00\x00"  # Random invalid bytes

        self.assertIsNone(decode_bytes(invalid_data_1))
        self.assertIsNone(decode_bytes(invalid_data_2))
        self.assertIsNone(decode_bytes(invalid_data_3))

    def test_edge_case(self):
        # Test edge cases, such as small valid data or mixed invalid data
        test_data_5 = b"S\xd4\xacGS\xac+\xa0000060\xeb\xe7\x8d\n"  # Expected weight: 60
        test_data_6 = b"S\xd4\xacGS\xac+\xa0003\xeb\xe7\x8d\n"  # Expected weight: 3

        self.assertEqual(decode_bytes(test_data_5), 60)
        self.assertEqual(decode_bytes(test_data_6), 3)


if __name__ == "__main__":
    unittest.main()
