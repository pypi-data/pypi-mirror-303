# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .application_configuration import ApplicationConfiguration

__all__ = [
    "PaginatedApplicationVariants",
    "Item",
    "ItemApplicationVariantV0Response",
    "ItemApplicationVariantAgentsServiceResponse",
    "ItemApplicationVariantAgentsServiceResponseConfiguration",
    "ItemApplicationVariantAgentsServiceResponseConfigurationGraph",
    "ItemApplicationVariantAgentsServiceResponseConfigurationGraphEdge",
    "ItemApplicationVariantAgentsServiceResponseConfigurationGraphInput",
    "ItemApplicationVariantAgentsServiceResponseConfigurationGraphNode",
    "ItemOfflineApplicationVariantResponse",
    "ItemOfflineApplicationVariantResponseConfiguration",
]


class ItemApplicationVariantV0Response(BaseModel):
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


class ItemApplicationVariantAgentsServiceResponseConfigurationGraphEdge(BaseModel):
    from_node: str

    to_node: str


class ItemApplicationVariantAgentsServiceResponseConfigurationGraphInput(BaseModel):
    name: str

    type: str


class ItemApplicationVariantAgentsServiceResponseConfigurationGraphNode(BaseModel):
    id: str

    config: object

    name: str

    type: str


class ItemApplicationVariantAgentsServiceResponseConfigurationGraph(BaseModel):
    edges: List[ItemApplicationVariantAgentsServiceResponseConfigurationGraphEdge]

    inputs: List[ItemApplicationVariantAgentsServiceResponseConfigurationGraphInput]

    nodes: List[ItemApplicationVariantAgentsServiceResponseConfigurationGraphNode]


class ItemApplicationVariantAgentsServiceResponseConfiguration(BaseModel):
    params: object

    type: Literal["WORKFLOW", "PLAN", "STATE_MACHINE"]

    graph: Optional[ItemApplicationVariantAgentsServiceResponseConfigurationGraph] = None
    """The graph of the agents service configuration"""

    metadata: Optional[object] = None
    """User defined metadata about the application"""


class ItemApplicationVariantAgentsServiceResponse(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    application_spec_id: str

    configuration: ItemApplicationVariantAgentsServiceResponseConfiguration

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    name: str

    version: Literal["AGENTS_SERVICE"]

    created_by_user_id: Optional[str] = None
    """The user who originally created the entity."""

    description: Optional[str] = None
    """Optional description of the application variant"""


class ItemOfflineApplicationVariantResponseConfiguration(BaseModel):
    metadata: Optional[object] = None
    """User defined metadata about the offline application"""

    output_schema_type: Optional[Literal["completion_only", "context_string", "context_chunks"]] = None
    """An enumeration."""


class ItemOfflineApplicationVariantResponse(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    application_spec_id: str

    configuration: ItemOfflineApplicationVariantResponseConfiguration

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    name: str

    version: Literal["OFFLINE"]

    created_by_user_id: Optional[str] = None
    """The user who originally created the entity."""

    description: Optional[str] = None
    """Optional description of the application variant"""


Item: TypeAlias = Annotated[
    Union[
        ItemApplicationVariantV0Response,
        ItemApplicationVariantAgentsServiceResponse,
        ItemOfflineApplicationVariantResponse,
    ],
    PropertyInfo(discriminator="version"),
]


class PaginatedApplicationVariants(BaseModel):
    current_page: int
    """The current page number."""

    items: List[Item]
    """The data returned for the current page."""

    items_per_page: int
    """The number of items per page."""

    total_item_count: int
    """The total number of items of the query"""
