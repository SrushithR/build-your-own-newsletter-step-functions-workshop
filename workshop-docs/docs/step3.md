# Step 3: Direct Integration with DynamoDB and Send Email

## 1. Create Step 3 SF (Direct Integration with DynamoDB + Send Email)
1. Go to the **Step Functions** service in the AWS Management Console.
2. Click on **Create state machine**.
3. In the state machine definition,add code from [here as json](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/step-functions/step3.json)
4. Name the state machine (e.g., `DDBDirectAndSendEmailStateMachine`), review, and create it.

## 2. Create the `send_email_v3` Lambda function
1. Navigate to the **Lambda** service in the AWS Management Console.
2. Click **Create function** and choose the **Author from scratch** option.
3. Name the function `send_email_v3`.
4. Select a runtime, such as **Python 3.12**.
5. In the code editor, you can copy the code from [here](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/lambda-functions/send_email_v3.py)
6. Under **Permissions**, use the IAM role created in Step 1 (with permissions to send emails).
7. Click **Deploy**.

> **Note:** The IAM role permission created in Step 1 can be reused for the `send_email_v3` Lambda function as well.
