# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.chunk_extra_info_schema import ChunkExtraInfoSchema
from .shared_params.string_extra_info_schema import StringExtraInfoSchema
from .evaluation_datasets.flexible_chunk_param import FlexibleChunkParam
from .evaluation_datasets.flexible_message_param import FlexibleMessageParam

__all__ = ["ResultSchemaFlexibleParam", "GenerationExtraInfo"]

GenerationExtraInfo: TypeAlias = Union[ChunkExtraInfoSchema, StringExtraInfoSchema]


class ResultSchemaFlexibleParam(TypedDict, total=False):
    generation_output: Required[
        Union[
            str,
            Dict[
                str,
                Union[
                    str, float, Iterable[FlexibleChunkParam], Iterable[FlexibleMessageParam], Iterable[object], object
                ],
            ],
        ]
    ]

    generation_extra_info: GenerationExtraInfo
