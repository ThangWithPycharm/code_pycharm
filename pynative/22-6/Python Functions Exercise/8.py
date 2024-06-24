""" Tạo danh sách Python gồm tất cả các số chẵn từ 4 đến 30 """


def list_even():
    list = []
    for i in range(4, 30):
        if i % 2 == 0:
            list.append(i)
    return list


result = list_even()
print(result)
