# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TestCaseResultCreateParams"]


class TestCaseResultCreateParams(TypedDict, total=False):
    application_spec_id: Required[str]

    evaluation_dataset_version_num: Required[str]

    test_case_evaluation_data: Required[object]

    test_case_id: Required[str]

    account_id: str
    """The ID of the account that owns the given entity."""

    annotated_by_user_id: str
    """The user who annotated the task."""

    audit_comment: str

    audit_required: bool

    audit_status: Literal["UNAUDITED", "FIXED", "APPROVED"]
    """An enumeration."""

    result: object

    time_spent_labeling_s: int
    """The time spent labeling in seconds."""
