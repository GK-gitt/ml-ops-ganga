import boto3

s3 = boto3.client('s3')

# Input values
bucket_name = 'mlops-s3-bucket-ganga-aws'
s3_file = 'my_first_upload.txt'
local_dest = 'downloaded_machi.txt'

try:
    print("Machi, S3-la irundhu file-a download panren...")
    s3.download_file(bucket_name, s3_file, local_dest)
    print("🚀 SUCCESS: File download aayiduchi!")
except Exception as e:
    print(f"Error: {e}")