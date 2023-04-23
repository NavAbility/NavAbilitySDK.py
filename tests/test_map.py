import asyncio
from uuid import uuid4

import pytest

from navability.entities import Client
from navability.entities.navabilityclient import NavAbilityClient
from navability.entities.user import User
from navability.services.map import getMap, getMaps
from navability.services.user import getUser, getUsers
from navability.services.variable import getVariable, ls

# Add a fixture for the guest user
@pytest.fixture(scope="module")
async def guest_user(navability_https_client: NavAbilityClient) -> User:
    return await getUser(navability_https_client, "guest@navability.io")

## TODO: Create a map as a fixture and delete it after.

@pytest.mark.asyncio
async def test_getMaps_shouldSucceed(navability_https_client: NavAbilityClient, guest_user: User):
    # Arrange: Nothing
    # Act: Get all maps
    maps = await getMaps(navability_https_client, guest_user.id)
    # Make sure the map exists
    assert set([m.label for m in maps]) == set(["ExampleMap"])


@pytest.mark.asyncio
async def test_getMap_shouldSucceed(navability_https_client: NavAbilityClient, guest_user: User):
    # Arrange: Get all maps
    maps = await getMaps(navability_https_client, guest_user.id)
    print(maps)
    # Act: Get the first map
    map = await getMap(navability_https_client, guest_user.id, maps[0].id)
    # Make sure the map is correctly returned
    assert maps[0].id == map.id


@pytest.mark.asyncio
async def test_getMaps_doesntExist(navability_https_client: NavAbilityClient):
    # Arrange: None
    # Act: Get maps for nonsense
    with pytest.raises(Exception) as ex:
        maps = await getMaps(navability_https_client, "derp@testing.io")
    # Assert: We don't get anything
    assert "The query did not return a user or a list of maps" in str(ex.value)


@pytest.mark.asyncio
async def test_getMap_doesntExist(navability_https_client: NavAbilityClient, guest_user: User):
    # Arrange: None
    # Act: Get a map that doesn't exist
    with pytest.raises(Exception) as ex:
        user = await getMap(navability_https_client, guest_user.id, uuid4())
    # Assert: Server-side validation failed
    assert "No map with Id" in str(ex.value)  


# Redefining the event loop so we can we can use module-level fixtures.
@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
