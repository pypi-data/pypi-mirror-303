# How to use
Generate a whl file by running the following command
```bash
poetry build
```

Upload the generated whl file in the dist folder to the environment in Microsoft Fabric

Import the package in a notebook

```python
from firestart_utils.logger import get_logger
```

Create a logger object
```python
logger = get_logger("{DATADOG_API_KEY}", "{CUSTOMER}", "{ENVIROMENT}", "{WORKSPACE_NAME}", "{LOG_LEVEL_TRESHOLD}")
```

Default logging. If given threshold is met it will be send towards datadog, 

!IMPORTANT! The source is mandatory and should be used in every default log for tracking in DataDog

```python
logger.info("{SOURCE}", "This is a test message") 
logger.warning("{SOURCE}", "This is a test message") 
logger.critical("{SOURCE}", "This is a test message") 
logger.debug("{SOURCE}", "This is a test message") 
```

Logging pipeline metrics DataDog
```python
logger.failed("{SOURCE}")
logger.success("{SOURCE}")
```

# Development
## Setup Environment
Install poetry using the following command
```bash
pip install poetry
```

# Start Enviroment
To start the environment, run the following command
```bash
poetry shell
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Build Project
```bash
poetry build
```

## Run Tests
```bash
python -m unittest discover
```
