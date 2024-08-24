""" Generate a random Password which meets the following conditions """
""" Password length must be 10 characters long.
It must contain at least 2 upper case letters, 1 digit, and 1 special symbol. """

import random
import string


def get_string(upper_count, digit_count, punct_count):
    letter = ''.join(random.choice(string.ascii_letters) for _ in range(10 - upper_count - digit_count - punct_count))
    upper = ''.join(random.choice(string.ascii_uppercase) for _ in range(upper_count))
    digit = ''.join(random.choice(string.digits) for _ in range(digit_count))
    punct = ''.join(random.choice(string.punctuation) for _ in range(punct_count))
    sample_list = list(letter + upper + digit + punct)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    print(final_string)


get_string(2, 3, 5)
