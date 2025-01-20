import sys
import unittest
from simple_calculator import SimpleCalculator



class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(-5, 3), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 6), 30)
        self.assertEqual(self.calc.multiply(-2, 4), -8)
        self.assertEqual(self.calc.multiply(0, 30), 0)

    def test_divide(self):
        try:
            self.assertEqual(self.calc.divide(9, 3), 3)

        except ZeroDivisionError:
            return "cant divide by zero"
        


if __name__ == '__main__':
    unittest.main()



