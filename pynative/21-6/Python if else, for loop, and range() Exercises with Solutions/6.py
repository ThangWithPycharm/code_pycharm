""" Count the total number of digits in a number """
""" For example, the number is 75869, so the output should be 5 """

count = 0
number = int(input("Enter a number: "))
while number != 0:
    number = number // 10
    count = count + 1
print(f"There are {count} digits in total."'')

