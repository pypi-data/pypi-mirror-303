# Downer Azure Helper

Collection of functions to wrap the Azure SDK.

## Get Secret Value

Retrieve the value of a keyvault secret.

### Example Usage

```python
from downerhelper.secrets import get_secret_value

value = get_secret_value(secret_name, keyvault_url)
```

## Postgres Log Handler

Simple handler to enter logs directly to postgres databases, uses psycopg2 for connection. Creates a new `table` if does not already exist, and groups logs by `job_id`.

### Quick Setup

Store database config in Azure Key Vault with format `<dbname>,<user>,<password>,<host>`.

#### Example Usage

```python
from downerhelper.logs import setup_handler

logger, job_id = setup_handler(secret_name: str, keyvault_url: str, logger_name: str, table: str, job_id=None: str)
logger.info("this is a test info message")
```

### Manual Setup

Provide database config dictionary.

#### Example Usage


```python
from downerhelper.logs import PostgresLogHandler

db_config = {
    'dbname': <dbname>,
    'user': <user>,
    'password': <password>,
    'host': <host>,
}

logger = PostgresLogHandler(logger_name: str, job_id: str, table: str, db_config: dict(str, str))
logger.info("this is a test info message")
```

## Warning

The following snippet shows incorrect usage. Modules must be declared and imported seperately.

```python
import downerhelper

value = downerhelper.secrets.get_secret_value(secret_name, keyvault_url)
```