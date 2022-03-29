from collections import OrderedDict

import numpy as np

from navability.entities import (
    FullNormal,
    Mixture,
    Normal,
    Point2Point2Range,
    Pose2AprilTag4Corners,
    Pose2Point2BearingRange,
    Pose2Point2Range,
    Pose2Pose2,
    Prior,
    PriorPoint2,
    PriorPose2,
    Uniform,
)
from src.navability.entities.factor.inferencetypes import LinearRelative


def test_prior():
    pose = Prior(Normal(0, 2))
    dumped = pose.dumps()
    assert (
        dumped
        == '{"Z": {"_type": "IncrementalInference.PackedNormal", "mu": 0.0, "sigma": 2.0}}'  # noqa: E501, B950
    )


def test_priorpose2():
    pose = PriorPose2(
        FullNormal(mu=np.asarray([0.0, 0.1, 0.2]), cov=np.diag([0.2, 0.3, 0.4]))
    )
    dumped = pose.dumps()
    assert (
        dumped
        == '{"Z": {"_type": "IncrementalInference.PackedFullNormal", "mu": [0.0, 0.1, 0.2], "cov": [0.2, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.4]}}'  # noqa: E501, B950
    )
    # TODO: Implement and test deserialization/marshalling


def test_pose2pose2():
    pose = Pose2Pose2(
        FullNormal(mu=np.array([0.0, 0.1, 0.2]), cov=np.diag([0.2, 0.3, 0.4]))
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
    assert (
        dumped
        == '{"N": 2, "F_": "PackedLinearRelative", "S": ["hypo1", "hypo2"], "components": [{"_type": "IncrementalInference.PackedNormal", "mu": 0.0, "sigma": 2.0}, {"_type": "IncrementalInference.PackedUniform", "a": 30.0, "b": 55.0, "PackedSamplableTypeJSON": "IncrementalInference.PackedUniform"}], "diversity": {"_type": "IncrementalInference.PackedCategorical", "p": [0.4, 0.6]}}'  # noqa: E501, B950
    )


def test_priorpoint2():
    pose = PriorPoint2(FullNormal(np.asarray([0.0, 0.1]), cov=np.diag([0.2, 0.3])))
    dumped = pose.dumps()
    assert (
        dumped
        == '{"Z": {"_type": "IncrementalInference.PackedFullNormal", "mu": [0.0, 0.1], "cov": [0.2, 0.0, 0.0, 0.3]}}'  # noqa: E501, B950
    )
    pass


def test_point2point2range():
    pose = Point2Point2Range(Normal(89.44271909999159, 3))
    dumped = pose.dumps()
    assert (
        dumped
        == '{"Z": {"_type": "IncrementalInference.PackedNormal", "mu": 89.44271909999159, "sigma": 3.0}}'  # noqa: E501, B950
    )
    pass


def test_pose2point2range():
    pose = Pose2Point2Range(Normal(89.44271909999159, 3))
    dumped = pose.dumps()
    assert (
        dumped
        == '{"Z": {"_type": "IncrementalInference.PackedNormal", "mu": 89.44271909999159, "sigma": 3.0}}'  # noqa: E501, B950
    )
    pass


def test_pose2point2bearingrange():
    pose = Pose2Point2BearingRange(Normal(0, 0.03), Normal(0.5, 0.1))
    dumped = pose.dumps()
    assert (
        dumped
        == '{"bearstr": {"_type": "IncrementalInference.PackedNormal", "mu": 0.0, "sigma": 0.03}, "rangstr": {"_type": "IncrementalInference.PackedNormal", "mu": 0.5, "sigma": 0.1}}'  # noqa: E501, B950
    )
    pass
