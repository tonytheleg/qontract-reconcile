"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


DEFINITION = """
fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query CNAProvisioners {
  cna_provisioners: cna_experimental_provisioners_v1 {
    name
    description
    ocm {
      name
      accessTokenUrl
      accessTokenClientId
      accessTokenClientSecret {
        ... VaultSecret
      }
      url
    }
  }
}
"""


class OpenShiftClusterManagerV1(BaseModel):
    name: str = Field(..., alias="name")
    access_token_url: str = Field(..., alias="accessTokenUrl")
    access_token_client_id: str = Field(..., alias="accessTokenClientId")
    access_token_client_secret: Optional[VaultSecret] = Field(
        ..., alias="accessTokenClientSecret"
    )
    url: str = Field(..., alias="url")

    class Config:
        smart_union = True
        extra = Extra.forbid


class CNAExperimentalProvisionerV1(BaseModel):
    name: str = Field(..., alias="name")
    description: Optional[str] = Field(..., alias="description")
    ocm: OpenShiftClusterManagerV1 = Field(..., alias="ocm")

    class Config:
        smart_union = True
        extra = Extra.forbid


class CNAProvisionersQueryData(BaseModel):
    cna_provisioners: Optional[list[CNAExperimentalProvisionerV1]] = Field(
        ..., alias="cna_provisioners"
    )

    class Config:
        smart_union = True
        extra = Extra.forbid


def query(query_func: Callable, **kwargs: Any) -> CNAProvisionersQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        CNAProvisionersQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return CNAProvisionersQueryData(**raw_data)
