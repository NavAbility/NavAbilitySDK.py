from navability.entities import Client
from navability.services import lsf  # getFactor


def test_lsf(example_graph):
    navability_client, client, variables, factors = example_graph
    assert set(lsf(navability_client, client)) == set([f.label for f in factors])


def test_lsf_no_session(example_graph):
    navability_client, client, variables, factors = example_graph
    noSessionClient = Client(client.userId, client.robotId, "DoesntExist")
    assert lsf(navability_client, noSessionClient) == []


# def test_getFactor(example_graph):
#     navability_client, client, variables, factors = example_graph
#     assert (
#         getFactor(navability_client, client, factors[0].label).label
#         == variables[0].label
#     )
