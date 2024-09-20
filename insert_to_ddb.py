import boto3

table_name = "newsletter-subs"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)


def insert_strings_to_dynamodb(email_ids):
    """
    Inserts an array of strings into a DynamoDB table.

    Args:
      email_ids: The array of strings to be inserted.
    """
    for string in email_ids:
        table.put_item(
            Item={
                "email_id": string
            }
        )

    print(f"Inserted {len(email_ids)} strings into DynamoDB table: {table_name}")


strings_to_insert = ["srush007@gmail.com"]
insert_strings_to_dynamodb(strings_to_insert)
