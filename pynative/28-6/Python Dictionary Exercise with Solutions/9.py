""" Get the key of a minimum value from the following dictionary """
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

value_dict = [i for i in sample_dict.values()]
print(min(value_dict))

key_min = min(sample_dict, key=sample_dict.get)
print(key_min)
