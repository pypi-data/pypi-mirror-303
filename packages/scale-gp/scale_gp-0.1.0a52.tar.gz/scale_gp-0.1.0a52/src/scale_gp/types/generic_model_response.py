# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GenericModelResponse"]


class GenericModelResponse(BaseModel):
    error_message: Optional[str] = None

    status: Optional[str] = None

    status_code: Optional[int] = None
