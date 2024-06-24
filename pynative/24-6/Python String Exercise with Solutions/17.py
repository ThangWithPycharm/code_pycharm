""" Tìm từ có cả bảng chữ cái và số """
str1 = " luong24 thang 2403abc "
print(' original string: ' + str1)
res = []
list_str = str1.split()
print(list_str)
for i in list_str:
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        res.append(i)
print(res)