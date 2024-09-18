import boto3

ses = boto3.client('sesv2')


def lambda_handler(event, context):
    """
    Lambda function to trigger an email
    Sample Input:
        {
          "email_ids": [{"email_id": "1@gmail.com"}, {"email_id": "2@gmail.com"}],
          "subject": "Welcome to the workshop",
          "content": "<p>Hello there again!</p>"
        }
    """
    print("input to the lambda", event)
    email_ids = [e["email_id"]["S"] for e in event["email_ids"]]
    subject = event["subject"]
    content = event["content"]

    ses.send_email(
        FromEmailAddress="<>",  # TODO: add your configured sender email address
        Destination={
            'ToAddresses': email_ids
        },
        Content={
            'Simple': {
                'Subject': {
                    'Data': subject,
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Html': {
                        'Data': content,
                        'Charset': 'UTF-8'
                    }
                }
            }
        }
    )
    return "Email sent successfully"
