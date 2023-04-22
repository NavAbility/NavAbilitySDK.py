from dataclasses import dataclass
from uuid import UUID
from typing import List
from marshmallow import Schema, fields, post_load

# Define a dataclass for Annotation
@dataclass
class Annotation:
    id = UUID
    text: str
    position: List[float]

# Define a Marshmallow schema for Annotation
class AnnotationSchema(Schema):
    # Define the required fields and their types
    id = fields.UUID(required=True)
    text = fields.String(required=True)
    position = fields.List(fields.Float(), required=True)

    # Define a method to create a Annotation object from deserialized data
    @post_load
    def make_annotation(self, data, **kwargs):
        return Annotation(**data)