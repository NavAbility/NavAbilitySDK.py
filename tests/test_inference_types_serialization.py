from collections import OrderedDict

import numpy as np

from navability.entities import (
    FullNormal,
    Mixture,
    Normal,
    Pose2AprilTag4Corners,
    Pose2Pose2,
    Prior,
    PriorPose2,
    Uniform,
)
from src.navability.entities.factor.inferencetypes import LinearRelative


def test_prior():
    pose = Prior(Z=Normal(0, 2))
    dumped = pose.dumps()
    assert (
        dumped
        == '{"Z": {"_type": "IncrementalInference.PackedNormal", "mu": 0.0, "sigma": 2.0}}'  # noqa: E501, B950
    )


def test_priorpose2():
    pose = PriorPose2(
        Z=FullNormal(mu=np.asarray([0.0, 0.1, 0.2]), cov=np.diag([0.2, 0.3, 0.4]))
    )
    dumped = pose.dumps()
    assert (
        dumped
        == '{"Z": {"_type": "IncrementalInference.PackedFullNormal", "mu": [0.0, 0.1, 0.2], "cov": [0.2, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.4]}}'  # noqa: E501, B950
    )
    # TODO: Implement and test deserialization/marshalling


def test_pose2pose2():
    pose = Pose2Pose2(
        Z=FullNormal(mu=np.array([0.0, 0.1, 0.2]), cov=np.diag([0.2, 0.3, 0.4]))
    )
    dumped = pose.dumps()
    assert (
        dumped
        == '{"Z": {"_type": "IncrementalInference.PackedFullNormal", "mu": [0.0, 0.1, 0.2], "cov": [0.2, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.4]}}'  # noqa: E501, B950
    )
    # TODO: Implement and test deserialization/marshalling


def test_pose2apriltag4corners():
    pose = Pose2AprilTag4Corners(
        corners=np.zeros(8),
        homography=np.zeros(9),
        K=[300.0, 0.0, 0.0, 0.0, 300.0, 0.0, 180.0, 120.0, 1.0],
        taglength=0.25,
        id=1,
    )
    dumped = pose.dumps()
    assert (
        dumped
        == '{"corners": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "homography": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "K": [300.0, 0.0, 0.0, 0.0, 300.0, 0.0, 180.0, 120.0, 1.0], "taglength": 0.25, "id": 1, "_type": "/application/JuliaLang/PackedPose2AprilTag4Corners"}'  # noqa: E501, B950
    )
    # TODO: Implement and test deserialization/marshalling


def test_mixture():
    pose = Mixture(
        LinearRelative,
        OrderedDict([("hypo1", Normal(0, 2)), ("hypo2", Uniform(30, 55))]),
        [0.4, 0.6],
        2,
    )
    dumped = pose.dumps()
    print(dumped)
    assert (
        dumped
        == '{"N": 2, "F_": "PackedLinearRelative", "S": ["hypo1", "hypo2"], "components": [{"_type": "IncrementalInference.PackedNormal", "mu": 0.0, "sigma": 2.0}, {"_type": "IncrementalInference.PackedUniform", "a": 30.0, "b": 55.0, "PackedSamplableTypeJSON": "IncrementalInference.PackedUniform"}], "diversity": {"_type": "IncrementalInference.PackedCategorical", "p": [0.4, 0.6]}}'  # noqa: E501, B950
    )
