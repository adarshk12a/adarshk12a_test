##
import json

data = {"key1" : "value1", "key2" : "value2"}

jsondata= json.dumps(data)
print(jsondata)

sampleJson = """{"key1": "value1", "key2": "value2"}"""

json_dict= json.loads(sampleJson)
print(json_dict)