# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "FlexibleMessageParam",
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
    TypedDict, total=False
):
    text: Required[str]

    type: Literal["text"]


class EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageURLUserMessageContentPartsImageURL(
    TypedDict, total=False
):
    url: Required[str]
    """The URL of the image. Note: only OpenAI supports this."""

    detail: Literal["low", "high", "auto"]
    """Only used for OpenAI. Corresponds to OpenAI's image detail parameter."""


class EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageURLUserMessageContentParts(
    TypedDict, total=False
):
    image_url: Required[
        EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageURLUserMessageContentPartsImageURL
    ]

    type: Literal["image_url"]


class EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageDataUserMessageContentPartsImageData(
    TypedDict, total=False
):
    data: Required[str]
    """The base64-encoded image data."""

    media_type: Required[str]
    """The media/mime type of the image data.

    For example, 'image/png'. Check providers' documentation for supported media
    types.
    """

    detail: Literal["low", "high", "auto"]
    """Only used for OpenAI. Corresponds to OpenAI's image detail parameter."""

    type: Literal["base64"]
    """The type of the image data. Only base64 is supported."""


class EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageDataUserMessageContentParts(
    TypedDict, total=False
):
    image_data: Required[
        EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageDataUserMessageContentPartsImageData
    ]

    type: Literal["image_data"]


EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1: TypeAlias = Union[
    EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesTextUserMessageContentParts,
    EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageURLUserMessageContentParts,
    EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1EgpAPIBackendServerInternalEntitiesImageDataUserMessageContentParts,
]


class EgpAPIBackendServerInternalEntitiesUserMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[EgpAPIBackendServerInternalEntitiesUserMessageContentUnionMember1]]]

    role: Literal["user"]


class EgpAPIBackendServerInternalEntitiesAssistantMessage(TypedDict, total=False):
    content: Required[str]

    role: Literal["assistant"]


class EgpAPIBackendServerInternalEntitiesSystemMessage(TypedDict, total=False):
    content: Required[str]

    role: Literal["system"]


FlexibleMessageParam: TypeAlias = Union[
    EgpAPIBackendServerInternalEntitiesUserMessage,
    EgpAPIBackendServerInternalEntitiesAssistantMessage,
    EgpAPIBackendServerInternalEntitiesSystemMessage,
]
