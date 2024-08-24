""" Rename key of a dictionary """
"Write a program to rename a key city to a location in the following dictionary"
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
if "city" in sample_dict.keys():
    sample_dict.pop("city")
    sample_dict.update({"location": "New york"})
print(sample_dict)
