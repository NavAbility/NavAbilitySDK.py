from typing import List

from gql import gql

from navability.common.queries import (
    gql_addVariable,
    gql_list,
    gql_list_fields_default,
    gql_list_fields_variable
)
from navability.entities.Client import Client
from navability.entities.NavAbilityClient import (
    MutationOptions,
    NavAbilityClient,
    QueryOptions,
)
from src.navability.entities.Variable.Variable import Variable


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
    fields: str,
    regexFilter: str = None,
    tags: List[str] = None,
    solvable: int = 0,
):
    query = gql_list.replace("__TYPE__", "VARIABLE").replace("__FIELDS__", fields)
    params = client.dump()
    params["solvable"] = solvable
    # These cannot be populated with Nones
    if regexFilter is not None:
        params["labelRegex"] = regexFilter
    if tags is not None:
        params["tags"] = tags
    ls = navAbilityClient.query(QueryOptions(gql(query),params))
    # TODO: Check for errors
    return ls["VARIABLE"]


def ls(
    navAbilityClient: NavAbilityClient,
    client: Client,
    regexFilter: str = None,
    tags: List[str] = None,
    solvable: int = 0
):
    return [v["label"] for v in 
        _getVariables(navAbilityClient, client, gql_list_fields_default, regexFilter, tags, solvable)]


def getVariable(navAbilityClient: NavAbilityClient, client: Client, label: str):
    query = gql_list.replace("__TYPE__", "VARIABLE").replace(
                    "__FIELDS__", gql_list_fields_variable)
    ls = navAbilityClient.query(
        QueryOptions(
            gql(query),
            {
                "userId": client.userId,
                "robotId": client.robotId,
                "sessionId": client.sessionId,
                "labelExact": label,
            },
        )
    )
    # TODO: Check for errors
    if len(ls['VARIABLE']) == 0:
        raise Exception(f"No variable {label} found")
    if len(ls['VARIABLE']) > 1:
        raise Exception(f"More than one variable named {label} returned")

    return Variable.load(ls['VARIABLE'][0])
