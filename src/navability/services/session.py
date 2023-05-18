import logging
import asyncio
from navability.entities.navabilityclient import (
    NavAbilityClient,
    # QueryOptions,
    MutationOptions,
)
from navability.entities.session import SessionSchema
from navability.services.loader import GQL_OPERATIONS
from navability.common.versions import payload_version

import nest_asyncio
nest_asyncio.apply()

logger = logging.getLogger(__name__)


async def addSessionAsync(
    navAbilityClient: NavAbilityClient,
    userLabel: str,
    robotLabel: str,
    sessionLabel: str,
):
    """Add a new session to the given user and robot.

    Args:
        navAbilityClient (NavAbilityClient): The NavAbility client.
    """
    params = {
        "userLabel": userLabel,
        "robotLabel": robotLabel,
        "sessionLabel": sessionLabel,
        "version": payload_version,
    }
    result = await navAbilityClient.mutate(
        MutationOptions(
            GQL_OPERATIONS["MUTATION_ADD_SESSION"].data,
            params,
        )
    )

    return SessionSchema().load(result["addSessions"]['sessions'][0])


def addSession(
    navAbilityClient: NavAbilityClient,
    userLabel: str,
    robotLabel: str,
    sessionLabel: str,
):
    tsk = addSessionAsync(navAbilityClient, userLabel, robotLabel, sessionLabel)
    return asyncio.run(tsk)
