""" Bài 2: Nối chuỗi mới vào giữa chuỗi đã cho """
""" Cho hai chuỗi s1 và s2. Viết chương trình tạo chuỗi mới s3 bằng cách thêm s2 vào giữa s1 """

s1 = input('enter a string: ')
s2 = input('enter another string: ')
before = int(len(s1)/2)
after = int(len(s1)/2)
before_s1 = s1[0:before]
after_s1 = s1[after+1:]
result = before_s1 + s2 + after_s1
print(result)