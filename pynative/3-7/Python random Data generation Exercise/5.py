""" Generate random String of length 5 """
""" Note: String must be the combination of the UPPER case and lower case letters only. 
No numbers and a special symbol. """
import random
import string


def get_radom_string(length):
    result = ''.join(random.choice(string.ascii_letters) for i in range(length))
    print(result)


get_radom_string(5)
get_radom_string(5)
    