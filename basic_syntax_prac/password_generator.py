
import random
import string

_digit = string.digits
_letter = string.ascii_letters
_letter_table = list(_digit + _letter)
random.shuffle(_letter_table)

_length = int(input("password digit? "))
_password = "".join(_letter_table[:_length])
print(f"random password: {_password}")
