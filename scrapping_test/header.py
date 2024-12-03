headers = {"x-CoxAuto-Correlation-Id": "ketan",
           "Content-Type": "application/json"}
CORRELATION_ID_HEADER_KEY = "X-CoxAuto-Correlation-Id"
# data = map(lambda x: x if x.lower() == CORRELATION_ID_HEADER_KEY.lower() else "no", headers.keys())
# print(list(data))
data1 = {"X-CoxAuto-Correlation-Id": "ketan",
        "x-coxauto-correlation-id": "ketan",
           "Content-Type": "application/json"}
event = dict()
event["headers"] = headers
headers = event["headers"].copy()
print(headers)
# data2 = map(lambda x,y: headers[x] if headers[x].lower() == CORRELATION_ID_HEADER_KEY.lower(), headers)
data2 = map(lambda d: {'content': d['content'].lower()}, headers)
# for k, v in headers.items():
#     event["headers"][k.lower()] = v
# print(event["headers"])
print(dict(data2))
