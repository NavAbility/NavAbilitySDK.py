import numpy as np

from navability.entities import (
    FullNormal,
    Pose2AprilTag4Corners,
    Pose2Pose2,
    PriorPose2,
)


def test_distribution_fullnormal():
    norm = FullNormal()
    dumped = norm.dumps()
    assert (
        dumped
        == '{"_type": "IncrementalInference.PackedFullNormal", "mu": [0.0, 0.0, 0.0], "cov": [0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1]}'  # noqa: E501, B950
    )
    # TODO: Implement and test deserialization/marshalling
    # fnret = FullNormal.load(dumped)
    # assert fnret == norm


def test_factor_priorpose2():
    pose = PriorPose2(
        Z=FullNormal(mu=np.asarray([0.0, 0.1, 0.2]), cov=np.diag([0.2, 0.3, 0.4]))
    )
    dumped = pose.dumps()
    assert (
        dumped
        == '{"Z": {"_type": "IncrementalInference.PackedFullNormal", "mu": [0.0, 0.1, 0.2], "cov": [0.2, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.4]}}'  # noqa: E501, B950
    )
    # TODO: Implement and test deserialization/marshalling


def test_factor_pose2pose2():
    pose = Pose2Pose2(
        Z=FullNormal(mu=np.array([0.0, 0.1, 0.2]), cov=np.diag([0.2, 0.3, 0.4]))
    )
    dumped = pose.dumps()
    assert (
        dumped
        == '{"Z": {"_type": "IncrementalInference.PackedFullNormal", "mu": [0.0, 0.1, 0.2], "cov": [0.2, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.4]}}'  # noqa: E501, B950
    )
    # TODO: Implement and test deserialization/marshalling


def test_factor_pose2apriltag4corners():
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
