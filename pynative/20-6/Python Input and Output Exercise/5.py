""" Chấp nhận danh sách 5 số float làm đầu vào từ người dùng """
""" 
Expected Output:
[78.6, 78.6, 85.3, 1.2, 3.5]"""

# tao list
numbers_list = []

for number in range(5):
    user = float(input("Enter a number: "))
    numbers_list.append(user)
print(numbers_list)

