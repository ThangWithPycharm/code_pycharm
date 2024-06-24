""" Tìm tất cả các lần xuất hiện của chuỗi con trong một chuỗi nhất định bằng cách bỏ qua chữ hoa chữ thường """
""" Viết chương trình tìm tất cả các lần xuất hiện của “USA” trong một chuỗi 
cho trước mà không phân biệt chữ hoa chữ thường."""

def count_usa(str1):
    str1 = str1.upper()
    count = str1.count('USA')
    print('USA in str1 is', count)

str1 = 'USA, USA < USA, how do you feel today ?'
count_usa(str1)
