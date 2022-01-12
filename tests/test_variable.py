from navability.entities.navabilityclient import NavAbilityClient
from navability.services.variable import getVariable, ls


def test_sample(navability_https_client: NavAbilityClient):
    pass


def test_ls(example_graph):
    navability_client, client, variables, factors = example_graph
    assert set([l.label for l in ls(navability_client, client)]) == set(
        [v.label for v in variables]
    )


def test_getVariable(example_graph):
    navability_client, client, variables, factors = example_graph
    assert (
        getVariable(navability_client, client, variables[0].label).label
        == variables[0].label
    )
