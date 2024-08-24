"""  PrettyPrint following JSON data  """
""" PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").

sampleJson = {"key1": "value1", "key2": "value2"}
Expected Output:

{
  "key1" = "value2",
  "key2" = "value2",
  "key3" = "value3"
}
"""
import json

sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}

display = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(display)
