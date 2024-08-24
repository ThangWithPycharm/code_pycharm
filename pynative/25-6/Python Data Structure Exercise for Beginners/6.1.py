first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

duplicate = first_set.intersection(second_set)
for i in duplicate:
    first_set.remove(i)

print(duplicate)
print(first_set)

