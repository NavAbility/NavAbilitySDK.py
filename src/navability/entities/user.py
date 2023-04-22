from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from typing import List, Optional
from marshmallow import Schema, fields, post_load

# Define a dataclass for User
@dataclass
class User:
    id: UUID
    sub: str
    givenName: str
    familyName: str
    status: str
    _version: str
    permissions: List[str]
    label: str
    metadata: Optional[str]
    createdTimestamp: datetime
    lastUpdatedTimestamp: datetime
    lastAuthenticatedTimestamp: Optional[datetime]

# Define a Marshmallow schema for User
class UserSchema(Schema):
    # Define the required fields and their types
    id = fields.UUID(required=True)
    sub = fields.String(required=True)
    givenName = fields.String(required=True)
    familyName = fields.String(required=True)
    status = fields.String(required=True)
    _version = fields.String(required=True)
    permissions = fields.List(fields.String(), required=True)
    label = fields.String(required=True)
    metadata = fields.String(allow_none=True)
    createdTimestamp = fields.DateTime(required=True)
    lastUpdatedTimestamp = fields.DateTime(required=True)
    lastAuthenticatedTimestamp = fields.DateTime(allow_none=True)

    # Define a method to create a User object from deserialized data
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)