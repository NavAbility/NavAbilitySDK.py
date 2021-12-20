from typing import List
from datetime import datetime
from pprint import pprint
from marshmallow import Schema, fields, INCLUDE


class PPESchema(Schema):
    solveKey = fields.Str(required=True)
    suggested = fields.List(fields.Float(), required=True)
    max = fields.List(fields.Float(), required=True)
    mean = fields.List(fields.Float(), required=True)
    lastUpdatedTimestamp = fields.Method("get_lastupdated", required=True)

    class Meta:
        ordered = True

    def get_lastupdated(self, obj):
        # Return a robust timestamp
        ts = obj.lastUpdatedTimestamp.isoformat(timespec="milliseconds")
        if not obj.lastUpdatedTimestamp.tzinfo:
            ts += "+00"
        return ts


class PPE:
    schema: PPESchema = PPESchema()

    def __init__(
        self,
        solveKey: str = "default",
        suggested: List[float] = [0, 0, 0],
        max: List[float] = [0, 0, 0],
        mean: List[float] = [0, 0, 0],
        lastUpdatedTimestamp: datetime = datetime.utcnow(),
    ):
        self.solveKey = solveKey
        self.suggested = suggested
        self.max = max
        self.mean = mean
        self.lastUpdatedTimestamp = lastUpdatedTimestamp

    def __repr__(self):
        return f"<PPE(solveKey={self.solveKey}, suggested={self.suggested})>"

    def dump(self):
        return PPE.schema.dump(self)

    def dumps(self):
        return PPE.schema.dumps(self)
