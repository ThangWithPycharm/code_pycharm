""" Count all letters, digits, and special symbols from a given string """


def count_letters():
    str1 = input("Enter a string: ")
    chars = 0
    digits = 0
    special = 0
    for letter in str1:
        if letter.isalpha():
            chars += 1
        elif letter.isdigit():
            digits += 1
        else:
            special += 1
    print("Number of chars: ", chars)
    print("Number of digits: ", digits)
    print("Number of special: ", special)


(count_letters())
