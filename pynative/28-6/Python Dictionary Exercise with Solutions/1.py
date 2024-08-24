""" Convert two lists into a dictionary """
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_1 = zip(keys,values)
print(dict(dict_1))

# Solution 2: Using a loop and update() method of a dictionary

res_dict = {}
for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)
