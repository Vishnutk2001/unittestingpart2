import Calculator

import unittest

class calculator_test(unittest.TestCase):

    def setUp(self):
        self.a = 20
        self.b = 10

    def tearDown(self):
        self.a = 0
        self.b = 0




    @unittest.skip("skipped this test")
    def test_add(self):

        c = Calculator.add(self.a,self.b)
        self.assertEqual(c,self.a+self.b)

    def test_sub(self):

        c = Calculator.sub(self.a,self.b)
        self.assertEqual(c,self.a-self.b)

    def test_mul(self):

        c = Calculator.mul(self.a,self.b)
        self.assertEqual(c,self.a*self.b)

    def test_div(self):

        c = Calculator.div(self.a,self.b)
        self.assertEqual(c,self.a/self.b)


if __name__ == "__main__":
    unittest.main()
