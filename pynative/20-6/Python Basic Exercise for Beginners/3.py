"""Viết chương trình nhận một chuỗi từ người dùng và hiển thị các ký tự có số chỉ mục chẵn"""
'''Sử dụng hàm input() của Python để chấp nhận một chuỗi từ người dùng.
Tính độ dài của chuỗi bằng hàm len()
Tiếp theo, lặp lại từng ký tự của chuỗi bằng cách sử dụng hàm for loop và range(). 
Sử dụng bắt đầu = 0, dừng = len(s)-1 và bước =2. bước này là 2 vì chúng tôi chỉ muốn các số chỉ mục chẵn
Trong mỗi lần lặp của vòng lặp, hãy sử dụng s[i] để in các ký tự có ở số chỉ mục chẵn hiện tại'''

user = input('please enter origin name: ')
for i in range(0, len(user) + 1, 2):
    print('index even name', user[i])
