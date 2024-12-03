import boto3
from boto3.dynamodb import conditions
from boto3.dynamodb.conditions import Attr, Key
from botocore.exceptions import ClientError

resource = boto3.resource("dynamodb",
                          region_name="us-east-1"
                          )
# ############ Read Table ###################
table = resource.Table("dr-deals-lab")
print(table)
data = table.query(
    KeyConditionExpression=Key("dealRefId").eq("01GRYB09S3NXMJ6WBCZAWCW70F"),
    FilterExpression=(Attr("apiVersion").exists()
                      | Attr("creditAppId").exists()
                      | Attr("leadRefID").exists()
                      | Attr("provider").exists()
                      )
).get("Items")

# No Filter Expression then get all Items
# data = table.query(
#     KeyConditionExpression=Key("dealRefId").eq("01GRYB09S3NXMJ6WBCZAWCW70F")
# ).get("Items")

print(data)
