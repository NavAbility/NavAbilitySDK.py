import numpy as np

from navability.entities import (
    FullNormal,
    Pose2AprilTag4Corners,
    Pose2Pose2,
    PriorPose2,
)


def test_distribution_fullnormal():
    norm = FullNormal()
    dumped = norm.dumpsPacked()
    assert (
        dumped
        == "FullNormal(\ndim: 3\nμ: [0.0, 0.0, 0.0]\nΣ: [0.1 0.0 0.0;0.0 0.1 0.0;0.0 0.0 0.1]\n)\n"  # noqa: E501, B950
    )
    # This functionality isn't used yet
    fnret = FullNormal.load(dumped)
    assert fnret == norm


def test_factor_priorpose2():
    pose = PriorPose2(
        z=FullNormal(
            mean=np.asarray([0.0, 0.1, 0.2]), covariance=np.diag([0.2, 0.3, 0.4])
        )
    )
    dumped = pose.dumps()
    assert (
        dumped
        == '{"str": "FullNormal(\\ndim: 3\\n\\u03bc: [0.0, 0.1, 0.2]\\n\\u03a3: [0.2 0.0 0.0;0.0 0.3 0.0;0.0 0.0 0.4]\\n)\\n"}'  # noqa: E501, B950
    )
    # TODO: Implement and test deserialization/marshalling


def test_factor_pose2pose2():
    pose = Pose2Pose2(
        z=FullNormal(
            mean=np.array([0.0, 0.1, 0.2]), covariance=np.diag([0.2, 0.3, 0.4])
        )
    )
    dumped = pose.dumps()
    assert (
        dumped
        == '{"datastr": "FullNormal(\\ndim: 3\\n\\u03bc: [0.0, 0.1, 0.2]\\n\\u03a3: [0.2 0.0 0.0;0.0 0.3 0.0;0.0 0.0 0.4]\\n)\\n"}'  # noqa: E501, B950
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
        == '{"corners": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "homography": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "K": [300.0, 0.0, 0.0, 0.0, 300.0, 0.0, 180.0, 120.0, 1.0], "taglength": 0.25, "id": 1, "mimeType": "/application/JuliaLang/PackedPose2AprilTag4Corners"}'  # noqa: E501, B950
    )
    # TODO: Implement and test deserialization/marshalling
