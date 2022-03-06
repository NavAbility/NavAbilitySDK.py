from dataclasses import dataclass, field

import numpy
from marshmallow import EXCLUDE, Schema, fields, post_load


class Distribution:
    """
    Base type for all distribution classes.
    """

    pass

    def dumpsPacked(self):
        raise Exception(f"'dumpsPacked' has not been implemented in {str(type(self))}")


class NormalSchema(Schema):
    _type = fields.String(default="IncrementalInference.PackedNormal")
    mu = fields.Float()
    sigma = fields.Float()

    @post_load
    def marshal(self, data, **kwargs):
        return Normal(**data)

    class Meta:
        ordered = True


@dataclass
class Normal(Distribution):
    mu: float
    sigma: float
    _type: str = "IncrementalInference.PackedNormal"

    def dumps(self):
        return NormalSchema().dumps(self)

    def dump(self):
        return NormalSchema().dump(self)

    @staticmethod
    def load(data):
        return NormalSchema().load(data)


class FullNormalSchema(Schema):
    _type = fields.String(default="IncrementalInference.PackedFullNormal")
    mu = fields.List(fields.Float)
    cov = fields.Method("get_cov", "set_cov", required=True)

    def get_cov(self, obj):
        return obj.cov.flatten().tolist()

    def set_cov(self, obj):
        raise Exception("Deserialization not supported yet.")  # obj.cov.reshape(3,3)?

    class Meta:
        ordered = True
        unknown = EXCLUDE  # Note: This is because of _version, remote and fix later.

    @post_load
    def marshal(self, data, **kwargs):
        return FullNormal(**data)


@dataclass
class FullNormal(Distribution):
    # TODO: Remove the default initializers.
    mu: numpy.ndarray = field(default_factory=lambda: numpy.zeros(3))
    cov: numpy.ndarray = field(default_factory=lambda: numpy.diag([0.1, 0.1, 0.1]))
    _type: str = "IncrementalInference.PackedFullNormal"

    def dumps(self):
        return FullNormalSchema().dumps(self)

    def dump(self):
        return FullNormalSchema().dump(self)

    @staticmethod
    def load(data):
        return FullNormalSchema().load(data)
