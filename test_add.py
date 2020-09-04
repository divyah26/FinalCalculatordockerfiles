import calculator
import unittest

class TestCalculator(unittest.TestCase):

    def test_addition(self):

        result = calculator.add(2, 5)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()

