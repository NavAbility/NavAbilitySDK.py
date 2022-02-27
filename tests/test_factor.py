import asyncio

import pytest

from navability.entities import Client
from navability.services import lsf  # getFactor


@pytest.mark.asyncio
async def test_lsf(example_graph):
    navability_client, client, variables, factors = example_graph
    assert set(await lsf(navability_client, client)) == set([f.label for f in factors])


@pytest.mark.asyncio
async def test_lsf_no_session(example_graph):
    navability_client, client, variables, factors = example_graph
    noSessionClient = Client(client.userId, client.robotId, "DoesntExist")
    assert await lsf(navability_client, noSessionClient) == []


# def test_getFactor(example_graph):
#     navability_client, client, variables, factors = example_graph
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
