# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .flexible_chunk_param import FlexibleChunkParam
from .flexible_message_param import FlexibleMessageParam
from ..shared_params.chunk_extra_info_schema import ChunkExtraInfoSchema
from ..shared_params.string_extra_info_schema import StringExtraInfoSchema

__all__ = ["FlexibleTestCaseSchemaParam", "ExpectedExtraInfo"]

ExpectedExtraInfo: TypeAlias = Union[ChunkExtraInfoSchema, StringExtraInfoSchema]


class FlexibleTestCaseSchemaParam(TypedDict, total=False):
    input: Required[
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

    expected_extra_info: ExpectedExtraInfo

    expected_output: Union[
        str,
        Dict[
            str,
            Union[str, float, Iterable[FlexibleChunkParam], Iterable[FlexibleMessageParam], Iterable[object], object],
        ],
    ]
