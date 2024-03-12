import unittest
from task import conv_endian


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def conv_endian_test1(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def conv_endian_test2(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def conv_endian_test3(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def conv_endian_test4(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def conv_endian_test5(self):
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def conv_endian_test6(self):
        self.assertEqual(conv_endian(0, 'big'), '00')

    def conv_endian_test7(self):
        self.assertEqual(conv_endian(0, 'little'), '00')

    def conv_endian_test8(self):
        self.assertEqual(conv_endian(16, 'big'), '10')

    def conv_endian_test9(self):
        self.assertEqual(conv_endian(15, 'big'), '0F')

    def conv_endian_test10(self):
        self.assertEqual(conv_endian(1, 'big'), '01')

    def conv_endian_test11(self):
        self.assertIsNone(conv_endian(1, 'foo'))


if __name__ == '__main__':
    unittest.main()
