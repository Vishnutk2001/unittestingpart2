import Calculator

import unittest

class calculator_test(unittest.TestCase):
    def test_add(self):
        a = 20
        b = 10
        c = Calculator.add(a,b)
        self.assertEqual(c,a+b)

    def test_sub(self):
        a = 20
        b = 10
        c = Calculator.sub(a,b)
        self.assertEqual(c,a-b)

    def test_mul(self):
        a = 10
        b = 20
        c = Calculator.mul(a,b)
        self.assertEqual(c,a*b)

    def test_div(self):
        a = 20
        b = 10
        c = Calculator.div(a,b)
        self.assertEqual(c,a/b)


if __name__ == "__main__":
    unittest.main()
