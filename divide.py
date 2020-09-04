import calculator
import unittest

class TestCalculator(unittest.TestCase):

    def test_division(self):

        result = calculator.divide(10, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
