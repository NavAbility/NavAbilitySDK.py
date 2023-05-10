from navability.entities import DFGClient
from navability.services import listBlobEntries, getBlobEntry
from navability.services import getBlob, NavAbilityBlobStore


def test_hex_listBlobEntries():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    assert 'key1' in listBlobEntries(fgclient, 'x1')


def test_hex_getBlobEntry():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    entry = getBlobEntry(fgclient, 'x1', 'key1')
    assert entry.label == 'key1'


# "ffd789e8-480a-4c38-8b84-2081b661e592"
# "example-blob.json"
# "20"
def test_hex_getBlob():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "TestHex"
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    store = NavAbilityBlobStore(fgclient.client, userLabel)
    blob = getBlob(store, "ffd789e8-480a-4c38-8b84-2081b661e592")
    assert len(blob) == 20
