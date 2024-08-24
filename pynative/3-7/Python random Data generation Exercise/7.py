""" Calculate multiplication of two random float numbers
Note:

First random float number must be between 0.1 and 1
Second random float number must be between 9.5 and 99.5 """

import random

first = random.random()
second = random.uniform(9.5, 99.5)
multiplication = first * second
print(f"Calculate multiplication of two random float numbers {first} * {second} = {multiplication}")
