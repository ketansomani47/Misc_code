import json
x = {
    "key1": "value1",
    "key2": [1, 2],
    "key3": {"flag": False}
}
print(json.dumps(x))
