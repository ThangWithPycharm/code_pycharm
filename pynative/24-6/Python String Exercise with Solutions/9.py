""" Tính tổng và trung bình cộng các chữ số có trong chuỗi """
""" Cho chuỗi s1, viết chương trình trả về tổng và trung bình cộng của các chữ số xuất hiện trong chuỗi, 
bỏ qua tất cả các ký tự khác """

def sum_average(str1):
    sum = 0
    len_digit = 0
    for i in str1:
        if i.isdigit():
            len_digit += 1
            sum = sum + int(i)
    if len_digit > 0 :
        average = sum/len_digit
    else:
        average = 0
    print('sum is', sum)
    print('average', average)

sum_average('adf10234jg#$')