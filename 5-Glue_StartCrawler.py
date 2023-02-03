import boto3
import json

client = boto3.client('glue', region_name="eu-west-1")

# List all crawlers 
print("The list of available Crawlers:")
response = client.list_crawlers()
print(json.dumps(response, indent=4, sort_keys=True, default=str))

# Start the crawler
response2 = client.start_crawler(
    Name="demo-glue-1" #response['CrawlerNames'][0]
)
print("\nStarting the Crawler:")
print(json.dumps(response2, indent=4, sort_keys=True, default=str))

# Check crawler status
print("\nCrawler Status:")
print("\tstatus: RUNNING")
exit_v = 0
while not(exit_v):
    response = client.get_crawler(Name = 'demo-glue-1')
    if (response['Crawler']['State'] == 'STOPPING') or (response['Crawler']['State'] == 'READY'):
        exit_v = 1
        
print("\tstatus:",response['Crawler']['State'])


# See the generated Table
response = client.get_tables(DatabaseName="input")
print("\nTable:")
print(response['TableList'][0])