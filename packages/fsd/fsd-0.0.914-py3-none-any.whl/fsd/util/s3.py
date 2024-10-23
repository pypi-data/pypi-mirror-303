import boto3
import os
import datetime
import zipfile
from fsd.log.logger_config import get_logger
logger = get_logger(__name__)

def upload_file_to_s3(file_path, bucket_name, s3_key):
    # Load configuration from environment variables or a config file
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', 'AKIAZ7YFAWD6HLD47Z4O')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', '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')
    region_name = os.environ.get('AWS_REGION', 'us-east-1')

    # Create an S3 client with the configuration
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=region_name)

    # Upload the file to S3
    s3.upload_file(file_path, bucket_name, s3_key)

def deploy_zip_to_s3(local_directory):
    """
    Create a zip file from a local directory and upload it to S3.
    
    :param local_directory: Path to the local directory to be zipped and uploaded
    :return: S3 key of the uploaded zip file
    """
    bucket_name = 'zinley'
    s3_prefix = 'fsd/'
    ignore_files = ['.git', '.DS_Store', '.zinley', '.zinley.tags.cache.v3', '.gitignore']
    # Create a temporary zip file
    zip_filename = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_web.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        logger.debug(local_directory)
        for root, dirs, files in os.walk(local_directory, topdown=True):
            # Convert local_directory to absolute path if it's not already
            local_directory = os.path.abspath(local_directory)
            
            # Ensure root is an absolute path
            root = os.path.abspath(root)
            
            # Skip if root is not within local_directory
            if not root.startswith(local_directory):
                continue

            # Remove ignored directories
            dirs[:] = [d for d in dirs if d not in ignore_files]
            for file in files:
                if file not in ignore_files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, local_directory)
                    if os.path.isfile(file_path):  # Check if it's a file before adding
                        zipf.write(file_path, arcname)
    
    # Check if the zip file is empty
    if os.path.getsize(zip_filename) == 0:
        raise ValueError(f"Generated zip file {zip_filename} is empty. No files were added.")
    # Generate S3 key for the zip file
    s3_key = f"{s3_prefix}{os.path.basename(local_directory)}_{zip_filename}"
    
    # Upload the zip file to S3
    upload_file_to_s3(zip_filename, bucket_name, s3_key)
    
    # Clean up the temporary zip file
    os.remove(zip_filename)
    
    return s3_key
