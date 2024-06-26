""" Thay thế mục trong danh sách bằng giá trị mới nếu tìm thấy """
""" Bạn đã đưa ra một danh sách Python. Viết chương trình tìm giá trị 20 trong danh sách, 
nếu có thì thay thế bằng 200. Chỉ cập nhật lần xuất hiện đầu tiên của một mục """

list1 = [5, 10, 15, 20, 25, 50, 20]
times_20 = 1
for i in range(len(list1)):
    if list1[i] == 20 and times_20 == 1:
        list1[i] = 200
        times_20 = times_20 - 1
print(list1)
