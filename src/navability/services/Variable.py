from gql import gql

from navability.entities.Variable import Variable
from navability.entities.Client import Client
from navability.common.queries import (
    gql_addVariable,
)
from navability.entities.NavAbilityClient import (
    NavAbilityClient,
    MutationOptions,
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
