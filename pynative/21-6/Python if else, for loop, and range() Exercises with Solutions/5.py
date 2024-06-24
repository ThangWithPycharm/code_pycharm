""" Display numbers from a list using loop """
""" Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop  """


def display(numbers):
    list_display = []
    for number in numbers:
        if number % 5 == 0 and number <= 150:
            list_display.append(number)
        elif number >= 500:
            break

    print(list_display)


numbers = [1, 2, 3, 150, 180, 50, 50, 500]
display(numbers)
