from navability.services import lsf


def test_lsf(example_graph):
    navability_client, client, variables, factors = example_graph
    assert set(lsf(navability_client, client)) == set([f.label for f in factors])


# def test_getFactor(example_graph):
#     navability_client, client, variables, factors = example_graph
#     assert (
#         getFactor(navability_client, client, factors[0].label).label
#         == variables[0].label
#     )
