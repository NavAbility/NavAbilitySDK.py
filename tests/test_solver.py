import asyncio

import pytest

from navability.services import getVariable


@pytest.mark.asyncio
async def test_solveSession_1d(example_1d_graph_solved):
    navability_client, client, variables, factors = example_1d_graph_solved
    ppes = {
        v: (await getVariable(navability_client, client, v)).ppes["default"]
        for v in variables
    }
    assert len(ppes) == 4


@pytest.mark.asyncio
async def test_solveSession_2d(example_2d_graph_solved):
    navability_client, client, variables, factors = example_2d_graph_solved
    v = await getVariable(navability_client, client, variables[0].label)
    assert "default" in v.ppes
    assert v.ppes["default"].solveKey == "default"
    assert len(v.ppes["default"].suggested) == 3


# Redefining the event loop so we can we can use module-level fixtures.
@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
