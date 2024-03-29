import asyncio

import pytest

from navability.entities import DFGClient
from navability.services.variable import getVariable, getVariables, ls, getPPE


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


def test_hex_getVariables():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    variables = getVariables(fgclient)
    assert len(variables) == 8


def test_hex_getPPE():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    ppe = getPPE(fgclient, "x1", "default")
    assert ppe.solveKey == "default"


@pytest.mark.skip
@pytest.mark.asyncio
def test_ls(example_2d_graph):
    navability_client, client, variables, factors = example_2d_graph
    fgclient = DFGClient(client.userLabel, client.robotLabel, client.sessionLabel)
    assert set(ls(fgclient)) == set([v.label for v in variables])


@pytest.mark.skip
@pytest.mark.asyncio
async def test_ls_no_session(example_2d_graph):
    navability_client, client, variables, factors = example_2d_graph
    #TODO I would say that this should already give an error
    nofgclient = DFGClient(client.userLabel, client.robotLabel, "DoesntExist")
    assert (await ls(navability_client, nofgclient)) == []


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
