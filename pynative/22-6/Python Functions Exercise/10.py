""" Tìm mục lớn nhất từ ​​một danh sách nhất định """


def max():
    x = [1, 2, 30, 4, 5, 10, 9, 7]
    num_max = 0
    for i in range(len(x)):
        if num_max < x[i]:
            num_max = x[i]
    return num_max


result = max()
print(result)
