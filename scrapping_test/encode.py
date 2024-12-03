# from base64 import b64encode, b64decode
#
# client_id = "ketan"
# client_secret = "somani"
# userpass = "{0}:{1}".format(client_id, client_secret)
# encoded_userpass = b64encode(userpass.encode()).decode()
# print(encoded_userpass)
# ##################################################################
# encoded_userpass = "a2V0YW46c29tYW5p"
# decoded_userpass = b64decode(encoded_userpass).decode()
# print(decoded_userpass)
#

import ast
x=10
y = x,
print(y)
if len(y) == 1:
    list_obj = [y[0]]
else:
    list_obj = list(y)
print(list_obj)
print(type(list_obj))
print(tuple(list_obj))


