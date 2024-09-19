import boto3

ses = boto3.client('sesv2')

function_url = ""


def lambda_handler(event, context):
    """
    Lambda function to trigger an email
    Sample Input:
        {
          "subject": "Subject",
          "content": "Content"
        }
    """
    print("input to the lambda", event)
    task_token = event["task_token"]
    subject = event["subject"]
    content = event["content"]

    approve_url = f"{function_url}?status=success&token={task_token}"
    reject_url = f"{function_url}?status=reject&token={task_token}"

    ses.send_email(
        FromEmailAddress="<>",  # TODO: add your configured sender email address
        Destination={
            'ToAddresses': [""]  # TODO: update with admin email ID
        },
        Content={
            'Simple': {
                'Subject': {
                    'Data': subject,
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Html': {
                        'Data': content + f"<br>Approve: {approve_url}<br><br>" + f"<br>Approve: {reject_url}<br><br>",
                        'Charset': 'UTF-8'
                    }
                }
            }
        }
    )
    return "Approval email sent successfully"
