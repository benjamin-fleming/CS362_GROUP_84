def my_func():
    return "Hello World"


# Function 1:   Ben
def conv_num(num_str):
    # Verify string is valid & not empty
    if isinstance(num_str, str) is False or len(num_str) == 0:
        return None

    # Return value
    return num_str


# Function 2:   Ash
def is_leap_year(year):
    """
    :param year: Integer representing the year to check.
    :return: True if year is a leap year, otherwise False.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def my_datetime(num_sec):
    """
    :param num_sec: Integer representing the number of seconds since 01-01-1970.
    :return: A formatted string "mm-dd-yyyy" based on the number of seconds that have passed since 01-01-1970.
    """
    day_in_seconds = (24 * 60 * 60)
    year_in_seconds = (day_in_seconds * 365)
    days_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate year
    year = 1970 + (num_sec // year_in_seconds)
    num_sec %= year_in_seconds

    # Account for leap years
    leap_years_since_1970 = ((year // 4) + (year // 400) - (year // 100)) - 477

    if is_leap_year(year):
        leap_years_since_1970 -= 1

    leap_year_adjustment = divmod(leap_years_since_1970, 365)
    year -= leap_year_adjustment[0]
    num_sec += (leap_year_adjustment[0] // 4) * day_in_seconds
    num_sec -= leap_year_adjustment[1] * day_in_seconds
    if num_sec < 0:
        num_sec += year_in_seconds
        year -= 1
        if is_leap_year(year):
            num_sec += day_in_seconds

    # February has 29 days if year is a leap year
    if is_leap_year(year):
        days_each_month[1] = 29

    # Calculate month
    month = 0
    seconds_each_month = [(m * day_in_seconds) for m in days_each_month]
    while num_sec > seconds_each_month[month] and month < 11:
        num_sec -= seconds_each_month[month]
        month += 1

    # Calculate day
    day = num_sec // day_in_seconds

    return '{:02d}-{:02d}-{}'.format(1 + month, 1 + day, year)


# Function 3:    Alex
def conv_endian(num, endian='big'):
    # TODO: implement function
    return ''
