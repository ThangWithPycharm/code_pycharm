""" Add a list of elements to a set """
""" Given a Python list, Write a program to add all its elements into a given set """
# using update function
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(set(sample_list))
print(sample_set)
