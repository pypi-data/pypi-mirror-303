from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import logging

def get_secret_value(secret_name, vault_url, queue=None, credential=DefaultAzureCredential()):
    try:
        client = SecretClient(vault_url=vault_url, credential=credential)
        secret = client.get_secret(secret_name)
        return secret.value
    except Exception as e:
        message = f"Error getting secret {secret_name}: {e}"
        if queue != None:
            queue.add('ERROR', message)
        else:
            logging.error(message)
    return None

def get_config_dict(secret_name, keyvault_url):
    db_config_str = get_secret_value(secret_name, keyvault_url)
    db_config_split = db_config_str.split(',')
    keys = ['dbname', 'user', 'password', 'host']
    return {k: v for k, v in zip(keys, db_config_split)}

def get_key_url(secret_name, keyvault_url, queue):
    try:
        value = get_secret_value(secret_name, keyvault_url)
        index = value.find('/')
        return value[:index], value[index+1:]
    except Exception as e:
        queue.add('ERROR', f"Error getting key URL {secret_name}: {e}")
        raise e