import boto3
import os

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Retrieve the source and destination bucket names from environment variables
    source_bucket = os.environ['SOURCE_BUCKET']
    destination_bucket = os.environ['DESTINATION_BUCKET']
    
    # Loop through each record in the event
    for record in event['Records']:
        # Get the key (filename) of the object that triggered the event
        key = record['s3']['object']['key']
        
        # Copy the object from the source bucket to the destination bucket
        copy_source = {
            'Bucket': source_bucket,
            'Key': key
        }
        
        # Construct the destination key (filename) in the destination bucket
        destination_key = f"copied_{key}"
        
        try:
            # Perform the copy operation
            s3.copy_object(
                Bucket=destination_bucket,
                Key=destination_key,
                CopySource=copy_source
            )
            
            print(f"Object '{key}' copied successfully from '{source_bucket}' to '{destination_bucket}' as '{destination_key}'")
        
        except Exception as e:
            print(f"Error copying object '{key}' from '{source_bucket}' to '{destination_bucket}': {e}")
