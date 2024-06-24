"""hiển thị các số chia hết cho 5 từ danh sách"""
''' Lặp lại danh sách các số đã cho và chỉ in những số chia hết cho 5 '''


def list_five(numbers):
    for i in numbers:
        if i % 5 == 0:
            print(i)


numbersl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 20]
print('given list is :', numbersl)
list_five(numbersl)
