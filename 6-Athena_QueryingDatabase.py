import boto3
import json

athena_client = boto3.client('athena')

# List all crawlers 
bucket = "antoinefrd-github-demo-glue-1/athena-results/"
database_name = "input"
table_name = "csv_customers"

response = athena_client.start_query_execution(
    QueryString = f"SELECT count(*) FROM {database_name}.{table_name};",
    QueryExecutionContext = {
        'Database': f"{database_name}"
    }, 
    ResultConfiguration = { 'OutputLocation': f's3://{bucket}'}
)

print("Query result saved in s3://%s" % bucket) 
print(json.dumps(response, indent=4, sort_keys=True, default=str))

