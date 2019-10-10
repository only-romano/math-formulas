import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    sequence = [None, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, -34, -21, -13, -8, -5, -3, -2, -1, -1, 0]
    def setUp(self):
        self.a_fibonacci = Fibonacci()
        self.b_fibonacci = Fibonacci()
        self.b_fibonacci.numbers = 10, 20
        self.cur_func = None
        self.multiple_args = False

    def testGetFib(self):
        self.assertEqual(self.a_fibonacci(10), 34)
        self.assertEqual(self.b_fibonacci(4), 50)
        self.cur_func = self.a_fibonacci.get_fib
        self.testTypes()

    def testSetCustom(self):
        self.a_fibonacci.numbers = 3, 4
        self.assertEqual(self.a_fibonacci.x1, 3)
        self.assertEqual(self.a_fibonacci.x2, 4)
        self.assertEqual(self.a_fibonacci.custom_flag, True)
        self.a_fibonacci.reset()
        self.assertEqual(self.a_fibonacci.x1, 0)
        self.assertEqual(self.a_fibonacci.x2, 1)
        self.assertEqual(self.a_fibonacci.custom_flag, False)

    def testTypes(self):
        self.testIntegers()
        #self.testFloats(func)
        #self.testLists(func)
        #self.testTuples(func)
        #self.testDicts(func)
        #self.testStrings(func)

    def testIntegers(self):
        if self.cur_func:
            for x in range(-10, 11):
                result = self.cur_func(x)
                self.assertTrue(result == self.sequence[x], 'Integer single ' +\
                    'argument call failed. Arg: %i. Expected: %s; Result: %s' %\
                    (x, str(self.sequence[x]), str(result)))

            with self.assertRaises(TypeError):
                self.cur_func(1, 2, 3)

if __name__ == '__main__':
    unittest.main()
