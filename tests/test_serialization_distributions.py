from navability.entities.factor.distributions import FullNormal


def test_fullnormal():
    norm = FullNormal()
    dumped = norm.dumpsPacked()
    assert (
        dumped
        == "FullNormal(\ndim: 3\nμ: [0.0, 0.0, 0.0]\nΣ: [0.1 0.0 0.0;0.0 0.1 0.0;0.0 0.0 0.1]\n)\n"  # noqa: E501, B950
    )
    # This functionality isn't used yet
    fnret = FullNormal.load(dumped)
    assert fnret == norm
