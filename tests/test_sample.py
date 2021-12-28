from navability.entities.NavAbilityClient import NavAbilityWebsocketClient
from navability.services.Variable import getVariable, ls


def test_sample(navability_wss_client: NavAbilityWebsocketClient):
    pass


def test_ls(example_graph):
    navability_client, client, variables, factors = example_graph
    assert set(ls(navability_client, client)) == set([v.label for v in variables])


def test_getVariable(example_graph):
    navability_client, client, variables, factors = example_graph
    assert (
        getVariable(navability_client, client, variables[0].label).label
        == variables[0].label
    )
