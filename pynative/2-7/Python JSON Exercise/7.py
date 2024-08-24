""" Convert the following JSON into Vehicle Object """

import json
from types import SimpleNamespace
vehicle_json = { "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }
vehicle_json = json.dumps(vehicle_json)
object_python = json.loads(vehicle_json, object_hook=lambda d: SimpleNamespace(**d))
print(object_python.name, object_python.engine, object_python.price)

