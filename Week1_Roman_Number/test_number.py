import unittest
from roman_converter import roman_to_integer, integer_to_roman


class TestRomanConverter(unittest.TestCase):

    # ---------------------------------------------------------
    # 1. Valid Conversions (Roman -> Integer & Integer -> Roman)
    # ---------------------------------------------------------
    def test_single_symbols(self):
        self.assertEqual(roman_to_integer("I"), 1)
        self.assertEqual(roman_to_integer("V"), 5)
        self.assertEqual(roman_to_integer("X"), 10)
        self.assertEqual(roman_to_integer("L"), 50)
        self.assertEqual(roman_to_integer("C"), 100)
        self.assertEqual(roman_to_integer("D"), 500)
        self.assertEqual(roman_to_integer("M"), 1000)

    def test_additive_and_subtractive_combinations(self):
        cases = {
            "III": 3,
            "IV": 4,
            "IX": 9,
            "LVIII": 58,
            "MCMXCIV": 1994,
            "MMMCMXCIX": 3999,
        }
        for roman, integer in cases.items():
            with self.subTest(roman=roman):
                self.assertEqual(roman_to_integer(roman), integer)
                self.assertEqual(integer_to_roman(integer), roman)

    def test_case_insensitivity_and_whitespace(self):
        self.assertEqual(roman_to_integer(" xiv "), 14)
        self.assertEqual(roman_to_integer("mcmxciv"), 1994)

    # ---------------------------------------------------------
    # 2. Validation & Error Handling (Roman -> Integer)
    # ---------------------------------------------------------
    def test_empty_input(self):
        with self.assertRaises(ValueError) as ctx:
            roman_to_integer("")
        self.assertEqual(str(ctx.exception), "Roman numeral cannot be empty.")

    def test_invalid_characters(self):
        with self.assertRaises(ValueError) as ctx:
            roman_to_integer("X12")
        self.assertEqual(str(ctx.exception), "Invalid Roman numeral character.")

    def test_illegal_repetitions(self):
        # Repetition of V, L, D
        for invalid in ["VV", "LL", "DD"]:
            with self.assertRaises(ValueError) as ctx:
                roman_to_integer(invalid)
            self.assertEqual(str(ctx.exception), "V, L, and D cannot be repeated.")

        # Repetition > 3 times for I, X, C, M
        for invalid in ["IIII", "XXXX", "CCCC", "MMMM"]:
            with self.assertRaises(ValueError) as ctx:
                roman_to_integer(invalid)
            self.assertEqual(
                str(ctx.exception),
                "A Roman numeral cannot repeat more than 3 times."
            )

    def test_invalid_subtractions(self):
        invalid_pairs = ["IL", "VX", "IC", "XD", "VL"]
        for pair in invalid_pairs:
            with self.assertRaises(ValueError) as ctx:
                roman_to_integer(pair)
            self.assertTrue(str(ctx.exception).startswith("Invalid subtraction"))

    def test_invalid_structure_and_order(self):
        # Non-canonical or malformed sequences caught by re-encoding
        malformed = ["IIV", "CMCC", "VIV", "XIXX"]
        for string in malformed:
            with self.assertRaises(ValueError) as ctx:
                roman_to_integer(string)
            self.assertEqual(str(ctx.exception), "Invalid Roman numeral format.")


if __name__ == "__main__":
    unittest.main()