import boto3
import json
import urllib.parse

sf_client = boto3.client("stepfunctions")


def lambda_handler(event, context):
    print("input", event)
    try:
        query_params = event["queryStringParameters"]
        encoded_token = query_params["token"]
        decoded_token = urllib.parse.unquote(encoded_token)
        status = query_params["status"]

        if status == "success":
            sf_client.send_task_success(taskToken=decoded_token, output=json.dumps({"status": "success"}))
        else:
            sf_client.send_task_failure(taskToken=decoded_token)

        response = {"statusCode": 200, "body": "SF workflow resumed", "headers": {"Content-Type": "application/json"},
                    "isBase64Encoded": False}
        print("response", response)
        return response

    except Exception as error:
        print(error)
        response = {
            "statusCode": 500,
            "body": "{\"message\":\"Internal Server Error\"}",
            "headers": {
                "Content-Type": "application/json"
            },
            "isBase64Encoded": False
        }
        print("response", response)
        return response
