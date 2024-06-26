""" Xóa tất cả các lần xuất hiện của một mục cụ thể khỏi danh sách. """
""" Cho một danh sách Python, viết chương trình loại bỏ tất cả các lần xuất hiện của mục 20."""

list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if i == 20:
        list1.remove(i)
print(list1)

# or
print()
list1 = [i for i in list1 if i != 20]
print(list1)
