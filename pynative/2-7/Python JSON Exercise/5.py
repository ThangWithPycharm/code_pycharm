""" Access the nested key ‘salary’ from the following JSON """""

import json

sampleJson = """{ 
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

print(" check itt")
display = json.loads(sampleJson)
print(display)
dict_json = display["company"]["employee"]["payble"]["salary"]
print("salary", dict_json)
