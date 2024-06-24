"""  Write a program to display all prime numbers within a range """
"""Lưu ý: Số nguyên tố là một số không thể được tạo ra bằng cách nhân các số nguyên khác. Số nguyên tố là số tự nhiên 
lớn hơn 1 không phải là tích của hai số tự nhiên nhỏ hơn"""
"""
Examples:
6 is not a prime mumber because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply together to make it
Given:

# range
start = 25
end = 50
Expected output:

Prime numbers between 25 and 50 are:
29
31
37
41
43
47
"""
import math
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True
start = 2
end = 50
for i in range(start, end + 1):
    if is_prime(i):
        print(i)


