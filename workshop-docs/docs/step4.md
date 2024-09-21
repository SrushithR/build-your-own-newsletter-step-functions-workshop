
Now that we have our core setup ready, lets try to make it scalable. We will use the `Map` state in the `Inline` mode to loop through the email addresses fetched from DynamoDB. But before we proceed further, lets first create a new lambda function that can process individual emails. For this part of the workshop, please follow these steps:

### Step 1: Create V3 of the send_email lambda function

Since we are going to leverage the `Map` state and iterate over the email addresses received from DynamoDB, we have to enhance the code to process individual email address instead of an array.

Use the code in the [here](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/lambda-functions/send_email_v3.py)

### Step 2: Create the Step Function with the `Map` state

Step Function code reference - [step4.json](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/step-functions/step4.json)