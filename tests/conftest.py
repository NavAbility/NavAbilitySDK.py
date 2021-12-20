import logging
import os
import time
import urllib.request
from uuid import uuid4

import pytest

from navability.entities.Client import Client
from navability.entities.NavAbilityClient import (
    NavAbilityClient,
    NavAbilityHttpsClient,
    NavAbilityWebsocketClient,
)

# setup basic logging to stderr
logging.basicConfig(level=logging.INFO)

_env_configs = {
    "local": {
        "navability_client": {
            "url_websocket": "wss://localhost:5000/graphql",
            "url_https": "https://localhost:5000",
        }
    },
    "dev": {
        "navability_client": {
            "url_websocket": "wss://api.d1.navability.io/graphql",
            "url_https": "https://api.d1.navability.io",
        }
    },
    "production": {},
}

SDK_ENV = os.environ.get("NAVABILITY_ENVIRONMENT", "dev")


@pytest.fixture
def env_config():
    return _env_configs[SDK_ENV]


@pytest.fixture
def navability_wss_client(env_config) -> NavAbilityClient:
    return NavAbilityWebsocketClient(
        url=env_config["navability_client"]["url_websocket"]
    )


@pytest.fixture
def navability_https_client(env_config) -> NavAbilityClient:
    return NavAbilityHttpsClient(url=env_config["navability_client"]["url_https"])


@pytest.fixture
def client(env_config) -> Client:
    return Client("Guest", "PySDKTests", str(uuid4())[0:8])
