import boto3
from botocore.exceptions import ClientError


# Create an S3 client
s3 = boto3.resource('s3')

# List S3 buckets 
for bucket in s3.buckets.all():
   print(bucket.name)

# Create S3 buckets 
try:
   s3.create_bucket(Bucket='antoinefrd-github-demo-glue-1', CreateBucketConfiguration={
      'LocationConstraint': 'eu-west-1'}
      )
   print("Bucket created!")
except ClientError as e:
   if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
       print("Bucket already created")
   else:
       print("Unexpected error: %s\n%s" % (e, e.response))

# Add folders and .csv file
my_bucket = s3.Bucket('antoinefrd-github-demo-glue-1')

input_folder_name = "input/customers"
output_folder_name = "output"
athena_folder_name = "athena-results"

my_bucket.put_object(Key=(output_folder_name+'/'))
my_bucket.put_object(Key=(athena_folder_name+'/'))

with open("customer.csv", 'rb') as f:
   my_bucket.put_object(Body=f, Key=(input_folder_name+'/'+f.name))

print([obj.key for obj in my_bucket.objects.all()])
