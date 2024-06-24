""" Xóa các chuỗi trống khỏi danh sách các chuỗi """
str_list = ["Emma", "is", "beautiful", None, "girl", None, "!!!"]
print(" original of list ", str_list)
for i in str_list[:]:
    if i is None:
        str_list.remove(i)
print(str_list)
