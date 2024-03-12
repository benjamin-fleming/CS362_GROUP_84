import unittest

from task import conv_num, my_datetime, conv_endian


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test_conv_num_0(self):
        self.assertIsNone(conv_num(123))

    def test_conv_num_1(self):
        self.assertIsNone(conv_num("0x1A.1A"))

    def test_conv_num_2(self):
        self.assertIsNone(conv_num("ABC"))

    def test_conv_num_3(self):
        self.assertIsNone(conv_num("1.2.3"))

    def test_conv_num_4(self):
        self.assertEqual(conv_num("123"), 123)

    def test_conv_num_5(self):
        self.assertEqual(conv_num("-123"), -123)

    def test_conv_num_6(self):
        self.assertEqual(conv_num("12.65"), 12.65)

    def test_conv_num_7(self):
        self.assertEqual(conv_num("0X1A"), 26)

    def test_conv_num_8(self):
        self.assertEqual(conv_num("-0x1A"), -26)

    def test_my_datetime_0(self):
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_my_datetime_1_year(self):
        self.assertEqual(my_datetime(365 * 24 * 60 * 60), '01-01-1971')

    def test_my_datetime_2_years(self):
        self.assertEqual(my_datetime(365 * 2 * 24 * 60 * 60), '01-01-1972')

    def test_my_datetime_3_years(self):
        self.assertEqual(my_datetime(365 * 3 * 24 * 60 * 60), '12-31-1972')

    def test_my_datetime_123456789(self):
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def test_my_datetime_9876543210(self):
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def test_my_datetime_201653971200(self):
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

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
