import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test_conv_num_1(self):
        self.assertIsNone(conv_num(123))


if __name__ == '__main__':
    unittest.main()
