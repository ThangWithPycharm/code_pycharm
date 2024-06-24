""" Xóa tất cả các ký tự khỏi chuỗi ngoại trừ số nguyên """
str1 = " luong duc thang 24 03 2004 "
str_int = []
for i in str1:
    if i.isnumeric():
        str_int.append(i)
print(''.join(str_int))