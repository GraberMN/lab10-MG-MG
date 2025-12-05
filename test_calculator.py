# https://github.com/GraberMN/lab10-MG-MG.git
# Partner 1: Mateo Graber (git config user.email "grabermn3@gmail.com")
# Partner 2: Mateo Graber (git config user.email "graberm@ufl.edu")

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-3, 4), 1)
        self.assertEqual(add(3, -4), -1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 4), -1)
        self.assertEqual(subtract(-3, 4), -7)
        self.assertEqual(subtract(3, -4), 7)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6 )
        self.assertEqual(mul(-2, -3), 6)
        self.assertEqual(mul(-2, 3), -6)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 6), 2)
        self.assertEqual(div(-3, 9), -3)
        self.assertEqual(div(15, 0), 0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
          # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(3, 27), 3)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0, 100)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
          # call log function inside, example:
          with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(8, 6), 10)
        self.assertEqual(hypotenuse(-8, -6), 10)
        self.assertEqual(hypotenuse(-8, 6), 10)

    def test_sqrt(self): # 3 assertions
          # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-9)
          # Test basic function
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(4), 2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()