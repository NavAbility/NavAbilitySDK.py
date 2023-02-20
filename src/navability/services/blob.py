import logging
import warnings
from typing import List

from gql import gql

# from navability.common.mutations import GQL_ADDVARIABLE
from navability.common.queries import (
    GQL_LISTDATAENTRIES,
)
from navability.entities.client import Client
from navability.entities.navabilityclient import (
    MutationOptions,
    NavAbilityClient,
    QueryOptions,
)
# from navability.entities.querydetail import QueryDetail
from navability.entities.blob.blob import (
    BlobEntry,
    BlobEntrySchema,
)


logger = logging.getLogger(__name__)

async def listBlobEntries(
    client: NavAbilityClient,
    context: Client,
    variableLabel,
):
    """ List the blob entries associated with a particular variable.

    Args:
        client (NavAbilityClient): client connection to API server
        context (Client): Unique context with (user, robot, session)
        variableLabel (string): list data entries connected to which variable

    Returns:
        _type_: coroutine containing a list of `BlobEntry`s

    """
    params = {
        "userId": context.userId,
        "robotId": context.robotId,
        "sessionId": context.sessionId,
        "variableLabel": variableLabel,
    }
    logger.debug(f"Query params: {params}")
    res = await client.query(
        QueryOptions(gql(GQL_LISTDATAENTRIES), params)
    )
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
    _lb = lambda s: s['label']
    resdata = res['users'][0]['robots'][0]['sessions'][0]['variables'][0]['data']
    ret = []
    [ret.append(_lb(v)) for v in resdata]

    schema = BlobEntrySchema()
    # schema = None
    if schema is None:
        return ret
    return [
        schema.load(l) for l in resdata
    ]
    # for d in listdata
    #   tupk = Tuple(Symbol.(keys(d)))
    #   nt = NamedTuple{tupk}( values(d) )
    #   push!(ret,
    #     nt
    #   )
    # end
    # return ret

async def listDataEntries(
    client: NavAbilityClient,
    context: Client,
    variableLabel,
):
    warnings.warn('listDataEntries is deprecated, use listBlobEntries instead.')
    return await listBlobEntries(client, context, variableLabel)