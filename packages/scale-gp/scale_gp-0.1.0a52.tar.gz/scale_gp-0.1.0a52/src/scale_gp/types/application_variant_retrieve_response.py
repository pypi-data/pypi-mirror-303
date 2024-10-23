# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .application_configuration import ApplicationConfiguration

__all__ = [
    "ApplicationVariantRetrieveResponse",
    "ApplicationVariantV0Response",
    "ApplicationVariantAgentsServiceResponse",
    "ApplicationVariantAgentsServiceResponseConfiguration",
    "ApplicationVariantAgentsServiceResponseConfigurationGraph",
    "ApplicationVariantAgentsServiceResponseConfigurationGraphEdge",
    "ApplicationVariantAgentsServiceResponseConfigurationGraphInput",
    "ApplicationVariantAgentsServiceResponseConfigurationGraphNode",
    "OfflineApplicationVariantResponse",
    "OfflineApplicationVariantResponseConfiguration",
]


class ApplicationVariantV0Response(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    application_spec_id: str

    configuration: ApplicationConfiguration

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    name: str

    version: Literal["V0"]

    created_by_user_id: Optional[str] = None
    """The user who originally created the entity."""

    description: Optional[str] = None
    """Optional description of the application variant"""


class ApplicationVariantAgentsServiceResponseConfigurationGraphEdge(BaseModel):
    from_node: str

    to_node: str


class ApplicationVariantAgentsServiceResponseConfigurationGraphInput(BaseModel):
    name: str

    type: str


class ApplicationVariantAgentsServiceResponseConfigurationGraphNode(BaseModel):
    id: str

    config: object

    name: str

    type: str


class ApplicationVariantAgentsServiceResponseConfigurationGraph(BaseModel):
    edges: List[ApplicationVariantAgentsServiceResponseConfigurationGraphEdge]

    inputs: List[ApplicationVariantAgentsServiceResponseConfigurationGraphInput]

    nodes: List[ApplicationVariantAgentsServiceResponseConfigurationGraphNode]


class ApplicationVariantAgentsServiceResponseConfiguration(BaseModel):
    params: object

    type: Literal["WORKFLOW", "PLAN", "STATE_MACHINE"]

    graph: Optional[ApplicationVariantAgentsServiceResponseConfigurationGraph] = None
    """The graph of the agents service configuration"""

    metadata: Optional[object] = None
    """User defined metadata about the application"""


class ApplicationVariantAgentsServiceResponse(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    application_spec_id: str

    configuration: ApplicationVariantAgentsServiceResponseConfiguration

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    name: str

    version: Literal["AGENTS_SERVICE"]

    created_by_user_id: Optional[str] = None
    """The user who originally created the entity."""

    description: Optional[str] = None
    """Optional description of the application variant"""


class OfflineApplicationVariantResponseConfiguration(BaseModel):
    metadata: Optional[object] = None
    """User defined metadata about the offline application"""

    output_schema_type: Optional[Literal["completion_only", "context_string", "context_chunks"]] = None
    """An enumeration."""


class OfflineApplicationVariantResponse(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    application_spec_id: str

    configuration: OfflineApplicationVariantResponseConfiguration

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    name: str

    version: Literal["OFFLINE"]

    created_by_user_id: Optional[str] = None
    """The user who originally created the entity."""

    description: Optional[str] = None
    """Optional description of the application variant"""


ApplicationVariantRetrieveResponse: TypeAlias = Annotated[
    Union[ApplicationVariantV0Response, ApplicationVariantAgentsServiceResponse, OfflineApplicationVariantResponse],
    PropertyInfo(discriminator="version"),
]
