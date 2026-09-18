# Project 4: The Serverless Logic

## Scenario

A company wants to build a simple "Cost Calculator" API. Running a server 24/7 just for this small calculation is wastefully expensive. They want a solution that only runs code when triggered.

## Mission

* Deploy code without managing infrastructure
* Create a Serverless Function (AWS Lambda)
* Write a script (Python) that takes two numbers as input and returns the sum
* Test the function with different test events to ensure accuracy

## Tools Used

* AWS Lambda (Python 3.13 runtime)
* Auto-generated IAM Execution Role (basic Lambda permissions)
* Amazon CloudWatch Logs

## Steps Taken

1. **Created the Lambda function** — "Author from scratch," Python 3.13 runtime, default execution role (auto-created with only CloudWatch Logs permission — Principle of Least Privilege).
2. **Wrote the handler code** — see [`lambda\_function.py`](./lambda_function.py).
3. **Deployed the code** via the console's Deploy button.
4. **Created and ran test events**:

   * `{"num1": 15, "num2": 25}` → `{"Sum": 40}`
   * `{"num1": 100, "num2": 250}` → `{"Sum": 350}`
(see [`test-events/`](./test-events))
5. **Verified billing/execution evidence** in CloudWatch Logs — confirmed millisecond-level `Duration` and `Billed Duration`.
6. **Reviewed the IAM Execution Role** under Configuration > Permissions — confirmed it only has the minimal CloudWatch logging permission, nothing more.

## Files in this folder

* `lambda\_function.py` — the deployed handler code
* `test-events/` — the sample JSON payloads used to test the function
* `screenshots/` — evidence of each step

## Screenshots

|#|File|Description|
|-|-|-|
|1|`screenshots/01-function-created.png`|Lambda function overview (name, Python runtime, ARN)|
|2|`screenshots/02-code-deployed.png`|Code editor + "Changes deployed" confirmation|
|3|`screenshots/03-test-event.png`|Test event JSON configuration|
|4|`screenshots/04-test-success.png`|Successful execution result ({"Sum": 40})|
|5|`screenshots/05-second-test.png`|Second test with different numbers ({"Sum": 350})|
|6|`screenshots/06-cloudwatch-log.png`|CloudWatch log showing Duration/Billed Duration|
|7|`screenshots/07-iam-role.png`|Auto-generated IAM Execution Role|



