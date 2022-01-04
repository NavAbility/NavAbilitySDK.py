from dataclasses import dataclass, field
from typing import List

import numpy


class Distribution:
    """
    Base type for all distribution classes.
    """

    pass

    def dumpsPacked(self):
        raise Exception(f"'dumpsPacked' has not been implemented in {str(type(self))}")


@dataclass
class FullNormal(Distribution):
    mean: List[float] = field(default_factory=lambda: [1, 0, numpy.pi / 3])
    covariance: numpy.ndarray = field(
        default_factory=lambda: numpy.diag([0.1, 0.1, 0.1])
    )

    def dumpsPacked(self):
        return f"FullNormal(\ndim: {len(self.mean)}\nμ: {str(self.mean)}\nΣ: [{';'.join([str(v).replace('[', '').replace(']', '') for v in self.covariance])}]\n)\n"  # noqa: E501, B950

    @staticmethod
    def load(data: str):
        # REF: IncrementalInference/src/SerializingDistributions.jl:111
        mean = [float(v) for v in data.split('μ')[1].split(']')[0].split('[')[1].split(',')]
        rows = data.split('Σ')[1].split(']')[0].split('[')[1].split(' ;')
        covariance = numpy.asmatrix([[float(v) for v in r.split(' ') if v != ''] for r in rows])
        return FullNormal(mean=mean,covariance=covariance)

    def __eq__(self, __o: object) -> bool:
        return self.mean == __o.mean and (self.covariance == __o.covariance).all()