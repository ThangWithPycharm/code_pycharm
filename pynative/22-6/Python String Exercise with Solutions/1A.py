""" Tạo một chuỗi gồm ký tự đầu tiên, giữa và cuối cùng """
""" Given:

str1 = "James"
Expected Output:

Jms
 
"""

str1 = input('Enter a string: ')
for  i in range(len(str1)):
    first = str1[0]
    last = str1[-1]
    middle = str1[len(str1)//2]
print(first,middle,last, sep='')

