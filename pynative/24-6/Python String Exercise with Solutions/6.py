""" Tạo một chuỗi hỗn hợp bằng cách sử dụng các quy tắc sau """
""" Cho hai chuỗi s1 và s2. Viết chương trình tạo một chuỗi mới s3 được tạo từ char đầu tiên của s1, 
sau đó là char cuối cùng của s2, Tiếp theo, char thứ hai của s1 và char cuối cùng thứ hai của s2, v.v. 
Mọi ký tự còn sót lại sẽ ở cuối kết quả. """

def contribute():
    str1 = input("enter a string: ")
    str2 = input("enter a string: ")
    result = []
    len1,len2 = len(str1), len(str2)
    min_len = min(len1,len2)
    for i in range(min_len):
        result.append(str1[i])
        result.append((str2[-(i+1)]))
    if min_len < len1:
        result.extend(str1[min_len:])
    if min_len < len2:
        result.extend(str2[:len2-min_len])
    print(''.join(result))
contribute()




