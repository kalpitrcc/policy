import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_hpe(file_path, bucket_name, object_name, access_key, secret_key, endpoint_url):
    """
    Upload a file to HPE object store.

    Parameters:
    - file_path: Local path of the file to upload.
    - bucket_name: Name of the bucket in HPE object store.
    - object_name: Name to give the object in the object store.
    - access_key: Access key for authentication.
    - secret_key: Secret key for authentication.
    - endpoint_url: HPE object store endpoint URL.
    """
    try:
        # Create an S3 client
        s3 = boto3.client('s3', endpoint_url=endpoint_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

        # Upload the file
        s3.upload_file(file_path, bucket_name, object_name)

        print(f"File uploaded successfully to {bucket_name}/{object_name}")

    except NoCredentialsError:
        print("Credentials not available or not valid.")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Example usage
file_path = "path/to/your/file.txt"
bucket_name = "your-bucket-name"
object_name = "uploaded-file.txt"
access_key = "your-access-key"
secret_key = "your-secret-key"
endpoint_url = "https://your-hpe-object-store-endpoint"

upload_to_hpe(file_path, bucket_name, object_name, access_key, secret_key, endpoint_url)
