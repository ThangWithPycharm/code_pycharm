""" Kiểm tra xem json sau có hợp lệ hay không hợp lệ. Nếu không hợp lệ hãy sửa nó """
import json
def isValid(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True
sample_json = """{
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
confirm = isValid(sample_json)
print(confirm)


