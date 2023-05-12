from navability.entities import DFGClient
from navability.services import listNeighbors


def test_hex_listNeighbors_var():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    assert set(listNeighbors(fgclient, 'x0')) == set(['x0f1', 'x0x1f1', 'x0l1f1'])


def test_hex_listNeighbors_fac():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    assert set(listNeighbors(fgclient, 'x0x1f1')) == set(['x0', 'x1'])
