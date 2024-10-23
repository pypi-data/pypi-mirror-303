# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InteractionCreateParams", "Input", "Output", "OutputContext", "TraceSpan"]


class InteractionCreateParams(TypedDict, total=False):
    application_variant_id: Required[str]
    """Identifier for the application variant that performed this interaction."""

    input: Required[Input]
    """Represents the input of an interaction."""

    output: Required[Output]
    """Represents the output of an interaction."""

    start_timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp marking the start of the interaction."""

    duration_ms: int
    """Duration of the interaction in milliseconds."""

    operation_metadata: object
    """
    Optional metadata related to the operation, including custom or predefined keys.
    """

    operation_status: Literal["SUCCESS", "ERROR"]
    """Enum representing the status of an operation."""

    thread_id: str
    """
    Optional UUID identifying the conversation thread associated with the
    interaction.The interaction will be associated with the thread if the id
    represents an existing thread.If the thread with the specified id is not found,
    a new thread will be created.
    """

    trace_spans: Iterable[TraceSpan]
    """
    List of trace spans associated with the interaction.These spans provide insight
    into the individual steps taken by nodes involved in generating the output.
    """


class Input(TypedDict, total=False):
    query: Required[str]
    """The query or input text for the interaction."""


class OutputContext(TypedDict, total=False):
    text: Required[str]
    """The text of the context entry."""

    score: float
    """The score of the context entry."""


class Output(TypedDict, total=False):
    response: Required[str]
    """The response or output text of the interaction."""

    context: Iterable[OutputContext]
    """Optional context information provided with the response."""


class TraceSpan(TypedDict, total=False):
    node_id: Required[str]
    """Identifier for the node that emitted this trace span."""

    operation_type: Required[Literal["COMPLETION", "RERANKING", "RETRIEVAL", "CUSTOM"]]
    """Enum representing the type of operation performed."""

    start_timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The start time of the step."""

    duration_ms: int
    """The duration of the operation step in milliseconds."""

    operation_input: object
    """The JSON representation of the input that this step received."""

    operation_metadata: object
    """The JSON representation of the metadata insights emitted during execution.

    This can differ based on different types of operations.
    """

    operation_output: object
    """The JSON representation of the output that this step emitted."""

    operation_status: Literal["SUCCESS", "ERROR"]
    """Enum representing the status of an operation."""
