import asyncio

import pytest

from navability.entities import DFGClient
from navability.services.graph import listNeighbors


def test_hex_listNeighbors():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    assert set(listNeighbors(fgclient, 'x0')) == set(['x0f1', 'x0x1f1'])