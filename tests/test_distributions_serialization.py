from navability.entities import Categorical, FullNormal, Normal, Uniform


def test_normal():
    dist = Normal(0.0, 23.0)
    assert (
        dist.dumps()
        == '{"_type": "IncrementalInference.PackedNormal", "mu": 0.0, "sigma": 23.0}'
    )


def test_distribution_fullnormal():
    norm = FullNormal()
    assert (
        norm.dumps()
        == '{"_type": "IncrementalInference.PackedFullNormal", "mu": [0.0, 0.0, 0.0], "cov": [0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1]}'  # noqa: E501, B950
    )
    # TODO: Implement and test deserialization/marshalling
    # fnret = FullNormal.load(dumped)
    # assert fnret == norm


def test_categorical():
    dist = Categorical([0.4, 0.6])
    assert (
        dist.dumps()
        == '{"_type": "IncrementalInference.PackedCategorical", "p": [0.4, 0.6]}'
    )


def test_uniform():
    dist = Uniform(a=30.0, b=55.0)
    assert (
        dist.dumps()
        == '{"_type": "IncrementalInference.PackedUniform", "a": 30.0, "b": 55.0, "PackedSamplableTypeJSON": "IncrementalInference.PackedUniform"}'  # noqa: E501, B950
    )
