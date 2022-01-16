from navability.services import getVariable

def test_solveSession(example_graph_solved):
    navability_client, client, variables, factors = example_graph_solved
    v = getVariable(navability_client, client, variables[0].label)
    assert 'default' in v.ppes
    assert v.ppes['default'].solveKey == 'default'
    assert len(v.ppes['default'].suggested) == 3
