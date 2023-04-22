from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from typing import Optional, List
from marshmallow import Schema, fields, post_load
from navability.entities.map.workflow import ( Workflow, WorkflowSchema )
from navability.entities.session import Session

# Define a dataclass for Map
@dataclass
class Map:
    id: UUID
    label: str
    description: Optional[str]
    status: str
    data: str
    thumbnailId: Optional[UUID]
    exportedMapId: Optional[UUID]
    workflows: List[Workflow]
    sessions: List[Session]
    createdTimestamp: datetime
    lastUpdatedTimestamp: datetime

# Define a Marshmallow schema for VisualizationBlob
class MapSchema(Schema):
    # Define the required fields and their types
    id = fields.UUID(required=True)
    label = fields.String(required=True)
    description = fields.String(allow_none=True)
    status = fields.String(required=True)
    data = fields.String(allow_none=True)
    result = fields.String(allow_none=True)
    createdTimestamp = fields.DateTime(required=True)
    lastUpdatedTimestamp = fields.DateTime(required=True)

    # Define a method to create a VisualizationBlob object from deserialized data
    @post_load
    def make_map(self, data, **kwargs):
        return Map(**data)