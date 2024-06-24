# sử dụng list comprehension
str1 = "luong duc thang 24 03 2004"
str_int = ''.join([i for i in str1 if i.isnumeric()])
print(str_int)