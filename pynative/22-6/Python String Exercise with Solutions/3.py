""" Bài tập 3: Tạo một chuỗi mới gồm các ký tự đầu tiên, giữa và cuối của mỗi chuỗi đầu vào """
""" Cho hai chuỗi s1 và s2, viết chương trình trả về một chuỗi mới gồm các ký tự đầu, giữa và cuối của s1 và s2 """
""" Given:

s1 = "America"
s2 = "Japan"
Expected Output:

AJrpan

"""
def connect():
    s1 = input('enter a string : ')
    s2 = input('enter a string : ')
    result = s1[0] + s2[0] + s1[int(len(s1)//2)] + s2[int(len(s2)//2)] + s1[-1] + s2[-1]
    return result

display = connect()
print(display)