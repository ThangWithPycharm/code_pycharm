""" Concatenate two lists in the following order """
""" 
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir'] """

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list_expect = []
for i in list1:
    for j in list2:
        list_expect.append(i+j)
print(list_expect)

# or
res = [x + y for x in list1 for y in list2]
print(res)