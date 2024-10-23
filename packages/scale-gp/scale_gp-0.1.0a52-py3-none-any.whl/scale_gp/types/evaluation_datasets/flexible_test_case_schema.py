# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .flexible_chunk import FlexibleChunk
from .flexible_message import FlexibleMessage
from ..shared.chunk_extra_info_schema import ChunkExtraInfoSchema
from ..shared.string_extra_info_schema import StringExtraInfoSchema

__all__ = ["FlexibleTestCaseSchema", "ExpectedExtraInfo"]

ExpectedExtraInfo: TypeAlias = Annotated[
    Union[ChunkExtraInfoSchema, StringExtraInfoSchema], PropertyInfo(discriminator="schema_type")
]


class FlexibleTestCaseSchema(BaseModel):
    input: Union[str, Dict[str, Union[str, float, List[FlexibleChunk], List[FlexibleMessage], List[object], object]]]

    expected_extra_info: Optional[ExpectedExtraInfo] = None

    expected_output: Union[
        str, Dict[str, Union[str, float, List[FlexibleChunk], List[FlexibleMessage], List[object], object]], None
    ] = None
