from typing import List
from datetime import datetime
from pprint import pprint
import numpy
import json

schema = DFGVariableSchema()
a = DFGVariable("x0", "Pose2")
packed = schema.dumps(a)
# PackedVariable
{
    "label": "x0",
    "dataEntry": "{}",
    "nstime": "0",
    "dataEntryType": "{}",
    "ppeDict": "{}",
    "solverDataDict": '{"default":{"vecval":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],"dimval":3,"vecbw":[0.0,0.0,0.0],"dimbw":3,"BayesNetOutVertIDs":[],"dimIDs":[0,1,2],"dims":3,"eliminated":false,"BayesNetVertID":"_null","separator":[],"variableType":"RoME.Pose2","initialized":false,"infoPerCoord":[0.0,0.0,0.0],"ismargin":false,"dontmargin":false,"solveInProgress":0,"solvedCount":0,"solveKey":"default"}}',
    "smallData": "{}",
    "variableType": "RoME.Pose2",
    "solvable": 1,
    "tags": '["VARIABLE"]',
    "timestamp": "2021-10-30T13:54:44.468-05:00",
    "_version": "0.16.2",
}
f = open("/tmp/variablePy.txt", mode="w")
f.write(packed)
f.close()

# PackedPrior
{
    "label": "x0f1",
    "_version": "0.16.2",
    "_variableOrderSymbols": '["x0"]',
    "data": '{"eliminated":false,"potentialused":false,"edgeIDs":[],"fnc":{"str":"FullNormal(\\ndim: 3\\nμ: [0.0, 0.0, 0.0]\\nΣ: [0.01 0.0 0.0; 0.0 0.01 0.0; 0.0 0.0 0.01]\\n)\\n"},"multihypo":[],"certainhypo":[1],"nullhypo":0.0,"solveInProgress":0,"inflation":5.0}',
    "tags": '["FACTOR"]',
    "timestamp": "2021-11-08T11:24:53.780-06:00",
    "nstime": "0",
    "fnctype": "PriorPose2",
    "solvable": 1,
}
# PackedFactor
{
    "label": "x0x1f1",
    "_version": "0.16.2",
    "_variableOrderSymbols": '["x0","x1"]',
    "data": '{"eliminated":false,"potentialused":false,"edgeIDs":[],"fnc":{"datastr":"FullNormal(\\ndim: 3\\nμ: [10.0, 0.0, 1.0471975511965976]\\nΣ: [0.010000000000000002 0.0 0.0; 0.0 0.010000000000000002 0.0; 0.0 0.0 0.010000000000000002]\\n)\\n"},"multihypo":[],"certainhypo":[1,2],"nullhypo":0.0,"solveInProgress":0,"inflation":5.0}',
    "tags": '["FACTOR"]',
    "timestamp": "2021-11-08T11:24:57.045-06:00",
    "nstime": "0",
    "fnctype": "Pose2Pose2",
    "solvable": 1,
}

# schema = DFGVariableNodeDataSchema()
# schema.dump(a.solverDataDict["default"])

# def prior(label: str, variable: str, type: str, tags: List[str]):
#   return {
#     "label":label,
#     "_version":"0.16.2",
#     "_variableOrderSymbols":f"[\"{variable}\"]",
#     "data":"{\"eliminated\":false,\"potentialused\":false,\"edgeIDs\":[],\"fnc\":{\"str\":\"FullNormal(\\ndim: 3\\nμ: [0.0, 0.0, 0.0]\\nΣ: [0.01 0.0 0.0; 0.0 0.01 0.0; 0.0 0.0 0.01]\\n)\\n\"},\"multihypo\":[],\"certainhypo\":[1],\"nullhypo\":0.0,\"solveInProgress\":0,\"inflation\":5.0}",
#     "tags":"[\"FACTOR\"]",
#     "timestamp":"2021-10-30T13:54:45.825-05:00",
#     "nstime":"0",
#     "fnctype":"PriorPose2",
#     "solvable":1}


try:
    BandMemberSchema(many=True).load(user_data)
except ValidationError as err:
    pprint(err.messages)


