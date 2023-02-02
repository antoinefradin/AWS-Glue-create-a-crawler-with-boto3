import boto3
import json

def create_iam_policy(s3_bucket_name):
    # Create IAM client
    iam = boto3.client("iam")

    # Create a policy
    glue_s3_crawler_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:PutObject"
                ],
                "Resource": [
                    f"arn:aws:s3:::{s3_bucket_name}/*"
                ]
            }
        ]
    }
    response = iam.create_policy(
        PolicyName='AWSGlueServiceRole-glue-1-crawlerdelete-s3Policy',
        PolicyDocument=json.dumps(glue_s3_crawler_policy)
    )

    return response["Policy"]["Arn"]


def create_iam_role():
    iam = boto3.client("iam")
    assume_role_policy_document = json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Principal": {
                "Service": "glue.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
            }
        ]
    })
    response = iam.create_role(
        RoleName = "AWSGlueServiceRole-glue-1-crawlerdelete",
        AssumeRolePolicyDocument = assume_role_policy_document
    )

    return response["Role"]["RoleName"]


def attach_iam_policy(policy_arn, role_name):
    iam = boto3.client("iam")
    response = iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )
    #print(json.dumps(response, indent=4, sort_keys=True, default=str))




# How to run:

s3_bucket_name = "antoinefrd-github-demo-glue-1" #antoinefrd-github-demo-glue-1/input/customers/*

# 1. Create Custom IAM Policy
print("Creating Custom IAM policy")
policy_arn = create_iam_policy(s3_bucket_name=s3_bucket_name)

# 2. Create IAM Role
print("\nCreating IAM role")
role_name = create_iam_role()

# 3. Attach Custom IAM policy
print("\nAttaching custom IAM policy")
attach_iam_policy(policy_arn=policy_arn, role_name=role_name)

# 4. Attach Default Glue Managed policy
print("\nAttaching default IAM policy: AWSGlueServiceRole")
service_policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
attach_iam_policy(policy_arn=service_policy_arn, role_name=role_name)


iam = boto3.client("iam")
response = iam.list_attached_role_policies(RoleName='AWSGlueServiceRole-glue-1-crawlerdelete',)
print("\nAWSGlueServiceRole attached Policies:")
print(json.dumps(response["AttachedPolicies"], indent=4, sort_keys=True, default=str))