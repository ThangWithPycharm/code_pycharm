""" Concatenate two lists index-wise """
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
concatenate = [(a+b) for (a,b) in zip(list1, list2)]
print(concatenate)

