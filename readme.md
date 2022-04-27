# Datafluids EMR setup

This is SAM serverless project. It can deploy the infrastructure using below command.
```bash
sam deploy -t .\template.yml --s3-bucket sam-bucket-hello-project --s3-prefix sam --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --region us-east-1 --profile krishna --parameter-overrides Environment=dev --stack-name datafluids
```