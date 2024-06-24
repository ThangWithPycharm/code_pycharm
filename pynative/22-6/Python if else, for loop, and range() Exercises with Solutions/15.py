""" Sử dụng vòng lặp để hiển thị các phần tử từ danh sách nhất định có ở vị trí chỉ mục lẻ """
""" Given:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected output:
20 40 60 80 100  """

amount_list = int(input("How many numbers do you want? "))
numbers_list = []
for i in range(amount_list):
    number = int(input("Enter a number: "))
    numbers_list.append(number)
print(numbers_list[1::2])
