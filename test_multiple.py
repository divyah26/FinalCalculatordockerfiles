import calculator
import unittest

class TestCalculator(unittest.TestCase):

    def test_multiplication(self):

        result = calculator.multiple(2, 5)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
