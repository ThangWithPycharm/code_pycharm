""" Tìm giai thừa của một số đã cho """
""" Viết chương trình sử dụng vòng lặp để tìm giai thừa của một số cho trước.
Giai thừa (ký hiệu: !) có nghĩa là nhân tất cả các số nguyên từ số đã chọn xuống 1 

"""


def display_giai_thua(n):
    total = 1
    for i in range(n, 0, -1):
        total = total * i
        if i > 1:
            print(i, end="*")
        if i <= 1:
            print(i, end=" ")
    print('=', total)


display_giai_thua(5)
