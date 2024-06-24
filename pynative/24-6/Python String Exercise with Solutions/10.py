""" Viết chương trình đếm số lần xuất hiện của tất cả các ký tự trong một chuỗi """
str1 = 'anfaad'
char_dict = dict()
for i in str1:
    count = str1.count(i)
    char_dict[i] = count

print(char_dict)
