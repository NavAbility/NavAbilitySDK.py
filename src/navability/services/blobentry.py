import asyncio
import logging

from navability.services.loader import GQL_OPERATIONS

from navability.entities.dfgclient import DFGClient

from navability.entities.blob.blobentry import BlobEntry

from navability.entities.navabilityclient import QueryOptions

logger = logging.getLogger(__name__)


def getBlobEntry(
    fgclient: DFGClient,
    variableLabel: str,
    label: str,
):
    client = fgclient.client
    context = fgclient.context

    params = {
        "userLabel": context.userLabel,
        "robotLabel": context.robotLabel,
        "sessionLabel": context.sessionLabel,
        "variableLabel": variableLabel,
        "blobLabel": label,
    }
    logger.debug(f"Query params: {params}")
    tsk = client.query(QueryOptions(GQL_OPERATIONS["QUERY_GET_BLOBENTRY"].data, params))
    res = asyncio.run(tsk)
    logger.debug(f"Query result: {res}")
    # TODO: Check for errors
    # Using the hierarchy approach, we need to check that we have
    # exactly one user/robot/session in it, otherwise error.
    if (
        "users" not in res
        or len(res["users"]) != 1
        or len(res["users"][0]["robots"]) != 1
        or len(res["users"][0]["robots"][0]["sessions"]) != 1
        or "variables" not in res["users"][0]["robots"][0]["sessions"][0]
    ):
        # Debugging information
        if len(res["users"]) != 1:
            logger.warn("User not found in result, returning empty list")
        if len(res["users"][0]["robots"]) != 1:
            logger.warn("Robot not found in result, returning empty list")
        if len(res["users"][0]["robots"][0]["sessions"]) != 1:
            logger.warn("Robot not found in result, returning empty list")
        return []

    entries = res["users"][0]["robots"][0]["sessions"][0]["variables"][0]["blobEntries"]

    if len(entries) == 0:
        return None
    if len(entries) > 1:
        raise Exception(f"More than one variable named {label} returned")

    return BlobEntry.load(entries[0])
