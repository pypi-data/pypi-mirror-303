# test_platform.py

import unittest
from kiowaplatform.platform import calculate_imei_check_digit

class TestCalculateImeiCheckDigit(unittest.TestCase):
    def test_valid_imei_numbers(self):
        # Test cases with known IMEI check digits
        test_cases = [
            ("49015420323751", 8),  # Example IMEI: 490154203237518
            ("35175605152315", 9),  # Example IMEI: 351756051523159
            ("00000000000000", 0),  # All zerosx
        ]

        for imei_14, expected_check_digit in test_cases:
            with self.subTest(imei_14=imei_14):
                result = calculate_imei_check_digit(imei_14)
                self.assertEqual(result, expected_check_digit,
                                 f"Failed for IMEI: {imei_14}")

    def test_invalid_length(self):
        # IMEI numbers that are not 14 digits long
        invalid_imeis = [
            "4901542032375",    # 13 digits
            "490154203237518",  # 15 digits
            "",                  # Empty string
            "1234567890123",     # 13 digits
            "123456789012345",   # 15 digits
        ]

        for imei in invalid_imeis:
            with self.subTest(imei=imei):
                with self.assertRaises(ValueError):
                    calculate_imei_check_digit(imei)

    def test_non_digit_characters(self):
        # IMEI numbers containing non-digit characters
        invalid_imeis = [
            "4901542032375A",
            "ABCDEFGHIJKLMN",
            "1234-5678-9012-34",
            "49015O20323751",  # Contains letter 'O'
        ]

        for imei in invalid_imeis:
            with self.subTest(imei=imei):
                with self.assertRaises(ValueError):
                    calculate_imei_check_digit(imei)

if __name__ == '__main__':
    unittest.main()
