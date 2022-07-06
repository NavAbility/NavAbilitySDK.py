import logging
import os
from collections import OrderedDict
from uuid import uuid4

import numpy as np
import pytest

from navability.entities import (
    Client,
    Factor,
    FactorData,
    FullNormal,
    LinearRelative,
    Mixture,
    NavAbilityClient,
    NavAbilityHttpsClient,
    NavAbilityWebsocketClient,
    Normal,
    Pose2Point2BearingRange,
    Pose2Point2Range,
    Pose2Pose2,
    Prior,
    PriorPoint2,
    PriorPose2,
    Uniform,
    Variable,
    VariableType,
)
from navability.entities.solve import SolveOptions
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
            "url_websocket": "wss://api.navability.io/graphql",
            "url_https": "https://api.navability.io",
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
def client_1d(env_config) -> Client:
    return Client(
        "guest@navability.io", "PySDKAutomation", "Session_1D_" + str(uuid4())[0:8]
    )


@pytest.fixture(scope="module")
def client_2d(env_config) -> Client:
    return Client(
        "guest@navability.io", "PySDKAutomation", "Session_2D_" + str(uuid4())[0:8]
    )


@pytest.fixture(scope="module")
async def example_1d_graph(
    navability_https_client: NavAbilityClient, client_1d: Client
):
    # Using the new signatures to validate both new and old addVariable/addFactor
    variables = ["x0", "x1", "x2", "x3"]
    factors = [
        (["x0"], Prior(Normal(0, 1))),
        (["x0", "x1"], LinearRelative(Normal(10, 0.1))),
        (
            ["x1", "x2"],
            Mixture(
                LinearRelative,
                OrderedDict([("hypo1", Normal(0, 2)), ("hypo2", Uniform(30, 55))]),
                [0.4, 0.6],
                2,
            ),
        ),
        (["x2", "x3"], LinearRelative(Normal(-50, 1))),
        (["x3", "x0"], LinearRelative(Normal(40, 1))),
    ]
    # Variables
    result_ids = [
        await addVariable(
            navability_https_client, client_1d, v, VariableType.ContinuousScalar
        )
        for v in variables
    ] + [await addFactor(navability_https_client, client_1d, *f) for f in factors]

    logging.info(f"[Fixture] Adding variables and factors, waiting for completion")

    # Await for only Complete messages, otherwise fail.
    await waitForCompletion(
        navability_https_client,
        result_ids,
        expectedStatuses=["Complete"],
        maxSeconds=120,
    )

    return (navability_https_client, client_1d, variables, factors)


@pytest.fixture(scope="module")
async def example_1d_graph_solved(example_1d_graph):
    """Get the graph after it has been solved.
    NOTE this changes the graph, so tests need to be defensive.
    """
    navability_https_client, client, variables, factors = example_1d_graph
    logging.info(f"[Fixture] Solving graph, client = {client.dumps()}")
    requestId = await solveSession(navability_https_client, client)
    await waitForCompletion(navability_https_client, [requestId], maxSeconds=180)
    return (navability_https_client, client, variables, factors)


@pytest.fixture(scope="module")
async def example_2d_graph(
    navability_https_client: NavAbilityClient, client_2d: Client
):
    variables = [
        Variable("x0", VariableType.Pose2.value),
        Variable("x1", VariableType.Pose2.value),
        Variable("x2", VariableType.Pose2.value),
        Variable("l0", VariableType.Point2.value),
    ]
    factors = [
        Factor(
            "x0f1",
            "PriorPose2",
            ["x0"],
            FactorData(
                fnc=PriorPose2(
                    FullNormal(np.zeros(3), np.diag([0.1, 0.1, 0.1]))
                ).dump()  # This is a generator for a PriorPose2
            ),
        ),
        Factor(
            "x0x1f1",
            "Pose2Pose2",
            ["x0", "x1"],
            FactorData(
                fnc=Pose2Pose2(
                    FullNormal([1, 1, np.pi / 3], np.diag([0.1, 0.1, 0.1]))
                ).dump()  # This is a generator for a PriorPose2
            ),
        ),
        Factor(
            "x1x2f1",
            "Pose2Pose2",
            ["x1", "x2"],
            FactorData(
                fnc=Pose2Pose2(
                    FullNormal([1, 1, np.pi / 3], np.diag([0.1, 0.1, 0.1]))
                ).dump()  # This is a generator for a PriorPose2
            ),
        ),
        # TODO: Improve problem setup in future.
        Factor(
            "l0f1",
            "PriorPoint2",
            ["l0"],
            FactorData(
                fnc=PriorPoint2(FullNormal(np.asarray([5, 0]), np.diag([2, 2]))).dump()
            ),
        ),
        Factor(
            "x0l0f1",
            "Pose2Point2Range",
            ["x0", "l0"],
            FactorData(fnc=Pose2Point2Range(Normal(5, 0.1)).dump()),  # Range
        ),
        Factor(
            "x0l0f2",
            "Pose2Point2BearingRange",
            ["x0", "l0"],
            FactorData(
                fnc=Pose2Point2BearingRange(
                    Normal(0, 0.3), Normal(5, 0.1)  # Bearing, range
                ).dump()
            ),
        ),
    ]
    # Variables
    result_ids = [
        await addVariable(navability_https_client, client_2d, v) for v in variables
    ] + [await addFactor(navability_https_client, client_2d, f) for f in factors]

    logging.info(f"[Fixture] Adding variables and factors, waiting for completion")

    # Await for only Complete messages, otherwise fail.
    await waitForCompletion(
        navability_https_client,
        result_ids,
        expectedStatuses=["Complete"],
        maxSeconds=120,
    )

    return (navability_https_client, client_2d, variables, factors)


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


@pytest.fixture(scope="module")
async def example_2d_graph_solved_parametric(example_2d_graph):
    """Get the graph after it has been solved.
    NOTE this changes the graph, so tests need to be defensive.
    """
    navability_https_client, client, variables, factors = example_2d_graph
    logging.info(f"[Fixture] Solving graph, client = {client.dumps()}")
    # Note the parametric key is not needed here, it is overwritten by default.
    requestId = await solveSession(
        navability_https_client, client, SolveOptions("parametric", True)
    )
    await waitForCompletion(navability_https_client, [requestId], maxSeconds=180)
    return (navability_https_client, client, variables, factors)
