## Callback Pattern

Now let's add a manual step to get an approval from the admin before the email blast can be sent. We will leverage the callback pattern for the same.

Please follow these steps for this part of the workshop:

## Step 1: Create send_approval_email lambda function

Create a new lambda function to send the approval email to the admin. You can find the code for this [here](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/lambda-functions/send_approval_email.py). This lambda function will send the original email with the subject, along with an approval and rejection link.

## Step 2: Create manage_notification_status lambda function

This lambda function will be the listener and react to what happens when the admin approves or rejects. You can find the lambda function code [here](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/lambda-functions/manage_notification_status.py).

This lambda function accepts the status and the task token passed via the function URL. Now, lets create a function URL

## Step 3: Create Function URL for manage_notification_status

Create a function URL by navigating to the `Configuration` tab, `Function URL` section and clicking on the `Create function URL` button. For the Auth part, please select `None` and `Save` the details. This will create a publicly accessible URL for your lambda function. Keep it safe, we need to use it in the `manage_notification_status` lambda function

## Step 4: Update `manage_notification_status` lambda function

Update the lambda function code and add the function URL created in the previous step

## Step 5: Create `step5` step function

Step Function code reference - [step5.json](https://github.com/SrushithR/build-your-own-newsletter-step-functions-workshop/blob/main/step-functions/step5.json)