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
    
    def count_documents_in_s3_bucket(self, bucket_name, prefix='', file_extension=None):
        """
        Counts total and unique documents of a specific type in an S3 bucket or within a specific prefix (folder).

        This method also returns a list of document names that match the specified criteria.

        Args:
            s3_bucket_name (str): Name of the S3 bucket.
            s3_prefix (str, optional): Prefix to list objects within a specific folder. 
                                        Defaults to '' (all objects).
            file_extension (str, optional): File extension to filter by (e.g., 'xml' for XML files).

        Returns:
            tuple: A tuple containing:
                - total_count (int): The total number of documents found.
                - unique_count (int): The count of unique documents based on ETags.
                - document_names (list): A list of document names that match the criteria.

        Raises:
            Exception: If there is an error accessing S3 or if the bucket does not exist.

        Examples:
            total, unique, documents = aws_service.count_documents_in_s3_bucket('my-bucket', prefix='data/', file_extension='csv')
            print(total, unique, documents)
        """
        etags = set()
        total_count = 0
        document_names = []

        try:
            # Initialize paginator for handling more than 1000 objects
            paginator = self.s3_client.get_paginator('list_objects_v2')

            # Ensure the file extension starts with a dot
            if file_extension and not file_extension.startswith('.'):
                file_extension = '.' + file_extension

            # Create a PageIterator from the paginator
            page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

            # Loop through each page of results
            for page in page_iterator:
                if 'Contents' in page:
                    for obj in page['Contents']:
                        # Filter objects by file extension and exclude unwanted files
                        if (file_extension is None or obj['Key'].endswith(file_extension)) and 'fhir_data' not in obj['Key']:
                            total_count += 1
                            etags.add(obj['ETag'])
                            document_names.append(obj['Key'])  # Collect document names

        except ClientError as e:
            raise Exception(f"Error accessing S3: {str(e)}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

        # Unique count is the size of the set of ETags
        unique_count = len(etags)
        return total_count, unique_count, document_names
    
    def s3_key_exists(self, bucket_name, object_key, processing_info=None, key_to_set=None):
        """
        Check if an object exists in an S3 bucket.

        This method checks for the existence of an object in the specified S3 bucket by
        attempting to retrieve its metadata. If the object exists, it can optionally store
        the object's ETag in a provided dictionary.

        Args:
            bucket_name (str): The name of the S3 bucket to check.
            object_key (str): The key (name) of the object to check for existence.
            processing_info (dict, optional): A dictionary to store additional processing
                                            information. If provided, the ETag of the
                                            object will be stored under `key_to_set`.
                                            Defaults to None.
            key_to_set (str, optional): The key under which to store the ETag in
                                        `processing_info`. Defaults to None.

        Returns:
            bool: True if the object exists, False otherwise.

        Raises:
            Exception: If an error occurs during the request to S3.

        Examples:
            exists = s3_key_exists('my-bucket', 'path/to/my/object.txt')
            print(exists)  # True or False

            processing_info = {}
            exists = s3_key_exists('my-bucket', 'path/to/my/object.txt', processing_info, 'etag_key')
            if exists:
                print(processing_info['etag_key'])  # Prints the ETag of the object if it exists
        """
        try:
            response = self.s3_client.head_object(Bucket=bucket_name, Key=object_key)
            etag = response['ETag']
            if processing_info and key_to_set:
                processing_info[key_to_set] = etag.strip('"')
            return True
        except self.s3_client.exceptions.NoSuchKey:
            print(f"Object with key '{object_key}' does not exist in bucket '{bucket_name}'.")
            return False
        except Exception as e:
            print(f"Error checking for object '{object_key}' in bucket '{bucket_name}': {e}")
            return False
