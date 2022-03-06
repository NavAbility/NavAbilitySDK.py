import logging
import os
from uuid import uuid4

import numpy as np
import pytest

from navability.entities import (
    Client,
    Factor,
    FactorData,
    FullNormal,
    NavAbilityClient,
    NavAbilityHttpsClient,
    NavAbilityWebsocketClient,
    Pose2Pose2,
    PriorPose2,
    Variable,
    VariableType,
)
from navability.services import addFactor, addVariable, solveSession, waitForCompletion

# setup basic logging to stderr
logging.basicConfig(level=logging.WARN)

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

SDK_ENV = os.environ.get("NVA_ENVIRONMENT", "dev")


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
    return Client("Guest", "PySDKAutomation", "Session_" + str(uuid4())[0:8])


@pytest.fixture(scope="module")
async def example_2d_graph(navability_https_client: NavAbilityClient, client: Client):
    variables = [
        Variable("x0", VariableType.Pose2.value),
        Variable("x1", VariableType.Pose2.value),
        Variable("x2", VariableType.Pose2.value),
    ]
    factors = [
        Factor(
            "x0f1",
            "PriorPose2",
            ["x0"],
            FactorData(
                fnc=PriorPose2(
                    Z=FullNormal(mu=np.zeros(3), cov=np.diag([0.1, 0.1, 0.1]))
                ).dump()  # This is a generator for a PriorPose2
            ),
        ),
        Factor(
            "x0x1f1",
            "Pose2Pose2",
            ["x0", "x1"],
            FactorData(
                fnc=Pose2Pose2(
                    Z=FullNormal(mu=[1, 1, np.pi / 3], cov=np.diag([0.1, 0.1, 0.1]))
                ).dump()  # This is a generator for a PriorPose2
            ),
        ),
        Factor(
            "x1x2f1",
            "Pose2Pose2",
            ["x1", "x2"],
            FactorData(
                fnc=Pose2Pose2(
                    Z=FullNormal(mu=[1, 1, np.pi / 3], cov=np.diag([0.1, 0.1, 0.1]))
                ).dump()  # This is a generator for a PriorPose2
            ),
        ),
    ]
    # Variables
    result_ids = [
        await addVariable(navability_https_client, client, v) for v in variables
    ] + [await addFactor(navability_https_client, client, f) for f in factors]

    logging.info(f"[Fixture] Adding variables and factors, waiting for completion")

    # Await for only Complete messages, otherwise fail.
    await waitForCompletion(
        navability_https_client,
        result_ids,
        expectedStatuses=["Complete"],
        maxSeconds=120,
    )

    return (navability_https_client, client, variables, factors)


@pytest.fixture(scope="module")
async def example_2d_graph_solved(example_2d_graph):
    """Get the graph after it has been solved.
    NOTE this changes the graph, so tests need to be defensive.
    """
    navability_https_client, client, variables, factors = example_2d_graph
    logging.info(f"[Fixture] Solving graph, client = {client.dumps()}")
    requestId = await solveSession(navability_https_client, client)
    await waitForCompletion(navability_https_client, [requestId], maxSeconds=180)
    return (navability_https_client, client, variables, factors)
