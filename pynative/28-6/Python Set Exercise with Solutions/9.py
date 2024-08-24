""" Xóa các mục khỏi set1 không phổ biến cho cả set1 và set2 """
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)