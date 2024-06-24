""" Sắp xếp các ký tự chuỗi sao cho chữ cái viết thường đứng trước """
""" Chuỗi đã cho chứa sự kết hợp của chữ thường và chữ in hoa. Viết chương trình sắp xếp các ký tự trong 
chuỗi sao cho tất cả các chữ cái viết thường đều đứng trước """

list_lower = []
list_upper = []
str1 = str(input("Enter a string: "))
for i in str1:
    if i.islower():
        list_lower.append(i)
    else:
        list_upper.append(i)
result = ''.join(list_lower + list_upper)
print(result)


