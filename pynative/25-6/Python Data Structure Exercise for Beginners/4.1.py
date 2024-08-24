list1 = [10, 30, 12, 34, 5, 5, 12, 30]
dict_list = {}
for i in list1:
    if i in dict_list:
        dict_list[i] += 1
    else:
        dict_list[i] = 1
print(dict_list)