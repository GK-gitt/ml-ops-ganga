import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

try:
    # Try to list buckets (It will show an empty list [] if your account is new)
    response = s3.list_buckets()
    print("\n✅ CONNECTION SUCCESSFUL!")
    print(f"Buckets in your account: {response['Buckets']}")
    print("\nMachi, unga Python code ippo Cloud-oda handshake panniduchi!")
except Exception as e:
    print(f"\n❌ Connection failed: {e}")