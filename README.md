# Software Delivery Pipeline - Denny Hoang

GitHub source -> ManualReview (email notification) -> CodeBuild (test and package).
The approval happens immediately after the source stage. CodeBuild cannot run until approval.
This homework builds a small Python application and saves its output as an artifact; it does not deploy a website.

## 1. GitHub
Create a new repository named `software-delivery-pipeline`. Extract this ZIP and upload all its files to the repository root on the `main` branch. Do not upload just the ZIP.

## 2. GitHub connection
In the AWS Developer Tools console, open Settings > Connections (or search for CodeConnections). Stay in N. Virginia / us-east-1. Create a GitHub connection named `homework-github`. Complete the GitHub authorization, granting access to this repository. Wait until the connection is AVAILABLE, then copy its ARN. The CloudFormation template uses this existing connection; it does not create it.

## 3. CloudFormation
Create stack > With new resources (standard) > Choose an existing template > Upload a template file. Upload `pipeline-template.json`.
Stack name: `software-delivery-homework`.
Parameters: RepositoryId = your GitHub username/software-delivery-pipeline; BranchName = main; ConnectionArn = copied connection ARN; ReviewerEmail = your own email.
Leave other settings at defaults, acknowledge IAM resource creation, and submit. Record CREATE_COMPLETE. If account verification blocks creation, save that error and resolve it with AWS Support.

## 4. Confirm email and run
Confirm the Amazon SNS subscription email. The first execution may have reached approval before you confirmed, so it may not produce an email you receive. After confirming, make a small edit to app.py (for example change Hello to Welcome) and update the expected text in test_app.py in the SAME commit. A new execution should start automatically.

## 5. Verify
Take screenshots with the execution ID visible where possible:
1. Successful CloudFormation creation.
2. GitHub commit that triggered this execution.
3. Source succeeded, ManualReview waiting, and Build not started for this execution.
4. Approval notification email after confirming the SNS subscription. Hide approval tokens or private links before sharing publicly.
5. Open the approval in CodePipeline, review the GitHub commit, enter a comment, and approve.
6. ManualReview succeeded and Build succeeded for the same execution.
7. CodeBuild log showing the unit test passed and packaging commands succeeded.
8. Optional stronger check: make another matching app/test edit, reject that execution, and show Build did not run for it.

If no execution starts, check connection AVAILABLE, repository access, owner/repo spelling, and branch. If a build fails, inspect the CodeBuild logs. Do not claim success until these live checks pass.

## 6. Report and submission
Use REPORT_OUTLINE.md to write the report with actual screenshots/outputs. Submit the new GitHub repository URL and report on Canvas. The outline is not a completed verification report.

## 7. Cleanup
After capturing all evidence, stop any active pipeline execution/build. Note ArtifactBucketName in stack Outputs. In S3, EMPTY that exact bucket, including versions/delete markers if any. Delete the CloudFormation stack, wait for DELETE_COMPLETE, and verify its resources are removed. If deletion fails because the artifact bucket is nonempty, empty it and retry deletion. Delete the separately created homework-github connection if it is used only for this homework. Keep the GitHub repository and report for submission.

## AWS references
- https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html
- https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-approve-or-reject.html
