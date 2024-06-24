""" Write a program to print multiplication table of a given number """
""" For example, num = 2 so the output should be
2
4
6
8
10
12
14
16
18
20 """

table_number = int(input("Enter a number: "))
for i in range(1, 11):
    print(table_number * i)
    print(f"{i} x {table_number} = {i*table_number}")