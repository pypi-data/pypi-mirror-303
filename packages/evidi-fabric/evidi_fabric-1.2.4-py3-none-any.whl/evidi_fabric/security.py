"""
This module contains functions to work with security.
    
        - get_azure_token: Get the token for the storage account
        - get_secret: Get secret from Azure Key Vault
Example:
        >>> from evidi_fabric.security import get_secret
        >>> secret = get_secret("secret_name", "https://keyvault_name.vault.azure.net/")

        >>> from evidi_fabric.security import get_azure_token
        >>> token = get_azure_token()
"""

def get_azure_token():
    """
    Get the token for the storage account
    """
    from azure.identity import DefaultAzureCredential
    return DefaultAzureCredential().get_token("https://storage.azure.com/").token


def get_secret(secret_name:str, vault_url:str):
    """
    Get secret from Azure Key Vault
    """
    from azure.identity import DefaultAzureCredential
    from azure.keyvault.secrets import SecretClient
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=vault_url, credential=credential)
    secret = secret_client.get_secret(secret_name)
    secret_value = secret.value
    return secret_value