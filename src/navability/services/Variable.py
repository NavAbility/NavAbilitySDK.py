from typing import List
from gql import gql

from src.navability.entities.Variable.Variable import Variable
from navability.entities.Client import Client
from navability.common.queries import (
    gql_addVariable,
    gql_list,
    gql_list_fields_default,
    gql_list_fields_variable,
    gql_list_fields_variable_summary,
    gql_list_fields_variable_skeleton,
)
from navability.entities.NavAbilityClient import (
    NavAbilityClient,
    MutationOptions,
    QueryOptions,
)


def addVariable(navAbilityClient: NavAbilityClient, client: Client, v: Variable):
    return navAbilityClient.mutate(
        MutationOptions(
            gql(gql_addVariable),
            {
                "variable": {
                    "client": client.dump(),
                    "packedData": v.dumps(),
                }
            },
        )
    )


def ls(
    navAbilityClient: NavAbilityClient,
    client: Client,
    regexFilter: str = None,
    tags: List[str] = None,
    solvable: int = 0,
    fields: str = gql_list_fields_default,
):
    ls = navAbilityClient.query(
        QueryOptions(
            gql(gql_list.replace("__TYPE__", "VARIABLE").replace("__FIELDS__", fields)),
            {
                "userId": client.userId,
                "robotId": client.robotId,
                "sessionId": client.sessionId,
                "regexFilter": regexFilter,
                "tags": tags,
                "solvable": solvable,
            },
        )
    )
    # TODO: Check for errors
    return ls["list"]


def getVariable(navAbilityClient: NavAbilityClient, client: Client, label: str):
    ls = navAbilityClient.query(
        QueryOptions(
            gql(
                gql_list.replace("__TYPE__", "VARIABLE").replace(
                    "__FIELDS__", gql_list_fields_variable
                )
            ),
            {
                "userId": client.userId,
                "robotId": client.robotId,
                "sessionId": client.sessionId,
                "regexFilter": label,
            },
        )
    )
    # TODO: Check for errors

    return ls["list"]
