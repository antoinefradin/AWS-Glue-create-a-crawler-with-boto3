import boto3
import json 

# Initialize the Boto3 Client for AWS Glue
client = boto3.client('glue', region_name="eu-west-1")


# Create the Glue Cralwer
try:
   response = client.create_crawler(
        Name='demo-glue-1',
        Role='AWSGlueServiceRole-glue-1-crawlerdelete-EZCRC-s3Policy',
        DatabaseName='input',
        Targets={
            'S3Targets': [
                {
                    'Path': 's3://antoinefrd-github-demo-glue-1/input/customers',
                },
            ]
        },
        SchemaChangePolicy={
            'UpdateBehavior': 'UPDATE_IN_DATABASE',
            'DeleteBehavior': 'DEPRECATE_IN_DATABASE'
        },
        RecrawlPolicy={
            'RecrawlBehavior': 'CRAWL_EVERYTHING'
        },
        LineageConfiguration={
            'CrawlerLineageSettings': 'DISABLE'
        }
) 
   print("Crawler created!")
   print(json.dumps(response, indent=4, sort_keys=True, default=str))

except client.exceptions.AlreadyExistsException as e:
   if e.response['Error']['Code'] == 'AlreadyExistsException':
       print("Crawler already created")
   else:
       print("Unexpected error: %s\n%s" % (e, e.response))

