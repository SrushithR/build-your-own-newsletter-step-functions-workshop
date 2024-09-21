 [step1.json](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/step-functions/step1.json)

# Step Function Workshop: Step 1 creating a basic workflow to send email.


## 1. Create the IAM Role with Permissions and Trust Policy
1. Navigate to the **IAM** service in the AWS Management Console.
2. Click on **Roles** in the left-hand menu, then click **Create role**.
3. Add a custom **trust policy** that allows Lambda to assume this role add it from [here] (https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/iam/trust_policy.json)
4. Add a role from copy from [here](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/iam/permissions.json)
5. Name the role (e.g., `LambdaSendEmailRole`) and finish creating the role.

## 1. Create the `send_email` Lambda function
1. Open the AWS Management Console and navigate to the **Lambda** service.
2. Click **Create function** and choose the **Author from scratch** option.
3. Name the function `send_email`.
4. Select a runtime, such as **Python 3.12**.
5. Under **Permissions**, create or choose an existing execution role that grants the Lambda function access to send emails (SES or a similar service).
6. In the code editor, write a function that sends an email copy it from [here](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/lambda-functions/send_email.py).
7. Click **Deploy** after writing the code.

## 2. Verify Email in Amazon SES
1. Navigate to the **Amazon SES** service in the AWS Management Console.
2. In the left-hand menu, select **Email Addresses**.
3. Click **Verify a New Email Address** and enter the email address from which you'll be sending emails.
4. Click **Verify This Email Address**. An email will be sent to that address.
5. Open the email and click the verification link to confirm.
6. After verification, your email address will be marked as **verified** in the SES console, allowing you to send emails from this address.

## 4. Create Step 1 SF (Send Email Step)
1. Go to the **Step Functions** service in the AWS Management Console.
2. Click on **Create state machine**.
3. Choose a **Standard**
4. In the state machine definition, you can select option as shown in demo or copy this as json from [here](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/step-functions/step1.json):
5. Name the state machine (e.g., `SendEmailStateMachine`), review, and create it.
