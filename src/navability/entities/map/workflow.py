from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from typing import Optional
from marshmallow import Schema, fields, post_load

# Define a dataclass for Workflow
@dataclass
class Workflow:
    id: UUID
    label: str
    description: Optional[str]
    status: str
    _type: str
    _version: str
    data: Optional[str]
    result: Optional[str]
    createdTimestamp: datetime
    lastUpdatedTimestamp: datetime

# Define a Marshmallow schema for Workflow
class WorkflowSchema(Schema):
    # Define the required fields and their types
    id = fields.UUID(required=True)
    label = fields.String(required=True)
    description = fields.String(allow_none=True)
    status = fields.String(required=True)
    _type = fields.String(required=True)
    _version = fields.String(required=True)
    data = fields.String(allow_none=True)
    result = fields.String(allow_none=True)
    createdTimestamp = fields.DateTime(required=True)
    lastUpdatedTimestamp = fields.DateTime(required=True)

    # Define a method to create a Workflow object from deserialized data
    @post_load
    def make_workflow(self, data, **kwargs):
        return Workflow(**data)