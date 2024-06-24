""" Kiểm tra cân bằng ký tự chuỗi """
""" Viết chương trình kiểm tra xem hai chuỗi có cân bằng hay không. Ví dụ: chuỗi s1 và s2 được cân bằng 
nếu tất cả các ký tự trong s1 đều có trong s2. Vị trí của nhân vật không quan trọng"""

def different(s1,s2):
    for i in s1:
        if i not in s2:
            return False
    return True

print(different('nag','thang13'))