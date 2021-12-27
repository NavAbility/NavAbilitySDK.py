import logging
from typing import List

from gql import gql

from navability.common.queries import (
    gql_addVariable,
    gql_list,
    gql_list_fields_default,
    gql_list_fields_variable,
    gql_list_fields_variable_skeleton,
    gql_list_fields_variable_summary,
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
DETAIL_FIELDS = {
    QueryDetail.LABEL: gql_list_fields_default,
    QueryDetail.SKELETON: gql_list_fields_variable_skeleton,
    QueryDetail.SUMMARY: gql_list_fields_variable_summary,
    QueryDetail.FULL: gql_list_fields_variable,
}

logger = logging.getLogger(__name__)


def addVariable(navAbilityClient: NavAbilityClient, client: Client, v: Variable):
    return navAbilityClient.mutate(
        MutationOptions(
            gql(gql_addVariable),
            {"variable": {"client": client.dump(), "packedData": v.dumpsPacked()}},
        )
    )


def _getVariables(
    navAbilityClient: NavAbilityClient,
    client: Client,
    detail: QueryDetail,
    labelExact: str = None,
    regexFilter: str = None,
    tags: List[str] = None,
    solvable: int = 0,
) -> VariableSkeleton:
    query = gql_list.replace("__TYPE__", "VARIABLE").replace(
        "__FIELDS__", DETAIL_FIELDS[detail]
    )
    params = client.dump()
    params["solvable"] = solvable
    # These cannot be populated with Nones
    if regexFilter is not None:
        params["labelRegex"] = regexFilter
    if tags is not None:
        params["tags"] = tags
    if labelExact is not None:
        params["labelExact"] = labelExact
    logger.debug(f"Query params: {params}")
    logger.debug(f"Query query: {query}")
    res = navAbilityClient.query(QueryOptions(gql(query), params))
    logger.debug(f"Query result: {res}")
    # TODO: Check for errors
    schema = DETAIL_SCHEMA[detail]
    if schema is None:
        return res["VARIABLE"]
    return [schema.load(l) for l in res["VARIABLE"]]


def ls(
    navAbilityClient: NavAbilityClient,
    client: Client,
    regexFilter: str = None,
    tags: List[str] = None,
    solvable: int = 0,
):
    return [
        v.label
        for v in _getVariables(
            navAbilityClient,
            client,
            QueryDetail.SKELETON,
            regexFilter=regexFilter,
            tags=tags,
            solvable=solvable,
        )
    ]


def getVariable(navAbilityClient: NavAbilityClient, client: Client, label: str):
    v = _getVariables(navAbilityClient, client, QueryDetail.FULL, labelExact=label)
    # TODO: Check for errors
    if len(v) == 0:
        raise Exception(f"No variable {label} found")
    if len(v) > 1:
        raise Exception(f"More than one variable named {label} returned")

    return v[0]
