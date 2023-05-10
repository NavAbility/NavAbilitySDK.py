import string
import random
import numpy as np
from navability.entities import DFGClient, VariableType, PriorPose2, FullNormal
from navability.services import addVariable, ls, addFactor, lsf


def test_add_variable_factor():
    userLabel = "guest@navability.io"
    robotLabel = "TestRobot"
    sessionLabel = 'TestPy'
    fgclient = DFGClient(userLabel, robotLabel, sessionLabel)
    #TODO SDK.py cannot create sessions yet, so adding random variables existing session
    vlabel = 'x_'+''.join(random.choices(string.ascii_letters + string.digits, k=4))
    v = addVariable(fgclient, vlabel, VariableType.Pose2)
    f = addFactor(fgclient, [vlabel], PriorPose2(Z=FullNormal([1.0,1.0,0.0], np.diag([0.1,0.1,0.1]))))
    assert v.label == vlabel and f['label'][0 : 6] == vlabel #FIXME f.label[0 : 6] == vlabel
