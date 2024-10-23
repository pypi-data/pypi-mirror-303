# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "FlexibleMessage",
    "EgpAPIBackendServerInternalEntitiesUserMessage",
    "EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1",
    "EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesTextUserMessageContentParts",
    "EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageURLUserMessageContentParts",
    "EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageURLUserMessageContentPartsImageURL",
    "EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageDataUserMessageContentParts",
    "EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageDataUserMessageContentPartsImageData",
    "EgpAPIBackendServerInternalEntitiesAssistantMessage",
    "EgpAPIBackendServerInternalEntitiesSystemMessage",
]


class EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesTextUserMessageContentParts(
    BaseModel
):
    text: str

    type: Optional[Literal["text"]] = None


class EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageURLUserMessageContentPartsImageURL(
    BaseModel
):
    url: str
    """The URL of the image. Note: only OpenAI supports this."""

    detail: Optional[Literal["low", "high", "auto"]] = None
    """Only used for OpenAI. Corresponds to OpenAI's image detail parameter."""


class EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageURLUserMessageContentParts(
    BaseModel
):
    image_url: EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageURLUserMessageContentPartsImageURL

    type: Optional[Literal["image_url"]] = None


class EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageDataUserMessageContentPartsImageData(
    BaseModel
):
    data: str
    """The base64-encoded image data."""

    media_type: str
    """The media/mime type of the image data.

    For example, 'image/png'. Check providers' documentation for supported media
    types.
    """

    detail: Optional[Literal["low", "high", "auto"]] = None
    """Only used for OpenAI. Corresponds to OpenAI's image detail parameter."""

    type: Optional[Literal["base64"]] = None
    """The type of the image data. Only base64 is supported."""


class EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageDataUserMessageContentParts(
    BaseModel
):
    image_data: EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageDataUserMessageContentPartsImageData

    type: Optional[Literal["image_data"]] = None


EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesTextUserMessageContentParts,
        EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageURLUserMessageContentParts,
        EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageDataUserMessageContentParts,
    ],
    PropertyInfo(discriminator="type"),
]


class EgpAPIBackendServerInternalEntitiesUserMessage(BaseModel):
    content: Union[str, List[EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1]]

    role: Optional[Literal["user"]] = None


class EgpAPIBackendServerInternalEntitiesAssistantMessage(BaseModel):
    content: str

    role: Optional[Literal["assistant"]] = None


class EgpAPIBackendServerInternalEntitiesSystemMessage(BaseModel):
    content: str

    role: Optional[Literal["system"]] = None


FlexibleMessage: TypeAlias = Annotated[
    Union[
        EgpAPIBackendServerInternalEntitiesUserMessage,
        EgpAPIBackendServerInternalEntitiesAssistantMessage,
        EgpAPIBackendServerInternalEntitiesSystemMessage,
    ],
    PropertyInfo(discriminator="role"),
]
