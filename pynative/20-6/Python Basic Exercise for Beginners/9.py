""" Kiểm tra số Palindrome """
""" Một số đối xứng là một số mà vẫn như cũ sau khi đảo ngược. Ví dụ, 545, là các số đối xứng. """


def is_palindrome(numbers):
    if numbers[0] == numbers[-1]:
        print('yes. given number is palindrome')
    else:
        print('no. given number is not palindrome')

numbers=input('Enter numbers: ')
is_palindrome(numbers)