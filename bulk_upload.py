import boto3
import os

# 1. AWS Connection
s3 = boto3.client('s3')

# 2. Settings (Change these to your names)
bucket_name = 'mlops-s3-bucket-ganga-aws' # Unga bucket name kudunga
folder_path = './'     # Unga laptop-la irukkura folder path

# 3. Create the folder if it doesn't exist (Testing-kku)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    # 3 dummy files create panrom automate panna
    for i in range(1, 4):
        with open(f"{folder_path}/file_{i}.txt", "w") as f:
            f.write(f"This is file number {i}")

# 4. THE MAGIC: Looping through the folder
print(f"Scanning folder: {folder_path}...")

for filename in os.listdir(folder_path):
    # Oru oru file-oda full path-a edukkurom
    local_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (not a sub-folder)
    if os.path.isfile(local_path):
        print(f"Uploading {filename} to S3...")
        
        # S3-ku thallurom
        s3.upload_file(local_path, bucket_name, filename)
        print(f"Done: {filename} is now in the cloud!")

print("\n🚀 All files uploaded successfully, Machi!")