import os
import json
import botocore 
import botocore.session 
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig 
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


def get_secret(secret_name: str):
    secret = os.environ.get(secret_name, None)
    return secret or get_value_from_secret_manager(secret_name)
    

def get_value_from_secret_manager(secret_name: str):
    client = botocore.session.get_session().create_client('secretsmanager')
    cache_config = SecretCacheConfig()
    cache = SecretCache( config = cache_config, client = client)
    secret = json.loads(cache.get_secret_string(secret_name))
    return secret.get(secret_name, "")