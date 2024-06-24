""" Reverse a given integer number """

number = int(input("Enter a number: "))
if number < 0:
    number = " - " + str(number)[:0:-1]
    print(number)
else:
    number = str(number)[::-1]
    print(number)
