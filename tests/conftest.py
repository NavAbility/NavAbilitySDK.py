import logging
import os
import time
from uuid import uuid4

import numpy as np
import pytest

from navability.entities.Client import Client
from navability.entities.factor.distributions import FullNormal
from navability.entities.factor.factor import Factor, FactorData
from navability.entities.factor.inferencetypes import Pose2Pose2, PriorPose2
from navability.entities.NavAbilityClient import (
    NavAbilityClient,
    NavAbilityHttpsClient,
    NavAbilityWebsocketClient,
)
from navability.entities.Variable.Variable import Variable
# from navability.services.Factor import addFactor
from navability.services.Status import getStatusLatest
from navability.services.Variable import addVariable

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


@pytest.fixture(scope="session")
def env_config():
    return _env_configs[SDK_ENV]


@pytest.fixture(scope="module")
def navability_wss_client(env_config) -> NavAbilityClient:
    return NavAbilityWebsocketClient(
        url=env_config["navability_client"]["url_websocket"]
    )


@pytest.fixture(scope="module")
def navability_https_client(env_config) -> NavAbilityClient:
    return NavAbilityHttpsClient(url=env_config["navability_client"]["url_https"])


@pytest.fixture(scope="module")
def client(env_config) -> Client:
    return Client("Guest", "PySDKAutomation", str(uuid4())[0:8])


@pytest.fixture(scope="module")
def example_graph(navability_wss_client: NavAbilityClient, client: Client):
    variables = [
        Variable(label="x0", variableType="Pose2"),
        Variable(label="x1", variableType="Pose2"),
        Variable(label="x2", variableType="Pose2"),
    ]
    factors = [
        Factor(
            "x0f1",
            FactorData(
                fnc=PriorPose2(
                    z=FullNormal(mean=np.zeros(3), covariance=np.diag([0.1, 0.1, 0.1]))
                ).dump()  # This is a generator for a PriorPose2
            ),
            ["x0"],
        ),
        Factor(
            "x0x1f1",
            FactorData(
                fnc=Pose2Pose2(
                    z=FullNormal(
                        mean=[1, 1, np.pi / 3], covariance=np.diag([0.1, 0.1, 0.1])
                    )
                ).dump()  # This is a generator for a PriorPose2
            ),
            ["x0", "x1"],
        ),
        Factor(
            "x1x2f1",
            FactorData(
                fnc=Pose2Pose2(
                    z=FullNormal(
                        mean=[1, 1, np.pi / 3], covariance=np.diag([0.1, 0.1, 0.1])
                    )
                ).dump()  # This is a generator for a PriorPose2
            ),
            ["x1", "x2"],
        ),
    ]
    # Variables
    result_ids = [
        addVariable(navability_wss_client, client, v)["addVariable"] for v in variables
    ]  # WIP[addFactor(navability_wss_client, client, f)["addFactor"] for f in factors]

    wait_time = 60
    while any(
        [
            getStatusLatest(navability_wss_client, res).state != "Complete"
            for res in result_ids
        ]
    ):
        time.sleep(1)
        wait_time -= 1
        if wait_time <= 0:
            raise Exception("Variable wasn't loaded in time")

    return (navability_wss_client, client, variables, factors)
