""" Tìm tổng của chuỗi có n số hạng """
""" Viết chương trình tính tổng các chuỗi đến n. Ví dụ: nếu n =5 thì chuỗi sẽ 
trở thành 2 + 22 + 222 + 2222 + 22222 = 24690"""

n = int(input(" nhap n: "))
sum = 0
for i in range(1,n+1):
    int_2 = '2'*i
    sum = sum + int(int_2)
print(sum)
