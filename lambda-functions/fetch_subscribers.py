import boto3

dynamodb = boto3.resource("dynamodb")
DDB_TABLE = dynamodb.Table("newsletter-subs")


def lambda_handler(event, context):
    response = DDB_TABLE.scan()
    subscribers = []
    for record in response["Items"]:
        print("record", record)
        subscribers.append(record["email_id"])
    return {"subscribers": subscribers}
