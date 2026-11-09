# Software Delivery Pipeline Verification Report
Denny Hoang

Status: NOT YET VERIFIED IN AWS. Replace this status after completing the live checks.

## Implementation
The pipeline retrieves code from a new GitHub repository and pauses at a separate ManualReview stage. Amazon SNS emails the subscribed reviewer. After approval, CodeBuild runs a Python unit test and creates an output artifact. IAM roles permit the pipeline and build to access their required resources.

Repository URL: [add actual URL]
AWS region: us-east-1
Stack name: software-delivery-homework
Execution ID: [record actual ID]

## Verification through the browser
For each item below, describe what you actually observed and insert its screenshot/output.

1. CloudFormation CREATE_COMPLETE: [evidence]
2. SNS email subscription confirmed: [evidence]
3. New GitHub commit automatically triggered an execution: [commit and execution evidence]
4. Pipeline paused at ManualReview and Build had not started: [evidence]
5. Approval notification arrived: [redacted evidence]
6. Reviewed changes and approved with comment: [evidence]
7. Same execution continued and Build succeeded: [evidence]
8. CodeBuild test result and generated artifact: [actual log output/evidence]
9. Optional rejection test: [actual result, or omit if not performed]

## Resource cleanup
[Actual stack deletion and resource checks. Include evidence. Confirm removal of the separate connection if created exclusively for this assignment.]

## Conclusion
[State only results supported by your actual verification.]
