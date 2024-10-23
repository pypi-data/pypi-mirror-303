# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InteractionCreateResponse", "Input", "Output", "OutputContext", "TraceSpan"]


class Input(BaseModel):
    query: str
    """The query or input text for the interaction."""


class OutputContext(BaseModel):
    text: str
    """The text of the context entry."""

    score: Optional[float] = None
    """The score of the context entry."""


class Output(BaseModel):
    response: str
    """The response or output text of the interaction."""

    context: Optional[List[OutputContext]] = None
    """Optional context information provided with the response."""


class TraceSpan(BaseModel):
    id: str
    """Unique identifier for the trace span."""

    application_interaction_id: str
    """The ID of the application interaction this trace span belongs to."""

    node_id: str
    """Identifier for the node that emitted this trace span."""

    operation_type: Literal["COMPLETION", "RERANKING", "RETRIEVAL", "CUSTOM"]
    """Enum representing the type of operation performed."""

    start_timestamp: datetime
    """The start time of the step."""

    duration_ms: Optional[int] = None
    """The duration of the operation step in milliseconds."""

    operation_input: Optional[object] = None
    """The JSON representation of the input that this step received."""

    operation_metadata: Optional[object] = None
    """The JSON representation of the metadata insights emitted during execution.

    This can differ based on different types of operations.
    """

    operation_output: Optional[object] = None
    """The JSON representation of the output that this step emitted."""

    operation_status: Optional[Literal["SUCCESS", "ERROR"]] = None
    """Enum representing the status of an operation."""


class InteractionCreateResponse(BaseModel):
    id: str
    """Unique identifier for the interaction."""

    application_variant_id: str
    """Identifier for the application variant that performed this interaction."""

    input: Input
    """Represents the input of an interaction."""

    output: Output
    """Represents the output of an interaction."""

    start_timestamp: datetime
    """Timestamp marking the start of the interaction."""

    duration_ms: Optional[int] = None
    """Duration of the interaction in milliseconds."""

    operation_metadata: Optional[object] = None
    """
    Optional metadata related to the operation, including custom or predefined keys.
    """

    operation_status: Optional[Literal["SUCCESS", "ERROR"]] = None
    """Enum representing the status of an operation."""

    thread_id: Optional[str] = None
    """
    Optional UUID identifying the conversation thread associated with the
    interaction.The interaction will be associated with the thread if the id
    represents an existing thread.If the thread with the specified id is not found,
    a new thread will be created.
    """

    trace_spans: Optional[List[TraceSpan]] = None
    """List of trace span entities associated with the interaction."""
