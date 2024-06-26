""" Xóa các chuỗi trống khỏi danh sách các chuỗi """
""" list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

Expected output:

["Mike", "Emma", "Kelly", "Brad"] """

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1:
    if len(i) == 0:
        list1.remove(i)
print(list1)

#
print()
for i in list1:
    if i.isspace():
        list1.remove(i)
print(list1)
