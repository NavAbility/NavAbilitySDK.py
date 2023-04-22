from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from typing import Optional
from marshmallow import Schema, fields, post_load

# Define a dataclass for Robot
@dataclass
class Robot:
    id: UUID
    label: str
    _version: str
    userLabel: str
    userId: Optional[UUID]
    metadata: Optional[str]
    createdTimestamp: datetime
    lastUpdatedTimestamp: datetime

    # Add sessions, blobEntries & user? [Alucard]

# Define a Marshmallow schema for Robot
class RobotSchema(Schema):
    # Define the required fields and their types
    id = fields.UUID(required=True)
    label = fields.String(required=True)
    _version = fields.String(required=True)
    userLabel = fields.String(required=True)
    userId = fields.UUID(allow_none=True)
    metadata = fields.String(allow_none=True)
    createdTimestamp = fields.DateTime(required=True)
    lastUpdatedTimestamp = fields.DateTime(required=True)

    # Define a method to create a Robot object from deserialized data
    @post_load
    def make_robot(self, data, **kwargs):
        return Robot(**data)

