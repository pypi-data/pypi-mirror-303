import pytest
from dotenv import load_dotenv
import os
from downerhelper.logs import setup_queue
from uuid import uuid4

@pytest.fixture(scope="session", autouse=True)
def setup_session():
    load_dotenv()

@pytest.fixture(scope="session")
def keyvault_url():
    return os.getenv('KEYVAULT_URL')

@pytest.fixture(scope="session")
def feature_service():
    return os.getenv('FEATURE_SERVICE')

@pytest.fixture(scope="session")
def queue(keyvault_url):
    return setup_queue('pytest', str(uuid4()), os.getenv('LOG_TABLE'), 'db-config-1', keyvault_url)

@pytest.fixture(scope="session")
def qgis_creds():
    root = os.getenv('QGIS_ROOT')
    username = os.getenv('QGIS_USERNAME')
    pwd = os.getenv('QGIS_PWD')
    return root, username, pwd