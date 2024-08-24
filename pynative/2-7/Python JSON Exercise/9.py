""" Phân tích cú pháp JSON sau đây để nhận tất cả các giá trị của 'tên' khóa trong một mảng """

data = [
    {
        "id": 1,
        "name": "name1",
        "color": [
            "red",
            "green"
        ]
    },
    {
        "id": 2,
        "name": "name2",
        "color": [
            "pink",
            "yellow"
        ]
    }
]

name = [item['name'] for item in data]
print(name)
