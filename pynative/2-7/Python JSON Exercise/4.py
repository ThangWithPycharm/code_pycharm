""" Sắp xếp các khóa JSON và ghi chúng vào một tệp """""
"""Sắp xếp dữ liệu JSON theo thứ tự bảng chữ cái của các khóa """

import json

sampleJson = {"id": 1, "name": "value2", "age": 29}
display = json.dumps(sampleJson, indent=2, sort_keys=True)
print(display)
