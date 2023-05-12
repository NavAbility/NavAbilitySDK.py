
import logging
from typing import List
from uuid import uuid4

from gql import gql

import asyncio

from navability.entities.dfgclient import DFGClient



async def listNeighborsAsync(fgclient: DFGClient, nodeLabe: str) -> List[str]:

    client = fgclient.client
    context = fgclient.context

    params = {
        "userLabel": context.userLabel,
        "robotLabel": context.robotLabel,
        "sessionLabel": context.sessionLabel,
        "nodeLabel": context.nodeLabel
    }

    logger.debug(f"Query params: {params}")
    res = await client.query(
        QueryOptions(GQL_OPERATIONS["QUERY_LIST_NEIGHBORS"].data, params)
    )

    logger.debug(f"Query result: {res}")
    # TODO: Check for errors
    # Using the hierarchy approach, we need to check that we
    # have exactly one user/robot/session in it, otherwise error.
    if (
        "users" not in res
        or len(res["users"][0]["robots"]) != 1
        or len(res["users"][0]["robots"][0]["sessions"]) != 1
        or "factors" not in res["users"][0]["robots"][0]["sessions"][0]
    ):
        raise Exception(
            "Received an empty data structure, set logger to debug for the payload"
        )

    var_or_fac = res["users"][0]["robots"][0]["sessions"][0]

    if ( len(var_or_fac["variables"]) > 0):
        flbls = [r["variables"][0]["factors"] for r in var_or_fac]
    if ( len(var_or_fac["factors"]) > 0):
        vlbls = [r["factors"][0]["variables"] for r in var_or_fac]

    neigh_list = []
    _lb = lambda s: s['label']
    [neigh_list.append(_lb(f)) for f in flbls]
    [neigh_list.append(_lb(f)) for f in vlbls]

    return neigh_list
