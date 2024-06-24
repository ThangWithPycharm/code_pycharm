""" Viết chương trình trích xuất từng chữ số của một số nguyên theo thứ tự ngược lại. """
""" For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits """

def reverse(numbers):
        number_str = str(numbers)
        numbers_reverse = number_str[::-1]
        for i in numbers_reverse:
            print(i, end = ' ')


reverse(2030)