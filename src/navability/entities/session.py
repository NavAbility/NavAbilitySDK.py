from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from typing import List, Optional
from marshmallow import Schema, fields, post_load

from navability.entities.blob.blobentry import ( BlobEntrySchema, BlobEntry )

# Define a dataclass for Session
@dataclass
class Session:
    id: UUID
    label: str
    _version: str
    userLabel: str
    robotLabel: str
    robotId: Optional[UUID]
    userId: Optional[UUID]
    # numVariables: Optional[int]
    # numFactors: Optional[int]
    # solveKeys: Optional[List[str]] # ??? Why list no work [Alucard]
    metadata: Optional[str]
    originLatitude: Optional[float]
    originLongitude: Optional[float]
    createdTimestamp: datetime
    lastUpdatedTimestamp: datetime
    blobEntries: List[BlobEntry]

    # TODO
    # This is added? [Alucard]
    # Session-specific origin in lat_lon (optional)
    # originLatitude: Latitude
    # originLongitude: Longitude
    # userLabel: String!
    # robotLabel: String!



# Define a Marshmallow schema for Session
class SessionSchema(Schema):
    # Define the required fields and their types
    id = fields.UUID(required=True)
    label = fields.String(required=True)
    _version = fields.String(required=True)
    userLabel = fields.String(required=True)
    robotLabel = fields.String(required=True)
    robotId = fields.UUID(allow_none=True)
    userId = fields.UUID(allow_none=True)
    # numVariables = fields.Integer(allow_none=True)
    # numFactors = fields.Integer(allow_none=True)
    # solveKeys = fields.List(fields.String(), allow_none=True)
    metadata = fields.String(allow_none=True)
    originLatitude = fields.Float(allow_none=True)
    originLongitude = fields.Float(allow_none=True)
    createdTimestamp = fields.DateTime(required=True)
    lastUpdatedTimestamp = fields.DateTime(required=True)
    blobEntries = fields.Nested(BlobEntrySchema, many=True)


    # Define a method to create a Session object from deserialized data
    @post_load
    def make_session(self, data, **kwargs):
        return Session(**data)