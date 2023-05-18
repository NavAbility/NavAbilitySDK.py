import random
import string
from navability.entities.navabilityclient import NavAbilityHttpsClient
from navability.services import addSession


def test_addSession():
    client = NavAbilityHttpsClient()
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = "Test_addSession_" + "".join(
        random.choices(string.ascii_letters + string.digits, k=4)
    )
    session = addSession(client, userLabel, robotLabel, sessionLabel)
    assert session.label == sessionLabel
