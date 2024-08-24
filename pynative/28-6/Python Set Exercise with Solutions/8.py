""" Update set1 by adding items from set2, except common items """
""" hint Use the symmetric_difference_update() method of a set. """
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
tol = set1.symmetric_difference_update(set2)
print(set1)