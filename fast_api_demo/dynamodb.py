import boto3
from boto3.dynamodb import conditions
from boto3.dynamodb.conditions import Attr, Key
from botocore.exceptions import ClientError

resource = boto3.resource("dynamodb",
                          region_name="us-east-1"
                          )
print(resource)
# ###### All table list #################3
# print(list(resource.tables.all()))

# ################# Table Creation #########################
# ct = resource.create_table(TableName='Test-Ketan', KeySchema=[
#         {
#             'AttributeName': 'name',
#             'KeyType': 'HASH'  #Partition key
#         },
#         {
#             'AttributeName': 'email',
#             'KeyType': 'RANGE'  #Sort key
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'name',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'email',
#             'AttributeType': 'S'
#         },
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 10,
#         'WriteCapacityUnits': 10
#     }
# )
# print(ct)
# print(ct.table_status)

# ############ Read Table ###################
table = resource.Table("Test-Ketan")
print(table)


# ############ Add Items #######################
# table.put_item(Item={"name": "test", "email": "test@test.com"})
# table.put_item(Item={"name": "test1", "email": "test1@test.com"})
# table.put_item(Item={"name": "test2", "email": "test2@test.com"})


# ############# Read Single Items ###########################
# @@@@ success case gives Item key in response
# data = table.get_item(Key={"name": "test", "email": "test@test.com"})
# print(data)
# @@@@ failure case not received any Item key in response
# data = table.get_item(Key={"name": "test2", "email": "test@test.com"})
# print(data)

# ################ Read All Items ###########
# data = table.scan()
# print(data)

# ######### update item ##########
# @@@@@ adding more data with key value pair
# data = table.update_item(Key={"name": "test3", "email": "test3@test.com"},
#                          UpdateExpression="set department=:d, age=:a",
#                          ExpressionAttributeValues={":a": 22, ":d": "IT"},
#                          ReturnValues="UPDATED_NEW"
#                          )
# print(data)

# @@@@ adding more data in dict format
# try:
#     # Not Worked
#     # data = table.update_item(Key={"name": "test2", "email": "test2@test.com"},
#     #                          ExpressionAttributeNames={
#     #                              "#address": "address",
#     #                              "#city": "city",
#     #                              "#state": "state"
#     #                          },
#     #                          ExpressionAttributeValues={":c": "KSG", ":s": "RJ"},
#     #                          UpdateExpression="set #address.#city=:c, #address.#state=:s"
#     #                          )
#
#     # Not Worked
#     # data = table.update_item(Key={"name": "test2", "email": "test2@test.com"},
#     #                          ExpressionAttributeNames={
#     #                              "#city": "city",
#     #                              "#state": "state"
#     #                          },
#     #                          ExpressionAttributeValues={":c": "KSG", ":s": "RJ"},
#     #                          UpdateExpression="set address.#city=:c, address.#state=:s"
#     #                          )
#
#     # Worked
#     # data = table.update_item(Key={"name": "test2", "email": "test2@test.com"},
#     #                          ExpressionAttributeNames={
#     #                              "#address": "address",
#     #                          },
#     #                          ExpressionAttributeValues={":a": {"city": "KSG", "state": "RJ"}},
#     #                          UpdateExpression="set #address=:a"
#     #                          )
#     # print(data)
# except ClientError as e:
#     print(e.response)

# ########### delete item #########
# data = table.delete_item(Key={"name": "test3", "email": "test4@test.com"})
# print(data)


# ######### Query Item ############3
# @@@@@@@ for exact match
# data = table.query(KeyConditionExpression=Key("name").eq("test"))
# print(data)

# @@@@@@ for appropriate match
# data = table.query(KeyConditionExpression=Key("name").begins_with("test"))
# print(data)
