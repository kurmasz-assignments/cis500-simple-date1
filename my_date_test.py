import unittest
import my_date

class MyDateTest(unittest.TestCase):

    #
    # is_leap_year
    #

    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1985))

    #
    # ordinal_date
    #

    def test_ordinal_date1(self):
        self.assertEqual(1, my_date.ordinal_date(1997, 1, 1))

    def test_ordinal_date2(self):
        self.assertEqual(32, my_date.ordinal_date(1995, 2, 1))

    #
    # days_elapsed  
    #

    def test_days_elapsed1(self):
        self.assertEqual(1, my_date.days_elapsed(1997, 1, 1, 1997, 1, 2))

    def test_days_elapsed2(self):
        self.assertEqual(31, my_date.days_elapsed(1997, 1, 1, 1997, 2, 1))

    def test_days_elapsed3(self):
        self.assertEqual(365, my_date.days_elapsed(1997, 1, 1, 1998, 1, 1))

    # Warning: You need more tests than you think for this function

    #
    # day_of_week
    #

    def test_day_of_week1(self):
        self.assertEqual("Monday", my_date.day_of_week(1753, 1, 1))


    #
    # to_str
    #
    def test_to_str1(self):
        self.assertEqual("Friday, 02 August 2024", my_date.to_str(2024, 8, 2))
