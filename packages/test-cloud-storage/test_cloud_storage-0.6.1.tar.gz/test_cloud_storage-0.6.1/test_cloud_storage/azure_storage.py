class AzureStorage:
    def __init__(self, connection_string):
        print(f"Initialized Azure Storage Service with connection string: {connection_string}")

    def get_document_details(self, container_name, prefix='', file_type=None):
        print(f"Fetching document details from Azure Blob: container={container_name}, prefix={prefix}, file_type={file_type}")
