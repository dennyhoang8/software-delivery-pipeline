# Software Delivery Pipeline Verification Report

Denny Hoang  
November 9, 2026

**Status:** GitHub trigger and manual approval workflow verified in AWS. CodeBuild was blocked before code execution by an account quota of `0`.

## Implementation

The pipeline retrieves code from GitHub and pauses at a separate ManualReview stage. Amazon SNS emails the subscribed reviewer. Approval allows the pipeline to proceed to CodeBuild, which is configured to run a Python unit test and package the application output.

The CloudFormation template defines the pipeline, CodeBuild project, S3 artifact bucket, SNS topic and subscription, CloudWatch log group, and IAM service roles. The GitHub connection was created separately.

- **Repository URL:** https://github.com/dennyhoang8/software-delivery-pipeline
- **AWS region:** `us-east-1`
- **Stack name:** `software-delivery-homework`
- **Execution ID:** `d2f6f38f-feff-4758-ae7a-be665d09a4f0`

## Verification Through the Browser

### 1. CloudFormation Deployment

CloudFormation displayed `CREATE_COMPLETE` for the stack, confirming successful creation of the defined resources.

### 2. GitHub Trigger

A commit to `main` automatically started a new pipeline execution.

- **Commit:** `50b7f7ae`
- **Commit message:** `Add comment for pipeline trigger verification`
- **Trigger:** `Webhook`
- **Started:** November 9, 2026, at 1:48 PM CST

### 3. Manual Approval Pause

The Source stage succeeded, and the pipeline paused at the `ApproveChanges` action in the ManualReview stage. Build had not started while approval was pending.

### 4. Email Notification

An approval notification arrived from `no-reply@sns.amazonaws.com`.

The notification included:

- **Stage:** `ManualReview`
- **Action:** `ApproveChanges`
- **Region:** `us-east-1`
- **Additional information:** Review the latest GitHub commit. Approve to allow CodeBuild to run.

Receiving the notification confirmed that the SNS subscription was active.

### 5. Approval and Continuation

After approval was submitted, ManualReview changed to `Succeeded`, and the pipeline attempted to start the Build stage for the same execution.

### 6. CodeBuild Account Quota Error

The Build action failed before the application code or build commands executed.

AWS returned:

> Error calling startBuild: Cannot have more than 0 builds in queue for the account  
> Service: AWSCodeBuild  
> Status Code: 400  
> Error Code: AccountLimitExceededException

**Action execution ID:** `ad887a04-a7af-4387-8393-67a55b3c4ea4`

The account's applied quota for concurrently running Linux/Small builds was `0`. An increase to `1` was requested, and AWS opened support case `179425429300138`.

A successful AWS build, test execution, and generated build artifact were not verified.

## Local Application Test

The supplied application test was run locally using:

    python3 -m unittest discover -v

Observed output:

    test_greeting_uses_name (test_app.GreetingTests.test_greeting_uses_name) ... ok

    Ran 1 test

    OK

This result confirms that the sample application unit test passes locally. It does not verify the complete AWS build process.

## Resource Cleanup

After collecting the verification evidence:

1. Emptied the homework S3 artifact bucket.
2. Deleted the `software-delivery-homework` CloudFormation stack.
3. Deleted the separately created `homework-github` connection.
4. Retained the GitHub repository for submission.

The AWS Connections page displayed `Connection deleted successfully` and an empty connections list.

## Supporting Evidence

The separately submitted report includes screenshots documenting:

- Successful CloudFormation deployment.
- The pipeline paused before approval.
- Source and ManualReview succeeding, followed by Build failing.
- Successful deletion of the GitHub connection.

The report also includes the approval notification details, webhook execution details, and the CodeBuild error output.

## Conclusion

Verification demonstrated that a GitHub commit automatically triggered the pipeline, the pipeline paused for review, an email notification arrived, and approval allowed the execution to proceed to the Build stage.

CodeBuild was blocked by the account quota before code execution. The local application unit test passed, but a successful AWS build and artifact generation remain unverified.
