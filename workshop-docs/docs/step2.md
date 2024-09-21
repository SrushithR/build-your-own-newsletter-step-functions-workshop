# Step 2: Fetch Subscribers and Send Email

## 1. Create the DynamoDB Table `newsletter-subs`
1. Navigate to the **DynamoDB** service in the AWS Management Console.
2. Click **Create Table**.
3. Set the **Table name** to `newsletter-subs`.
4. Set the **Primary key** to `email` (String).
5. Configure any additional settings as needed, then click **Create table**.

## 2. Create the `fetch_subscribers` Lambda function
1. Navigate to the **Lambda** service in the AWS Management Console.
2. Click **Create function** and choose the **Author from scratch** option.
3. Name the function `fetch_subscribers`.
4. Select a runtime, such as **Python 3.12** *.
5. In the code editor, copy the function from [here](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/lambda-functions/fetch_subscribers.py) to query the `newsletter-subs` DynamoDB table and return the list of subscribers.
6. Under **Permissions**, use the IAM role created in Step 1 (with permissions to access DynamoDB).
7. Click **Deploy**.

## 3. Create Step 2 SF (Fetch from DDB + Send Email)
1. Go to the **Step Functions** service in the AWS Management Console.
2. Click on **Create state machine**.
3. In the state machine definition, add the following tasks as [json](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/step-functions/step2.json)
4. Name the state machine (e.g., `FetchAndSendStateMachine`), review, and create it.

## 4. Create the `send_email_v2` Lambda function
1. Navigate to the **Lambda** service in the AWS Management Console.
2. Click **Create function** and choose the **Author from scratch** option.
3. Name the function `send_email_v2`.
4. Select a runtime, such as **Python 3.12** .
5. In the code editor, copy the function from [here](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/lambda-functions/send_email_v2.py)
6. Under **Permissions**, use the IAM role created in Step 1 (with permissions to send emails).
7. Click **Deploy**.

> **Note:** The IAM role permission created in Step 1 can be reused for both the `fetch_subscribers` and `send_email_v2` Lambda functions.