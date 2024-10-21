from .aws_storage import AWSStorage
from .azure_storage import AzureStorage
from .gcp_storage import GCPStorage

def get_cloud_storage_service(provider, connection_string=None):
    """
    Initialize the appropriate cloud storage service based on the provider.
    """
    if provider == 'aws':
        return AWSStorage()
    elif provider == 'azure':
        if not connection_string:
            raise ValueError("Azure requires a connection string")
        return AzureStorage(connection_string)
    elif provider == 'gcp':
        return GCPStorage()
    else:
        raise ValueError(f"Unsupported cloud provider: {provider}")