class DFGFactor:
    label: str
    _variableOrderSymbols: str  # TODO
    data: str  # TODO
    tags: str  # TODO
    timestamp: str
    nstime: str
    fnctype: str
    solvable: int  # Need an int
    _version: str

    def __init__(
        self,
        label: str,
        fncType: str,
        variableOrderSymbols: List[str],
        tags: str = List[str],
        # Why is this datastr and the prior is str?
        func: str = '{"datastr":"FullNormal(\\ndim: 3\\nμ: [10.0, 0.0, 0.0]\\nΣ: [0.010000000000000002 0.0 0.0; 0.0 0.010000000000000002 0.0; 0.0 0.0 0.010000000000000002]\\n)\\n"}',
        timestamp: str = datetime.utcnow().isoformat(),
    ):
        self.label = label
        self._variableOrderSymbols = variableOrderSymbols
        self.data = '{"eliminated":false,"potentialused":false,"edgeIDs":[],"fnc": {},"multihypo":[],"certainhypo":[1],"nullhypo":0.0,"solveInProgress":0}'.format(
            func
        )
        self.tags = tags
        self.timestamp = timestamp
        self.nstime = "0"
        self.fnctype = fncType
        self.solvable = 1
        self._version = "0.10.2"


class DFGFactorPrior(DFGFactor):
    def __init__(
        self,
        label: str,
        fncType: str,
        variableOrderSymbols: List[str],
        tags: str = List[str],
        # Why is this datastr and the prior is str?
        func: str = '{"str":"FullNormal(\\ndim: 3\\nμ: [0.0, 0.0, 0.0]\\nΣ: [0.01 0.0 0.0; 0.0 0.01 0.0; 0.0 0.0 0.01]\\n)\\n"}',
        timestamp: str = datetime.utcnow().isoformat(),
    ):
        super().__init__(label, fncType, variableOrderSymbols, tags, func, timestamp)


# export class DFGFactorPrior extends DFGFactor {
#   constructor(label: string,
#   fncType: string,
#   variableOrderSymbols: string,
#   tags: string = "[\"FACTOR\"]",
#   func: string = "{\"str\":\"FullNormal(\\ndim: 3\\nμ: [0.0, 0.0, 0.0]\\nΣ: [0.01 0.0 0.0; 0.0 0.01 0.0; 0.0 0.0 0.01]\\n)\\n\"}",
#   timestamp: string = new Date().toISOString()) {
#     super(label, fncType, variableOrderSymbols, tags, func, timestamp);
#   }
# }

# PackedVariable
{
    "label": "x0",
    "dataEntry": "{}",
    "nstime": "0",
    "dataEntryType": "{}",
    "ppeDict": "{}",
    "solverDataDict": '{"default":{"vecval":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],"dimval":3,"vecbw":[0.0,0.0,0.0],"dimbw":3,"BayesNetOutVertIDs":[],"dimIDs":[0,1,2],"dims":3,"eliminated":false,"BayesNetVertID":"_null","separator":[],"variableType":"RoME.Pose2","initialized":false,"infoPerCoord":[0.0,0.0,0.0],"ismargin":false,"dontmargin":false,"solveInProgress":0,"solvedCount":0,"solveKey":"default"}}',
    "smallData": "{}",
    "variableType": "RoME.Pose2",
    "solvable": 1,
    "tags": '["VARIABLE"]',
    "timestamp": "2021-10-30T13:54:44.468-05:00",
    "_version": "0.16.2",
}
# PackedPrior
{
    "label": "x0f1",
    "_version": "0.16.2",
    "_variableOrderSymbols": '["x0"]',
    "data": '{"eliminated":false,"potentialused":false,"edgeIDs":[],"fnc":{"str":"FullNormal(\\ndim: 3\\nμ: [0.0, 0.0, 0.0]\\nΣ: [0.01 0.0 0.0; 0.0 0.01 0.0; 0.0 0.0 0.01]\\n)\\n"},"multihypo":[],"certainhypo":[1],"nullhypo":0.0,"solveInProgress":0,"inflation":5.0}',
    "tags": '["FACTOR"]',
    "timestamp": "2021-11-08T11:24:53.780-06:00",
    "nstime": "0",
    "fnctype": "PriorPose2",
    "solvable": 1,
}
# PackedFactor
{
    "label": "x0x1f1",
    "_version": "0.16.2",
    "_variableOrderSymbols": '["x0","x1"]',
    "data": '{"eliminated":false,"potentialused":false,"edgeIDs":[],"fnc":{"datastr":"FullNormal(\\ndim: 3\\nμ: [10.0, 0.0, 1.0471975511965976]\\nΣ: [0.010000000000000002 0.0 0.0; 0.0 0.010000000000000002 0.0; 0.0 0.0 0.010000000000000002]\\n)\\n"},"multihypo":[],"certainhypo":[1,2],"nullhypo":0.0,"solveInProgress":0,"inflation":5.0}',
    "tags": '["FACTOR"]',
    "timestamp": "2021-11-08T11:24:57.045-06:00",
    "nstime": "0",
    "fnctype": "Pose2Pose2",
    "solvable": 1,
}
