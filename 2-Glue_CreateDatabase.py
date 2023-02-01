import boto3
import json 

# Initialize the Boto3 Client for AWS Glue
client = boto3.client('glue', region_name="eu-west-1")

# Create the Glue Database
try:
   response = client.create_database(
        DatabaseInput={
            'Name': 'input',
        },
    )  
   print("Database created!")
   print(json.dumps(response, indent=4, sort_keys=True, default=str))

except client.exceptions.AlreadyExistsException as e:
   if e.response['Error']['Code'] == 'AlreadyExistsException':
       print("Database already created")
   else:
       print("Unexpected error: %s\n%s" % (e, e.response))

