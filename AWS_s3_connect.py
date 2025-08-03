import boto3
import pandas as pd

''' Safely configured the s3 credntials in Terminal'''

s3 = boto3.client('s3') # establishes the connection as boto3 looks for credential, authenticates it and sends API call to AWS as a HTTP request
all_buckets = s3.list_buckets()

# printing bucket names
for bucket in all_buckets['Buckets']: # 'Buckets' is a key here that contains values of each bucket 
    print(bucket['Name']) # Each bucket again has a key called 'Name' that returns the value containing name of our bucket

# Creating a sample csv file and upload it 
squared_10 = pd.DataFrame({'x':[1, 2, 3, 4, 5, 6, 7, 8, 9], 'y' : [1, 4, 9, 16, 25, 36, 49, 64, 81]})
squared_10.to_csv('squared_10.csv')

# Uploading it to my data bucketn using the upload file method :  def upload_file(file_name, bucket, object_name=None):
s3.upload_file('squared_10.csv','sohail-aws-s3data-bucket', 'sampleCSV_Folder/squared_10.csv') # sampleCSV is a folder in sohail-aws-s3data-bucket where squared_10 file is uploaded 

# seeing the filenames(objects in my 'sohail-aws-s3data-bucket' where I upload the squared_10.csv file) to confirm my upload
bucket_name = 'sohail-aws-s3data-bucket'
response = s3.list_objects_v2(Bucket = bucket_name)

for file_objs in response['Contents']:
    print(file_objs['Key']) # output : netflix_cleaned.csv , sampleCSV_Folder/squared_10.csv. Confirmed! 





