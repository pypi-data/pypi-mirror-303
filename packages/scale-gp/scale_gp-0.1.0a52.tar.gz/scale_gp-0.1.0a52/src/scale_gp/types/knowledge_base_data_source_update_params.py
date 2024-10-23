# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

from .s3_data_source_auth_config_param import S3DataSourceAuthConfigParam
from .slack_data_source_auth_config_param import SlackDataSourceAuthConfigParam
from .confluence_data_source_auth_config_param import ConfluenceDataSourceAuthConfigParam
from .share_point_data_source_auth_config_param import SharePointDataSourceAuthConfigParam
from .google_drive_data_source_auth_config_param import GoogleDriveDataSourceAuthConfigParam
from .azure_blob_storage_data_source_auth_config_param import AzureBlobStorageDataSourceAuthConfigParam

__all__ = ["KnowledgeBaseDataSourceUpdateParams", "DataSourceAuthConfig"]


class KnowledgeBaseDataSourceUpdateParams(TypedDict, total=False):
    data_source_auth_config: DataSourceAuthConfig

    description: str

    name: str


DataSourceAuthConfig: TypeAlias = Union[
    SharePointDataSourceAuthConfigParam,
    AzureBlobStorageDataSourceAuthConfigParam,
    GoogleDriveDataSourceAuthConfigParam,
    S3DataSourceAuthConfigParam,
    ConfluenceDataSourceAuthConfigParam,
    SlackDataSourceAuthConfigParam,
]
