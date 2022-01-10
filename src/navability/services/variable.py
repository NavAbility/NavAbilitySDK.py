import logging
from typing import List

from gql import gql

from navability.common.queries import (
    GQL_FINDVARIABLEFACTORS,
    GQL_GETVARIABLE,
)
from navability.common.mutations import (
    GQL_ADDVARIABLE,
)
from navability.entities.Client import Client
from navability.entities.NavAbilityClient import (
    MutationOptions,
    NavAbilityClient,
    QueryOptions,
)
from navability.entities.QueryDetail import QueryDetail
from navability.entities.Variable.Variable import (
    Variable,
    VariableSchema,
    VariableSkeleton,
    VariableSkeletonSchema,
    VariableSummarySchema,
)

DETAIL_SCHEMA = {
    QueryDetail.LABEL: None,
    QueryDetail.SKELETON: VariableSkeletonSchema(),
    QueryDetail.SUMMARY: VariableSummarySchema(),
    QueryDetail.FULL: VariableSchema(),
}

logger = logging.getLogger(__name__)


def addVariable(navAbilityClient: NavAbilityClient, client: Client, v: Variable):
    return navAbilityClient.mutate(
        MutationOptions(
            gql(GQL_ADDVARIABLE),
            {"variable": {
                "client": client.dump(), 
                "packedData": v.dumpsPacked()}},
        )
    )


def ls(
    navAbilityClient: NavAbilityClient,
    client: Client,
    detail: QueryDetail = QueryDetail.SKELETON,
    regexFilter: str = ".*",
    tags: List[str] = ["VARIABLE"],
    solvable: int = 0,
) -> List[VariableSkeleton]:
    """[summary]

    Args:
        navAbilityClient (NavAbilityClient): [description]
        client (Client): [description]
        detail (QueryDetail, optional): [description]. Defaults to QueryDetail.SKELETON.
        regexFilter (str, optional): [description]. Defaults to ".*".
        tags (List[str], optional): [description]. Defaults to ["VARIABLE"].
        solvable (int, optional): [description]. Defaults to 0.

    Raises:
        Exception: [description]

    Returns:
        List[VariableSkeleton]: [description]
    """
    params = {
        "userId": client.userId,
        "robotIds": [client.robotId],
        "sessionIds": [client.sessionId],
        "variables": True,
        "factors": False,
        "variable_label_regexp": regexFilter,
        "variable_tags": tags,
        "solvable": solvable,
        "fields_summary": detail in [QueryDetail.SUMMARY, QueryDetail.FULL],
        "fields_full": detail == QueryDetail.FULL
    }
    logger.debug(f"Query params: {params}")
    res = navAbilityClient.query(QueryOptions(
        gql(GQL_FINDVARIABLEFACTORS), 
        params))
    logger.debug(f"Query result: {res}")
    # TODO: Check for errors
    schema = DETAIL_SCHEMA[detail]
    if schema is None:
        return res["VARIABLE"]
    # Using the hierarchy approach, we need to check that we have exactly one user/robot/session in it, otherwise error.
    if "USER" not in res or\
        len(res["USER"][0]["robots"]) != 1 or\
        len(res["USER"][0]["robots"][0]["sessions"]) != 1 or\
        "variables" not in res["USER"][0]["robots"][0]["sessions"][0]:
        raise Exception("Received an empty data structure, set logger to debug to see the resultant payload")
    return [schema.load(l) for l in res["USER"][0]["robots"][0]["sessions"][0]["variables"]]


def getVariable(navAbilityClient: NavAbilityClient, client: Client, label: str):
    params = client.dump()
    params["label"] = label
    logger.debug(f"Query params: {params}")
    res = navAbilityClient.query(QueryOptions(
        gql(GQL_GETVARIABLE), 
        params))
    logger.debug(f"Query result: {res}")
    # TODO: Check for errors
    # Using the hierarchy approach, we need to check that we have exactly one user/robot/session in it, otherwise error.
    if "USER" not in res or\
        len(res["USER"][0]["robots"]) != 1 or\
        len(res["USER"][0]["robots"][0]["sessions"]) != 1 or\
        "variables" not in res["USER"][0]["robots"][0]["sessions"][0]:
        raise Exception("Received an empty data structure, set logger to debug to see the resultant payload")
    vs = res["USER"][0]["robots"][0]["sessions"][0]["variables"]
    # TODO: Check for errors
    if len(vs) == 0:
        raise Exception(f"No variable {label} found")
    if len(vs) > 1:
        raise Exception(f"More than one variable named {label} returned")
    return Variable.load(vs[0])
