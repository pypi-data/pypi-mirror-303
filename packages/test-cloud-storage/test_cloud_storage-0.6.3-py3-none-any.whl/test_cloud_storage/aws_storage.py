import os
import boto3
from botocore.exceptions import ClientError

class AWSStorage:
    """
    A class to interact with AWS S3 storage.

    This class provides methods to initialize an AWS S3 client and fetch details of documents
    stored in an S3 bucket. It uses the Boto3 library to interface with AWS services.

    Attributes:
        s3_client (boto3.client): The S3 client instance for performing S3 operations.
    """
    def __init__(self):
        """
        Initialize AWS S3 client for interacting with S3 storage.
        
        This method creates an S3 client instance using Boto3, which allows for various
        operations on S3 buckets and objects.
        """
        self.s3_client = boto3.client('s3')

    def get_document_details(self, bucket_name, prefix='', file_type=None):
        """
        Fetches details of documents from an AWS S3 bucket with a specific prefix and file type.

        This method retrieves the names, hashes, and sizes of documents in the specified
        S3 bucket, filtering by optional prefix and file type.

        Parameters:
            bucket_name (str): The name of the S3 bucket from which to retrieve documents.
            prefix (str, optional): The folder prefix within the S3 bucket to filter results. 
                                    Defaults to '' (all objects in the bucket).
            file_type (str, optional): The file extension (e.g., '.csv') to filter files. 
                                        Defaults to None (no filtering by file type).

        Returns:
            dict: A dictionary with document details including:
                  - document_name (str): The name of the document without extension.
                  - document_hash (str): The MD5 hash of the document (ETag).
                  - document_size (int): The size of the document in bytes.
                  - file_type (str or None): The file type used for filtering (if provided).

        Raises:
            Exception: If the S3 request fails or if the bucket does not exist.

        Examples:
            aws_service = AWSStorage()
            documents = aws_service.get_document_details('my-bucket', prefix='data/', file_type='.csv')
            print(documents)

        Notes:
            - The method excludes files containing 'fhir_data' in their name.
            - To use this class, ensure you have the Boto3 library installed and configured.
        """
        if not bucket_name:
            raise ValueError("Bucket name must not be empty.")

        print(f"Fetching document details from AWS S3: bucket={bucket_name}, prefix={prefix}, file_type={file_type}")
        
        # Initialize paginator for listing large sets of objects
        paginator = self.s3_client.get_paginator('list_objects_v2')
        document_details = {}

        try:
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

        except ClientError as e:
            # Handle specific errors related to S3
            print(f"An error occurred: {e}")
            raise Exception(f"Failed to fetch documents from bucket '{bucket_name}': {e}")

        except Exception as e:
            # Handle any other exceptions
            print(f"An unexpected error occurred: {e}")
            raise Exception(f"An unexpected error occurred: {e}")

        return document_details