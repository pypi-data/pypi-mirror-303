# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .application_configuration_param import ApplicationConfigurationParam

__all__ = [
    "ApplicationVariantCreateParams",
    "ApplicationVariantV0Request",
    "ApplicationVariantAgentsServiceRequest",
    "ApplicationVariantAgentsServiceRequestConfiguration",
    "ApplicationVariantAgentsServiceRequestConfigurationGraph",
    "ApplicationVariantAgentsServiceRequestConfigurationGraphEdge",
    "ApplicationVariantAgentsServiceRequestConfigurationGraphInput",
    "ApplicationVariantAgentsServiceRequestConfigurationGraphNode",
    "OfflineApplicationVariantRequest",
    "OfflineApplicationVariantRequestConfiguration",
]


class ApplicationVariantV0Request(TypedDict, total=False):
    account_id: Required[str]
    """The ID of the account that owns the given entity."""

    application_spec_id: Required[str]

    configuration: Required[ApplicationConfigurationParam]

    name: Required[str]

    version: Required[Literal["V0"]]

    description: str
    """Optional description of the application variant"""


class ApplicationVariantAgentsServiceRequest(TypedDict, total=False):
    account_id: Required[str]
    """The ID of the account that owns the given entity."""

    application_spec_id: Required[str]

    configuration: Required[ApplicationVariantAgentsServiceRequestConfiguration]

    name: Required[str]

    version: Required[Literal["AGENTS_SERVICE"]]

    description: str
    """Optional description of the application variant"""


class ApplicationVariantAgentsServiceRequestConfigurationGraphEdge(TypedDict, total=False):
    from_node: Required[str]

    to_node: Required[str]


class ApplicationVariantAgentsServiceRequestConfigurationGraphInput(TypedDict, total=False):
    name: Required[str]

    type: Required[str]


class ApplicationVariantAgentsServiceRequestConfigurationGraphNode(TypedDict, total=False):
    id: Required[str]

    config: Required[object]

    name: Required[str]

    type: Required[str]


class ApplicationVariantAgentsServiceRequestConfigurationGraph(TypedDict, total=False):
    edges: Required[Iterable[ApplicationVariantAgentsServiceRequestConfigurationGraphEdge]]

    inputs: Required[Iterable[ApplicationVariantAgentsServiceRequestConfigurationGraphInput]]

    nodes: Required[Iterable[ApplicationVariantAgentsServiceRequestConfigurationGraphNode]]


class ApplicationVariantAgentsServiceRequestConfiguration(TypedDict, total=False):
    params: Required[object]

    type: Required[Literal["WORKFLOW", "PLAN", "STATE_MACHINE"]]

    graph: ApplicationVariantAgentsServiceRequestConfigurationGraph
    """The graph of the agents service configuration"""

    metadata: object
    """User defined metadata about the application"""


class OfflineApplicationVariantRequest(TypedDict, total=False):
    account_id: Required[str]
    """The ID of the account that owns the given entity."""

    application_spec_id: Required[str]

    configuration: Required[OfflineApplicationVariantRequestConfiguration]

    name: Required[str]

    version: Required[Literal["OFFLINE"]]

    description: str
    """Optional description of the application variant"""


class OfflineApplicationVariantRequestConfiguration(TypedDict, total=False):
    metadata: object
    """User defined metadata about the offline application"""

    output_schema_type: Literal["completion_only", "context_string", "context_chunks"]
    """An enumeration."""


ApplicationVariantCreateParams: TypeAlias = Union[
    ApplicationVariantV0Request, ApplicationVariantAgentsServiceRequest, OfflineApplicationVariantRequest
]
