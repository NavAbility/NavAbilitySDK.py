import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from marshmallow import Schema, fields, post_load, EXCLUDE

from navability.common.versions import payload_version
from navability.entities.Factor.inferencetypes import InferenceType


@dataclass()
class FactorData:
    fnc: InferenceType #{"datastr":"FullNormal(\\ndim: 3\\nμ: [10.0, 0.0, 1.0471975511965976]\\nΣ: [0.010000000000000002 0.0 0.0; 0.0 0.010000000000000002 0.0; 0.0 0.0 0.010000000000000002]\\n)\\n"}
    eliminated: bool = False
    potentialused: bool = False
    edgeIDs: List[int] = field(default_factory=lambda: [])
    multihypo: List[int] = field(default_factory=lambda: [])
    certainhypo: List[int] = field(default_factory=lambda: [1,2])
    nullhypo: float = 0
    solveInProgress: int = 0
    inflation: float = 5

    def dumps(self):
        return FactorDataSchema().dumps(self)

class FactorDataSchema(Schema):
    fnc = fields.Method("get_fnc", "set_fnc", required=True)
    eliminated = fields.Bool(required=True)
    edgeIDs = fields.List(fields.Int(), required=True)
    multihypo = fields.List(fields.Int(), required=True)
    certainhypo = fields.List(fields.Int(), required=True)
    nullhypo = fields.Float(required=True)
    solveInProgress = fields.Int(required=True)
    inflation = fields.Float(required=True)

    class Meta:
        ordered = True

    def get_fnc(self, obj):
        # TODO: Switch this out to a real embedded object, no need for strings.
        return obj.fnc.dumps()

    def set_fnc(self, ob):
        raise Exception("Deserialization not supported yet.")

    @post_load
    def load(self, data, **kwargs):
        return FactorData(**data)


@dataclass()
class Factor:
    label: str
    fnctype: str
    data: FactorData #'{"eliminated":false,"potentialused":false,"edgeIDs":[],"fnc":{"datastr":"FullNormal(\\ndim: 3\\nμ: [10.0, 0.0, 1.0471975511965976]\\nΣ: [0.010000000000000002 0.0 0.0; 0.0 0.010000000000000002 0.0; 0.0 0.0 0.010000000000000002]\\n)\\n"},"multihypo":[],"certainhypo":[1,2],"nullhypo":0.0,"solveInProgress":0,"inflation":5.0}'  # noqa: E501, B950
    variableOrderSymbols: List[str]
    tags: List[str] = field(default_factory=lambda: ["FACTOR"])
    timestamp: str = datetime.utcnow()
    # nstime: str = "0"
    solvable: str = 1
    _version: str = payload_version

    def __init__(self, label:str, data:FactorData, variableOrderSymbols: List[str], fnctype:str=None):
        self.label = label
        self.data = data
        self.variableOrderSymbols = variableOrderSymbols
        if fnctype is None:
            self.fnctype=data.fnc.__class__.__name__
        
    def __repr__(self):
        return f"<{self.__class__.__name__}(label={self.label}), variables={self.variableOrderSymbols}>"

    def dump(self):
        return FactorSchema().dump(self)

    def dumps(self):
        return FactorSchema().dumps(self)


# @dataclass()
# class FactorPrior(Factor):
#     data: str = '{"eliminated":false,"potentialused":false,"edgeIDs":[],"fnc":{"datastr":"FullNormal(\\ndim: 3\\nμ: [10.0, 0.0, 1.0471975511965976]\\nΣ: [0.010000000000000002 0.0 0.0; 0.0 0.010000000000000002 0.0; 0.0 0.0 0.010000000000000002]\\n)\\n"},"multihypo":[],"certainhypo":[1,2],"nullhypo":0.0,"solveInProgress":0,"inflation":5.0}'  # noqa: E501, B950


class FactorSchema(Schema):
    label = fields.Str(required=True)
    _variableOrderSymbols = fields.Method("get_variableOrderSymbols", required=True)
    data = fields.Method("get_data", "set_data", required=True)
    tags = fields.List(fields.Str(), required=True)
    timestamp = fields.Method("get_timestamp", "set_timestamp", required=True)
    nstime = fields.Str(required=True)
    fnctype = fields.Str(required=True)
    solvable = fields.Int(required=True)
    _version = fields.Str(required=True)

    class Meta:
        ordered = True
        unknown = EXCLUDE  # Note: This is because of _version, remote and fix later.

    def get_variableOrderSymbols(self, obj):
        # TODO: Switch this out to a real embedded object, no need for strings.
        return json.dumps(obj.variableOrderSymbols)

    def get_timestamp(self, obj):
        # Return a robust timestamp
        ts = obj.timestamp.isoformat(timespec="milliseconds")
        if not obj.timestamp.tzinfo:
            ts += "+00"
        return ts

    def set_timestamp(self, obj):
        return datetime.strptime(obj["formatted"], TS_FORMAT)

    def get_data(self, obj):
        return obj.data.dumps()

    def set_data(self, ob):
        raise Exception("Deserialization not supported yet.")

    @post_load
    def load(self, data, **kwargs):
        return Factor(**data)
