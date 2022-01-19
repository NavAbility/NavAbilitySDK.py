from navability.services.variable import getVariable, ls


def test_ls(example_graph):
    navability_client, client, variables, factors = example_graph
    assert set(ls(navability_client, client)) == set([v.label for v in variables])


def test_ls_no_session(example_graph):
    navability_client, client, variables, factors = example_graph
    client.sessionId = "Doesntexist"
    assert ls(navability_client, client) == []


def test_getVariable(example_graph):
    navability_client, client, variables, factors = example_graph
    assert (
        getVariable(navability_client, client, variables[0].label).label
        == variables[0].label
    )
