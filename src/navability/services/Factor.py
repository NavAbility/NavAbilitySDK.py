from gql import gql

from navability.entities.Factor import Factor
from navability.entities.Client import Client
from navability.common.queries import (
    gql_addFactor,
)
from navability.entities.NavAbilityClient import (
    NavAbilityClient,
    MutationOptions,
)


def addFactor(navAbilityClient: NavAbilityClient, client: Client, f: Factor):
    return navAbilityClient.mutate(
        MutationOptions(
            gql(gql_addFactor),
            {
                "factor": {
                    "client": client.dump(),
                    "packedData": f.dumps(),
                }
            },
        )
    )
