import asyncio

import pytest

from navability.entities import Client, DFGClient
from navability.services.variable import getVariable, ls


def test_hex_ls():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    assert set(ls(fgclient)) == set(['x4', 'x1', 'x0', 'x3', 'x2', 'x6', 'x5', 'l1'])


def test_hex_getVariable():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    var = getVariable(fgclient, "x1")
    assert var.label == "x1" and 'default' in var.solverData.keys()


@pytest.mark.skip
@pytest.mark.asyncio
def test_ls(example_2d_graph):
    navability_client, client, variables, factors = example_2d_graph
    fgclient = DFGClient(navability_client, client)
    assert set(ls(fgclient)) == set([v.label for v in variables])


@pytest.mark.skip
@pytest.mark.asyncio
async def test_ls_no_session(example_2d_graph):
    navability_client, client, variables, factors = example_2d_graph
    noSessionClient = Client(client.userId, client.robotId, "DoesntExist")
    assert (await ls(navability_client, noSessionClient)) == []


@pytest.mark.skip
@pytest.mark.asyncio
async def test_getVariable(example_2d_graph):
    navability_client, client, variables, factors = example_2d_graph
    fgclient = DFGClient(navability_client, client)
    variable = await getVariableAsync(fgclient, variables[0].label)
    assert variable.label == variables[0].label


# Redefining the event loop so we can we can use module-level fixtures.
@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
