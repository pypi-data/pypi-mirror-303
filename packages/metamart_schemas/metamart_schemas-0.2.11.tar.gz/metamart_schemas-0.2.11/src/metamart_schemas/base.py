from typing import Union

from metamart_schemas import v1
from metamart_schemas.generics import MetamartBaseModel, MalformedMetadata
from metamart_schemas.v1.metadata import edges as edge_v1
from metamart_schemas.v1.metadata import nodes as node_v1


class MetamartMetadata(MetamartBaseModel):
    """Class definition of MetamartMetadata

    Attributes:
        metamart: Metamart defined metadata attributes used to drive application logic.

    """

    metamart: Union[node_v1.Metadata, edge_v1.Metadata]


Node = v1.node.NodeV1
Edge = v1.edge.EdgeV1


SourcedNode = v1.node.SourcedNodeV1
SourcedEdge = v1.edge.SourcedEdgeV1
Source = v1.source.SourceV1
Event = v1.events.EventV1
Workspace = v1.workspace.WorkspaceV1
Organisation = v1.organization.OrganisationV1

MetamartType = Union[Node, Edge, SourcedNode, SourcedEdge, Source, Event, Workspace, Organisation]

__all__ = [
    "MetamartMetadata",
    "Node",
    "Edge",
    "Event",
    "SourcedNode",
    "SourcedEdge",
    "Source",
    "Workspace",
    "Organisation",
    "MetamartType",
]
