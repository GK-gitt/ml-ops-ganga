# 1. Base Image
FROM python:3.9-slim

# 2. Work Directory
WORKDIR /app

# 3. Copy ONLY what we need
# Namma script-a copy panrom
COPY bulk_upload.py .
# Namma upload panna pora files-a mattum selective-ah copy panrom
COPY ganga_note.txt .
COPY downloaded_machi.txt .

# 4. Install Library
RUN pip install boto3

# 5. Run the script
CMD ["python", "bulk_upload.py"]