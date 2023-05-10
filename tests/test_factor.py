import asyncio

import pytest

from navability.entities import Client, DFGClient
from navability.services import lsf, getFactor, getFactors


def test_hex_lsf():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    assert set(['x6l1f1', 'x0l1f1', 'x5x6f1', 'x4x5f1', 'x3x4f1', 'x2x3f1', 'x1x2f1', 'x0x1f1', 'x0f1']).issubset(set(lsf(fgclient)))


def test_hex_getFactor():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    fac = getFactor(fgclient, "x0x1f1")
    assert fac.label == "x0x1f1"


def test_hex_getFactors():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    facs = getFactors(fgclient)
    assert len(facs) >= 9


@pytest.mark.skip
@pytest.mark.asyncio
async def test_lsf(example_2d_graph):
    navability_client, client, variables, factors = example_2d_graph
    assert set(await lsf(navability_client, client)) == set([f.label for f in factors])


@pytest.mark.skip
@pytest.mark.asyncio
async def test_lsf_no_session(example_2d_graph):
    navability_client, client, variables, factors = example_2d_graph
    noSessionClient = Client(client.userId, client.robotId, "DoesntExist")
    assert await lsf(navability_client, noSessionClient) == []


# def test_getFactor(example_2d_graph):
#     navability_client, client, variables, factors = example_2d_graph
#     assert (
#         getFactor(navability_client, client, factors[0].label).label
#         == variables[0].label
#     )

# Redefining the event loop so we can we can use module-level fixtures.
@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
