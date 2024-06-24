""" Thay thế từng ký hiệu đặc biệt bằng # trong chuỗi sau """
import string
str1 = " thang@123 thang*& thang45,"
char = "#"
for i in string.punctuation:
    str1 = str1.replace(i, char)
print(str1)