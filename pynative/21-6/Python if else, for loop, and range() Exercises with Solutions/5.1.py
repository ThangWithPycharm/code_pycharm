def display(numbers):
    list_display = []
    for number in numbers:
        if number % 5 == 0:
            if number > 150:
                continue
            if number > 500 :
                break
            list_display.append(number)
    print(list_display)

numbers = [1, 2, 3, 150, 180, 50, 50, 500]
display(numbers)