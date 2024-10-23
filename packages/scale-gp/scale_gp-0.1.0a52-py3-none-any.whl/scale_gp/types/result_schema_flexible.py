# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.chunk_extra_info_schema import ChunkExtraInfoSchema
from .shared.string_extra_info_schema import StringExtraInfoSchema
from .evaluation_datasets.flexible_chunk import FlexibleChunk
from .evaluation_datasets.flexible_message import FlexibleMessage

__all__ = ["ResultSchemaFlexible", "GenerationExtraInfo"]

GenerationExtraInfo: TypeAlias = Annotated[
    Union[ChunkExtraInfoSchema, StringExtraInfoSchema], PropertyInfo(discriminator="schema_type")
]


class ResultSchemaFlexible(BaseModel):
    generation_output: Union[
        str, Dict[str, Union[str, float, List[FlexibleChunk], List[FlexibleMessage], List[object], object]]
    ]

    generation_extra_info: Optional[GenerationExtraInfo] = None
