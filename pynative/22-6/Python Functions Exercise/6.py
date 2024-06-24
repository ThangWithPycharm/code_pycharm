""" Tạo hàm đệ quy """
""" Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again and again """


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


result = sum(10)

print(result)
