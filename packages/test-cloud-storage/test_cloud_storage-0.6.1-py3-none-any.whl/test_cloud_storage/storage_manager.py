from .aws_storage import AWSStorage
from .azure_storage import AzureStorage
from .gcp_storage import GCPStorage

def get_cloud_storage_service(provider, connection_string=None):
    """
    Initializes and returns a cloud storage service instance based on the provider.

    Parameters:
        provider (str): The cloud provider to use ('aws', 'azure', 'gcp').
        connection_string (str, optional): Required for Azure. The connection string 
                                           for accessing Azure Blob Storage. Defaults to None.

    Returns:
        CloudStorage: An instance of the appropriate cloud storage service (AWS, Azure, or GCP).
        
    Raises:
        ValueError: If the provider is unsupported or if the connection string is not provided 
                    for Azure.

    Examples:
        aws_service = get_cloud_storage_service('aws')
        azure_service = get_cloud_storage_service('azure', connection_string='your_connection_string')
        gcp_service = get_cloud_storage_service('gcp')
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
