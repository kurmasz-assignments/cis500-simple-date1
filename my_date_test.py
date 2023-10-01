import unittest
import my_date


class MyDateTest(unittest.TestCase):

    # is_leap_year
    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(2000))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1900))

    def test_is_leap_year3(self):
        self.assertTrue(my_date.is_leap_year(2024))

    def test_is_leap_year4(self):
        self.assertFalse(my_date.is_leap_year(2021))

    def test_is_leap_year5(self):
        self.assertTrue(my_date.is_leap_year(2400))

    # orginal_data

    def test_ordinal_date1(self):
        self.assertEqual(1, my_date.ordinal_date(2000, 1, 1))

    def test_ordinal_date2(self):
        self.assertEqual(31, my_date.ordinal_date(2023, 1, 31))

    def test_ordinal_date3(self):
        self.assertEqual(365, my_date.ordinal_date(2022, 12, 31))

    def test_ordinal_date4(self):
        self.assertEqual(60, my_date.ordinal_date(2022, 2, 29))

    def test_ordinal_date5(self):
        self.assertEqual(100, my_date.ordinal_date(2021, 4, 10))

    # days_elapsed

    def test_days_elapsed1(self):
        self.assertEqual(365, my_date.days_elapsed(2020, 1, 1, 2021, 1, 1))

    def test_days_elapsed2(self):
        self.assertEqual(15, my_date.days_elapsed(2023, 9, 15, 2023, 9, 30))

    def test_days_elapsed3(self):
        self.assertEqual(0, my_date.days_elapsed(2022, 5, 10, 2022, 5, 10))

    def test_days_elapsed4(self):
        self.assertEqual(366, my_date.days_elapsed(2020, 1, 1, 2021, 1, 2))

    # day_of_week

    def test_day_of_week1(self):
        self.assertEqual("Wednesday", my_date.day_of_week(2022, 5, 18))

    def test_day_of_week2(self):
        self.assertEqual("Friday", my_date.day_of_week(2023, 9, 29))

    def test_day_of_week3(self):
        self.assertEqual("Saturday", my_date.day_of_week(2023, 10, 7))

    def test_day_of_week4(self):
        self.assertEqual("Thursday", my_date.day_of_week(2023, 1, 5))

    def test_day_of_week5(self):
        self.assertEqual("Sunday", my_date.day_of_week(2023, 12, 31))

    # to_str

    def test_to_str1(self):
        self.assertEqual("Tuesday, 01 January 2008", my_date.to_str(2008, 1, 1))

    def test_to_str2(self):
        self.assertEqual("Friday, 15 December 2023", my_date.to_str(2023, 12, 15))

    def test_to_str3(self):
        self.assertEqual("Sunday, 04 July 2021", my_date.to_str(2021, 7, 4))

    def test_to_str4(self):
        self.assertEqual("Thursday, 10 March 2050", my_date.to_str(2050, 3, 10))

    def test_to_str5(self):
        self.assertEqual("Saturday, 29 February 2400", my_date.to_str(2400, 2, 29))


if _name_ == '_main_':
    unittest.main()
