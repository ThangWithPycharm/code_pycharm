""" Lặp lại cả hai danh sách cùng một lúc """
""" Đưa ra một danh sách hai Python. Viết chương trình lặp lại đồng thời cả hai danh sách và 
hiển thị các mục từ list1 theo thứ tự ban đầu và các mục từ list2 theo thứ tự ngược lại"""
""" Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:

10 400
20 300
30 200
40 100"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i in range(len(list1)):
    print(list1[i], list2[-(i + 1)])

# or
print()
for i, j in zip(list1, list2[::-1]):
    print(i, j) 
