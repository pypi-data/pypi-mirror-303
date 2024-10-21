class GCPStorage:
    def __init__(self):
        print("Initialized GCP Storage Service")

    def get_document_details(self, bucket_name, prefix='', file_type=None):
        print(f"Fetching document details from GCP Storage: bucket={bucket_name}, prefix={prefix}, file_type={file_type}")
