""" Mở rộng danh sách lồng nhau bằng cách thêm danh sách con """

""" 
Given List:

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
Expected Output:

['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

"""
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]
for i in range(len(sub_list)):
    list1[2][1][2].append(sub_list[i])
print(list1)
# or
print()
list1[2][1][2].extend(sub_list)
print(list1)
