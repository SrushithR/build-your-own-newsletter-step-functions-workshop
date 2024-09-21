# Schedule Step Function via AWS EventBridge

## 1. Create an EventBridge Rule to Trigger the Step Function
1. Navigate to the **Amazon EventBridge** service in the AWS Management Console.
2. In the left-hand menu, click **Rules**, then click **Create rule**.
3. Set the **Name** for the rule (e.g., `ScheduleSendEmails`).
4. Under **Define pattern**, select **Event Source** as **EventBridge Schedule**.
5. Define your schedule pattern:
    - For a fixed interval (e.g., every day at 12:00 PM), choose **Cron expression** and use an expression like `cron(0 12 * * ? *)`.
    - Or, set a **Rate** expression for a more generic interval (e.g., every hour, day, etc.).
6. In the **Select targets** section, choose **Step Functions state machine** as the target.
7. Select the Step Function created in Step 3/4/5 (`DDBDirectAndSendEmailStateMachine`).
8. Click **Create** to finalize the rule.

Once the rule is created, EventBridge will trigger the Step Function according to the schedule you specified, initiating the process to fetch subscribers from DynamoDB and send emails.

> **Note:** You can modify the schedule by updating the EventBridge rule at any time.