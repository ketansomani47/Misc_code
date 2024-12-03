# import xmltodict
# import json
#
# obj = xmltodict.parse(None)
# dict1 = obj
# # dict1 = json.dumps(obj)
# print(dict1)
# if dict1:
#     if type(dict1["Partners"]['PartnerId']) == list:
#         print(dict1["Partners"]['PartnerId'])
#         print([{"partnerId": i} for i in dict1["Partners"]['PartnerId']])
#     else:
#         print([{"partnerId": dict1["Partners"]['PartnerId']}])
# else:
#     print("nothing")

from enum import Enum


class EnrollmentId(Enum):
    RA = "RA"
    AAR = "AAR"
    PI = "PI"


print(EnrollmentId)
print(list(EnrollmentId))
print(EnrollmentId.RA.value)
print(list(EnrollmentId._value2member_map_.keys()))

