from typing import Any, Dict, Optional, Union
from uuid import UUID

from metamart_schemas.generics import MalformedMetadata, Metadata
from metamart_schemas.utilities import merge
from metamart_schemas.v1.metadata import edges, nodes


class MetamartNodeMetadataV1(Metadata):
    """Class definition of MetamartNodeMetadataV1

    Attributes:
        metamart: Metamart defined operation attributes

    """

    metamart: nodes.Metadata


class MetamartEdgeMetadataV1(Metadata):
    """Class definition of MetamartEdgeMetadataV1

    Attributes:
        metamart: Metamart defined operation attributes

    """

    metamart: edges.Metadata


MetamartMetadataV1 = Union[MetamartNodeMetadataV1, MetamartEdgeMetadataV1]


class SourcesNodeMetadataV1(Metadata):
    """Class definition of SourcesNodeMetadataV1

    Attributes:
        sources: A dictionary of source names to source metadata

    """

    sources: Dict[str, MetamartNodeMetadataV1]


class SourcesEdgeMetadataV1(Metadata):
    """Class definition of SourcesEdgeMetadataV1

    Attributes:
        sources: A dictionary of source names to source metadata

    """

    sources: Dict[str, MetamartEdgeMetadataV1]


SourcesMetadataV1 = Union[SourcesNodeMetadataV1, SourcesEdgeMetadataV1]


class NodeMetadataV1(MetamartNodeMetadataV1, SourcesNodeMetadataV1):
    """Class definition of NodeMetadataV1"""

    pass


class EdgeMetadataV1(MetamartEdgeMetadataV1, SourcesEdgeMetadataV1):
    """Class definition of EdgeMetadataV1"""

    pass


MetadataV1 = Union[NodeMetadataV1, EdgeMetadataV1]


class MetamartMalformedNodeMetadataV1(MalformedMetadata, NodeMetadataV1):
    """Class definition of MetamartMalformedNodeMetadataV1

    Attributes:
        metamart: Metamart defined operation attributes
        sources: A dictionary of source names to source metadata

    """

    metamart: nodes.MalformedNodeMetadataV1 = nodes.MalformedNodeMetadataV1()  # type: ignore
    sources: Dict[str, nodes.Metadata] = {}


class MetamartMalformedEdgeMetadataV1(MalformedMetadata, EdgeMetadataV1):
    """Class definition of MetamartMalformedEdgeMetadataV1

    Attributes:
        metamart: Metamart defined operation attributes
        sources: A dictionary of source names to source metadata

    """

    metamart: edges.MalformedEdgeMetadataV1 = edges.MalformedEdgeMetadataV1()  # type: ignore
    sources: Dict[str, edges.Metadata] = {}
