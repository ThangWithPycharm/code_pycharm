""" Tạo một chuỗi gồm ba ký tự ở giữa """
str1 = input('Enter a string: ')
if len(str1) < 3:
    print('Too short')
else:
    middle1 = str1[(len(str1)//2)-1]
    middle2 = str1[(len(str1)//2)]
    middle3 = str1[(len(str1)//2)+1]

    result = middle1 + middle2 + middle3
    print(result)
