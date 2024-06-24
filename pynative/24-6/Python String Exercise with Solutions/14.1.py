str_list = ["list", "Nanms", None, "ta", None]
print(" original of list :", str_list)
list_removed = [i for i in str_list if i is not None]
print("new list :", list_removed)