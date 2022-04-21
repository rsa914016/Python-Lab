import unittest
from Ex13 import isEven, isOdd


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('SetUp')

    def tearDown(self):
        print('TearDown')

    def test_isEven(self):
        self.assertEqual(isEven(2), True)
        self.assertEqual(isEven(65), False)
        self.assertEqual(isEven(8), True)
        self.assertEqual(isEven(100), True)

    def test_isOdd(self):
        self.assertEqual(isOdd(2), False)
        self.assertEqual(isOdd(65), True)
        self.assertEqual(isOdd(8), False)
        self.assertEqual(isOdd(101), True)


if __name__ == '__main__':
    unittest.main()
