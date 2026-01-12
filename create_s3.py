import boto3

s3 = boto3.client('s3')

# Bucket name must be globally unique (Ulagathulaye yarum indha name-a vachurukka koodathu)
bucket_name = "mlops-s3-bucket-ganga-aws" 

try:
    print(f"Creating bucket: {bucket_name}...")
    s3.create_bucket(Bucket=bucket_name)
    print("🚀 SUCCESS: Bucket created!")
    
    # List buckets again to verify
    response = s3.list_buckets()
    print(f"Updated Buckets List: {[b['Name'] for b in response['Buckets']]}")

except Exception as e:
    print(f"Oops! Something went wrong: {e}")