""" Sử dụng vòng lặp để hiển thị các phần tử từ danh sách nhất định có ở vị trí chỉ mục lẻ """
""" Given:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected output:
20 40 60 80 100  """

amount_list = int(input("amount in  a list: "))
number_list = []
for i in range(amount_list):
    number_list.append(int(input("number in  a list: ")))

for i in range(1, len(number_list), 2):
    print(number_list[i], end=" ")
