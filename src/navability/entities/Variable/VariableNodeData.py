from typing import List, Dict
from datetime import datetime
from pprint import pprint
from marshmallow import Schema, fields, INCLUDE
import numpy


class VariableNodeDataSchema(Schema):
    vecval = fields.List(fields.Float(), required=True)  # numpy.zeros(3*100) # 300
    dimval = fields.Integer(required=True)  # 3
    vecbw = fields.List(fields.Float(), required=True)  # numpy.zeros(3)
    dimbw = fields.Integer(required=True)  # 3
    BayesNetOutVertIDs = fields.List(fields.Integer(), required=True)  # []
    dimIDs = fields.List(fields.Integer(), required=True)  # [0,1,2]
    dims = fields.Integer(required=True)  # 3
    eliminated = fields.Boolean(required=True)  # False
    BayesNetVertID = fields.Str(required=True)  # "_null"
    separator = fields.List(fields.Integer(), required=True)  # []
    variableType = fields.Str(required=True)  # type
    initialized = fields.Boolean(required=True)  # False
    infoPerCoord = fields.List(fields.Float(), required=True)  # numpy.zeros(3)
    ismargin = fields.Boolean(required=True)  # False
    dontmargin = fields.Boolean(required=True)  # False
    solveInProgress = fields.Integer(required=True)  # 0
    solvedCount = fields.Integer(required=True)  # 0
    solveKey = fields.Str(required=True)  # solveKey

    class Meta:
        ordered = True


class VariableNodeData:
    schema: VariableNodeDataSchema = VariableNodeDataSchema()

    def __init__(self, type: str, solveKey: str = "default"):
        self.vecval = list(numpy.zeros(3 * 100))
        self.dimval = 3
        self.vecbw = list(numpy.zeros(3))
        self.dimbw = 3
        self.BayesNetOutVertIDs = []
        self.dimIDs = [0, 1, 2]
        self.dims = 3
        self.eliminated = False
        self.BayesNetVertID = "_null"
        self.separator = []
        self.variableType = type
        self.initialized = False
        self.infoPerCoord = list(numpy.zeros(3))
        self.ismargin = False
        self.dontmargin = False
        self.solveInProgress = 0
        self.solvedCount = 0
        self.solveKey = solveKey

    def __repr__(self):
        return f"<VariableNodeData(solveKey={self.solveKey})>"

    def dump(self):
        return VariableNodeData.schema.dump(self)

    def dumps(self):
        return VariableNodeData.schema.dumps(self)
