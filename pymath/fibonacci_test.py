import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.a_fibonacci = Fibonacci()
        self.b_fibonacci = Fibonacci()
        self.b_fibonacci.numbers = 10, 20

    def testGetFib(self):
        self.assertEqual(self.a_fibonacci(10), 34)
        self.assertEqual(self.b_fibonacci(4), 50)

    def testSetCustom(self):
        self.a_fibonacci.numbers = 3, 4
        self.assertEqual(self.a_fibonacci.x1, 3)
        self.assertEqual(self.a_fibonacci.x2, 4)
        self.assertEqual(self.a_fibonacci.custom_flag, True)
        self.a_fibonacci.reset()
        self.assertEqual(self.a_fibonacci.x1, 0)
        self.assertEqual(self.a_fibonacci.x2, 1)
        self.assertEqual(self.a_fibonacci.custom_flag, False)

if __name__ == '__main__':
    unittest.main()
