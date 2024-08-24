"""  HINT
Lặp lại các khóa được đề cập bằng vòng lặp
Tiếp theo, kiểm tra xem khóa hiện tại có trong từ điển hay không, nếu có, hãy thêm nó vào từ điển mới """
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
# Keys to extract
keys = ["name", "salary"]
dict_n = dict()
for k in keys:
    dict_n.update({k: sample_dict[k]})
print(dict_n)
print()
new_dict = {k: sample_dict[k] for k in keys}
[print(new_dict)]
