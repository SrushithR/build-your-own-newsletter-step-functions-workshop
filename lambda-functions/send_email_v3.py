import boto3

ses = boto3.client('sesv2')


def lambda_handler(event, context):
    """
    Lambda function to trigger an email
    Sample Input:
        {
          "email_id": "abc@gmail.com",
          "subject": "Subject",
          "content": "Content"
        }
    """
    print("input to the lambda", event)
    email_ids = event["email_id"]
    subject = event["subject"]
    content = event["content"]

    ses.send_email(
        FromEmailAddress="<>",  # TODO: add your configured sender email address
        Destination={
            'ToAddresses': [email_ids]
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
