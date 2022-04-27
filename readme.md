# Datafluids EMR setup

## Prerequisites

To deploy this application, we should have SAM CLI install in local machine. It can also be deployed using CI/CD. However, CI/CD is not yet implemented.

This is SAM serverless project. It can deploy the infrastructure using the below command.
```powershell
$env:AWS_PROFILE="profile"
sam deploy -t .\template.yml --s3-bucket sam-bucket-hello-project --s3-prefix sam --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --region us-east-1 --parameter-overrides Environment=dev InstanceType=m4.xlarge --stack-name datafluids --no-fail-on-empty-changeset
```
### Params Description

* -t : Relative location to template file.
* --s3-bucket : The bucket which will be used for deploying the lambda artifacts. Usually created by SAM CLI but we can use any bucket
* --s3-prefix : prefix of artifacts objects in s3
* --capabilities : It's the capabilities of template. No need to update it.
* --region : AWS Region where we need to provision the infrastructure
* --parameter-overrides : Input parameters that we need to override in deployment. In our case, we have two input variables that we need to set while deployment
* --stack-name : The cloudformation stack name. It can be anything.
* --no-fail-on-empty-changeset: This key is to not to fail the command when there is no change in template while deployment.

## Things to improve and resolve

1. Is there any VPC configuration for EMR?<br />
  This is required if the EMR cluster is using database and database is in private subnet. It's recommended to process sensitive data in private network with end to end encryption.
2. How you want to terminate the EMR cluster?<br />
  To terminate the EMR cluster, there is no straight forward way. We can send the message to cloudwatch about activity and then set the alarms to trigger lambda which will terminate the cluster. For reference, https://aws.amazon.com/blogs/big-data/optimize-amazon-emr-costs-with-idle-checks-and-automatic-resource-termination-using-advanced-amazon-cloudwatch-metrics-and-aws-lambda/
3. whats the current configuration for cluster?<br />
  I am creating new cluster using cloudformation template. I am referring the document provided. However, if the configuration for the current clusters are different, we can update that as well in template.