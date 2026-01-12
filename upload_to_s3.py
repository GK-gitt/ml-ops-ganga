import boto3

s3 = boto3.client('s3')

# Define your details
local_file = 'ganga_note.txt'
target_bucket = 'mlops-s3-bucket-ganga-aws' # Adhae name-a kudunga
s3_file_name = 'my_first_upload.txt' # Cloud-la idhu dhaan file name

try:
    print(f"Uploading {local_file} to {target_bucket}...")
    
    # The 'upload_file' action
    # Arguments: (Local path, Bucket name, Name in Cloud)
    s3.upload_file(local_file, target_bucket, s3_file_name)
    
    print("🚀 SUCCESS: File uploaded to Amazon Cloud!")

except Exception as e:
    print(f"Error: {e}")