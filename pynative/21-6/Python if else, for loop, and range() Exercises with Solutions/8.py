""" Print list in reverse order using a loop """
""" list1 = [10, 20, 30, 40, 50]
Expected output:

50
40
30
20
10 """

list1 = [10, 20, 30, 40, 50]
for i in reversed(range(len(list1))):
    print(list1[i])