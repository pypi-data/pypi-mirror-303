# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .flexible_test_case_schema_param import FlexibleTestCaseSchemaParam
from .artifact_schema_generation_param import ArtifactSchemaGenerationParam
from .generation_test_case_schema_param import GenerationTestCaseSchemaParam

__all__ = ["TestCaseBatchParams", "Item", "ItemTestCaseData"]


class TestCaseBatchParams(TypedDict, total=False):
    items: Required[Iterable[Item]]


ItemTestCaseData: TypeAlias = Union[
    ArtifactSchemaGenerationParam, GenerationTestCaseSchemaParam, FlexibleTestCaseSchemaParam
]


class Item(TypedDict, total=False):
    test_case_data: Required[ItemTestCaseData]
    """The data for the test case in a format matching the provided schema_type"""

    account_id: str
    """The ID of the account that owns the given entity."""

    chat_history: object
    """Used for tracking previous chat interactions for multi-chat test cases"""

    test_case_metadata: object
    """Metadata for the test case"""
