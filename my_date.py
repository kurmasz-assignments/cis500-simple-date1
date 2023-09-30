#######################################################
# my_date
#
# Name: Bhavya Sri Pallapu
# Section: 03
#
# Fall 2023
#########################################################

DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def is_leap_year(year: int) -> bool:
    isLeapYear = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    return isLeapYear
    pass
 
def ordinal_date(year: int , month: int, day: int) -> int:
    daysInMonth = [0, 31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(daysInMonth[:month]) + day
    pass
    
def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    startDate = ordinal_date(year1, month1, day1)
    endDate = ordinal_date(year2, month2, day2)
    return endDate - startDate
    pass
    
# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


def day_of_week(year: int, month: int, day: int) -> str:
    daysElapsed = ordinal_date(year, month, day) - ordinal_date(1753, 1, 1)
    dayIndex = (daysElapsed % 7 + 1) % 7  
    return DAYS_OF_WEEK[dayIndex]
    pass
    
def to_str(year: int, month: int, day: int) -> str:
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    dayName = day_of_week(year, month, day)
    formattedDate = f"{dayName}, {day:02d} {months[month - 1]} {year}"
    return formattedDate
    pass
              
    
