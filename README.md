# Software Delivery Pipeline - Denny Hoang

This project uses GitHub, AWS CodePipeline, and AWS CodeBuild to automate a software delivery workflow. A manual approval stage pauses the pipeline after source retrieval and sends an email notification through Amazon SNS.

## Pipeline Workflow

1. **Source:** Retrieves the latest code from GitHub.
2. **ManualReview:** Notifies the reviewer and waits for approval.
3. **Build:** After approval, runs the configured testing and packaging process.

CodeBuild is configured to test a sample Python application and package its output as an artifact.

## Repository Files

| File | Description |
|---|---|
| `pipeline-template.json` | CloudFormation template for the pipeline and supporting resources. |
| `buildspec.yml` | Commands for testing and packaging the application. |
| `app.py` | Sample Python application. |
| `test_app.py` | Application unit test. |
| `REPORT_OUTLINE.md` | Original outline used to prepare the separately submitted report. |
| `README.md` | Project overview and verification results. |

## AWS Infrastructure

The CloudFormation template defines:

- CodePipeline with Source, ManualReview, and Build stages.
- CodeBuild project.
- S3 artifact bucket.
- SNS topic and email subscription.
- CloudWatch log group.
- IAM service roles.

The GitHub connection is created separately using AWS CodeConnections.

## Deployment

- **Region:** `us-east-1` — N. Virginia
- **Stack name:** `software-delivery-homework`
- **Repository:** `dennyhoang8/software-delivery-pipeline`
- **Branch:** `main`

### Deployment Steps

1. Create and authorize a GitHub connection in AWS CodeConnections.
2. Upload `pipeline-template.json` to CloudFormation.
3. Enter the following parameters:

   | Parameter | Value |
   |---|---|
   | `RepositoryId` | `dennyhoang8/software-delivery-pipeline` |
   | `BranchName` | `main` |
   | `ConnectionArn` | ARN of an available GitHub connection in the same region. |
   | `ReviewerEmail` | Email address for approval notifications. |

4. Acknowledge IAM resource creation and create the stack.
5. Confirm the SNS email subscription.
6. Commit a change to `main`.
7. Review and approve the pending action in CodePipeline.

## Verification Results

| Check | Result |
|---|---|
| CloudFormation deployment | Succeeded with `CREATE_COMPLETE`. |
| GitHub trigger | A commit automatically started an execution through a webhook. |
| Manual approval pause | The pipeline paused at ManualReview before Build. |
| Email notification | The SNS approval notification was received. |
| Approval processing | ManualReview succeeded and the pipeline attempted to start CodeBuild. |
| AWS build | Blocked before code execution by an account quota of `0`. |
| Local unit test | Passed. |

### Verified Commit

- **Commit:** `50b7f7ae`
- **Message:** `Add comment for pipeline trigger verification`
- **Execution ID:** `d2f6f38f-feff-4758-ae7a-be665d09a4f0`

### AWS Build Limitation

CodeBuild returned:

> Error calling startBuild: Cannot have more than 0 builds in queue for the account  
> Error Code: AccountLimitExceededException

The applied quota for concurrently running Linux/Small builds was `0`. An increase to `1` was requested, and AWS opened a support case.

The build commands did not execute in AWS. A successful AWS build and generated artifact were therefore not verified.

### Local Test

Run the application test from the repository root:

    python3 -m unittest discover -v

Observed output:

    test_greeting_uses_name (test_app.GreetingTests.test_greeting_uses_name) ... ok

    Ran 1 test

    OK

The local result verifies the sample application test. It does not replace verification of the AWS build process.

## Resource Cleanup

After collecting verification evidence:

- Emptied the S3 artifact bucket.
- Deleted the CloudFormation stack.
- Deleted the separately created GitHub connection.
- Retained the GitHub repository for submission.

## Verification Report

The completed report is submitted separately on Canvas. It contains screenshots and outputs documenting deployment, the manual approval workflow, the AWS quota error, and cleanup.

## AWS References

- [Manual approval actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html)
- [GitHub connection source actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html)
- [Approve or reject an action](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-approve-or-reject.html)
