import math

def my_func():
    return "Hello World"


# Function 1:   Ben
def conv_num(num_str):
    # ADD MORE CODE!
    return num_str


# Function 2:   Ash


# Function 3:    Alex
def conv_endian(num, endian='big'):
    """
    Convert decimal integer to hexadecimal number, formatted as a space
    separated string of two character bytes. big or little indian may be
    specified to change the order of the bytes.
    """
    negative = False
    # check for negative and store result
    if(num < 0):
        num *= -1
        negative = True
    # check if num is 0, otherwise will cause math error
    elif (num == 0):
        return '00'
    # list of hexadecimal digits for indexing
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
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
    # compile list of digits into a string of bytes
    # add 0 digit at beginning if number of digits is uneven
    if(len(hex_digits) % 2 != 0):
        hex_digits.insert(0, '0')
    # hex_str which will contain the final returned string
    hex_str = '-' if negative else ''
    if(endian == 'big'):
        # add bytes in order
        for i in range(len(hex_digits)):
            hex_str += hex_digits[i]
            if(i % 2 != 0):
                hex_str += ' '
    elif(endian == 'little'):
        # add bytes in reverse order
        for i in range(len(hex_digits) - 1, -1, -1):
            if(i % 2 != 0):
                hex_str += hex_digits[i - 1]
            else:
                hex_str += hex_digits[i + 1] + ' '
    else:
        return None
    # remove trailing space
    hex_str = hex_str[:-1]
    return hex_str