from gql import gql

from navability.common.mutations import GQL_SOLVESESSION
from navability.entities.Client import Client
from navability.entities.NavAbilityClient import MutationOptions, NavAbilityClient


def solveSession(navAbilityClient: NavAbilityClient, client: Client):
    return navAbilityClient.mutate(
        MutationOptions(gql(GQL_SOLVESESSION), {"client": client.dump()})
    )
