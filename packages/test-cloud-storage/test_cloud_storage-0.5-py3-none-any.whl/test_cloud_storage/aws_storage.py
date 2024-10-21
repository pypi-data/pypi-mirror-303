import os
import boto3

class AWSStorage:
    def __init__(self):
        """
        Initialize AWS S3 client for interacting with S3 storage.
        """
        self.s3_client = boto3.client('s3')
        print("Initialized AWS Storage Service")

    def get_document_details(self, bucket_name, prefix='', file_type=None):
        """
        Fetches details of documents from an AWS S3 bucket with a specific prefix and file type.
        
        Parameters:
            bucket_name (str): The name of the S3 bucket.
            prefix (str, optional): The folder prefix within the S3 bucket. Defaults to ''.
            file_type (str, optional): The file extension (e.g., '.csv') to filter files. Defaults to None.
        
        Returns:
            dict: A dictionary with document details including document name, hash, and size.
        """
        print(f"Fetching document details from AWS S3: bucket={bucket_name}, prefix={prefix}, file_type={file_type}")
        
        # Initialize paginator for listing large sets of objects
        paginator = self.s3_client.get_paginator('list_objects_v2')
        document_details = {}

        # Paginate through all objects in the bucket with the specified prefix
        for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
            if 'Contents' in page:
                for obj in page['Contents']:
                    full_document_name = obj['Key']
                    
                    # Filter by file type and exclude unwanted files
                    if (file_type is None or full_document_name.endswith(file_type)) and 'fhir_data' not in full_document_name:
                        base_document_name = os.path.splitext(os.path.basename(full_document_name))[0]
                        document_size = obj['Size']
                        document_hash = obj['ETag'].strip('"')  # MD5 hash from S3 metadata

                        # Store document details
                        document_details[base_document_name] = {
                            'document_name': base_document_name,
                            'document_hash': document_hash,
                            'document_size': document_size,  
                            'file_type': file_type
                        }

        return document_details