import asyncio

import pytest

from navability.entities import Client
from navability.entities.navabilityclient import NavAbilityClient
from navability.services.user import getUser, getUsers
from navability.services.variable import getVariable, ls


@pytest.mark.asyncio
async def test_getUsers_shouldSucceed(navability_https_client: NavAbilityClient):
    users = await getUsers(navability_https_client)
    assert set([u.label for u in users]) == set(["guest@navability.io"])


@pytest.mark.asyncio
async def test_getUser_shouldSucceed(navability_https_client: NavAbilityClient):
    # Arrange: None
    # Act: Get a user 
    user = await getUser(navability_https_client, "guest@navability.io")
    # Assert: We got one
    assert user.label == "guest@navability.io"


@pytest.mark.asyncio
async def test_getUser_doesntExist(navability_https_client: NavAbilityClient):
    # Arrange: None
    # Act: Get a user 
    user = await getUser(navability_https_client, "derp@testing.io")
    # Assert: We got one
    assert user is None


@pytest.mark.asyncio
async def test_getUser_BadUsername(navability_https_client: NavAbilityClient):
    # Arrange: None
    # Act: Get a user that fails validation
    with pytest.raises(Exception) as ex:
        user = await getUser(navability_https_client, "IDontWork")
    # Assert: Server-side validation failed
    assert "Value is not a valid email address: IDontWork" in str(ex.value)  


# Redefining the event loop so we can we can use module-level fixtures.
@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
