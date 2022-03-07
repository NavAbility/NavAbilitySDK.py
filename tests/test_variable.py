import asyncio

import pytest

from navability.entities import Client
from navability.services.variable import getVariable, ls


@pytest.mark.asyncio
async def test_ls(example_2d_graph):
    navability_client, client, variables, factors = example_2d_graph
    assert set(await ls(navability_client, client)) == set([v.label for v in variables])


@pytest.mark.asyncio
async def test_ls_no_session(example_2d_graph):
    navability_client, client, variables, factors = example_2d_graph
    noSessionClient = Client(client.userId, client.robotId, "DoesntExist")
    assert (await ls(navability_client, noSessionClient)) == []


@pytest.mark.asyncio
async def test_getVariable(example_2d_graph):
    navability_client, client, variables, factors = example_2d_graph
    variable = await getVariable(navability_client, client, variables[0].label)
    assert variable.label == variables[0].label


# Redefining the event loop so we can we can use module-level fixtures.
@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
