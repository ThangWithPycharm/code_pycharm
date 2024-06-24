""" Xóa các ký hiệu/dấu chấm câu đặc biệt khỏi chuỗi """
import re
str1 = " #luong /duc .,@thang"
print('original string :', str1)
string_nnew = re.sub(r"[^\s\w]","", str1)
print(string_nnew)