import math


def my_func():
    return "Hello World"


# Function 1:   Ben
def conv_hex(hex_str):
    """
    Convert hexadecimal string to a base 10 integer
    """
    # Remove 0x from hex string
    num_str = hex_str[2:]

    # Define integer
    integer = 0

    # Convert hexadecimal to integer & return int
    for char in num_str:
        if '0' <= char <= '9':
            integer = integer * 16 + (ord(char) - ord('0'))
        elif 'a' <= char.lower() <= 'f':
            integer = integer * 16 + (ord(char.lower()) - ord('a') + 10)
        else:
            return None
    return integer


def conv_dec(dec_str):
    """
    Convert decimal or integer string to a base 10 integer
    """
    # Define integer & decimal place variables
    integer = 0
    decimal_place = 0

    # Convert string to integer
    for char in dec_str:
        if '0' <= char <= '9':
            integer = integer * 10 + (ord(char) - ord('0'))
            # Check for decimal place
            if decimal_place > 0:
                decimal_place *= 10
        elif char == '.':
            # Check for multiple decimal places
            if decimal_place > 0:
                return None
            decimal_place = 1
        else:
            return None

    # Check if decimal, update & return integer accordingly
    if decimal_place > 0:
        return integer / decimal_place
    return integer


def conv_num(num_str):
    """
    Convert Int, float, or hexadecimal entered as a string to a base 10 integer or float.
    """
    # Verify string is valid & not empty
    if isinstance(num_str, str) is False or len(num_str) == 0:
        return None

    # Check if number is negative
    negative = False
    if num_str[0] == '-':
        negative = True
        # Start from the next character if negative
        num_str = num_str[1:]

    # Check if number is hexadecimal
    if num_str.lower().startswith('0x'):
        # Call conv_hex helper function
        integer = conv_hex(num_str)
    else:
        # Call conv_dex helper function
        integer = conv_dec(num_str)

    # Check if negative & return integer value
    if negative is True:
        return -integer
    return integer


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
    """
    Convert decimal integer to hexadecimal number, formatted as a space
    separated string of two character bytes. big or little indian may be
    specified to change the order of the bytes.
    """
    negative = False
    # check for negative and store result
    if (num < 0):
        num *= -1
        negative = True
    # check if num is 0, otherwise will cause math error
    elif (num == 0):
        return '00'
    # list of hexadecimal digits for indexing
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'A', 'B', 'C', 'D', 'E', 'F']
    # list that will hold strings for each hex byte
    hex_digits = []
    # number of hex digits
    hex_digits_num = math.floor(math.log(num, 16))
    # iterate from the largest digit down to the 0th digit
    for i in range(hex_digits_num, -1, -1):
        # value of next hex digit = (num / 16^current_digit_place) rounded down
        digit_val = math.floor(num/(16**i))
        # add digit to hex string
        hex_digits += str(digits[digit_val])
        # subtract value added to hex number from decimal number
        num -= digit_val*(16**i)
    # converts the list of hex digits to a string of bytes and returns it
    return hex_to_bytes(hex_digits, endian, negative)


def hex_to_bytes(hex_digits, endian, negative):
    """
    Compile list of hex digits into a string of bytes,
    each two characters long and space separated.
    """
    # add 0 digit at beginning if number of digits is uneven
    if (len(hex_digits) % 2 != 0):
        hex_digits.insert(0, '0')
    # hex_str which will contain the final returned string
    hex_str = '-' if negative else ''
    if (endian == 'big'):
        # add bytes in order
        for i in range(len(hex_digits)):
            hex_str += hex_digits[i]
            if (i % 2 != 0):
                hex_str += ' '
    elif (endian == 'little'):
        # add bytes in reverse order
        for i in range(len(hex_digits) - 1, -1, -1):
            if (i % 2 != 0):
                hex_str += hex_digits[i - 1]
            else:
                hex_str += hex_digits[i + 1] + ' '
    else:
        return None
    # remove trailing space
    hex_str = hex_str[:-1]
    return hex_str
