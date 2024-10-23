# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""DICOMweb Abstract Credential Factory and Default implementation."""
import abc
import copy
import hashlib
import json
import os
from typing import Any, Dict, List, Mapping, Optional, Union

import google.auth
import google.auth.transport.requests
from google.oauth2 import service_account
import requests  # Required by: google.auth.transport.requests.Request()

_SCOPES = [
    'https://www.googleapis.com/auth/cloud-platform',
    'https://www.googleapis.com/auth/cloud-healthcare',
]


class AbstractCredentialFactory(metaclass=abc.ABCMeta):
  """Generates the credentials used to access DICOM store.

  Implementations of the abstract credential factory should be compatible with
  pickle serialization. The purpose of the credential factory is to enable
  EZ-WSI to construct the credentials needed to access the DICOM store
  following pickle deserialization. As one example, this enables EZ-WSI DICOM
  Store and DICOM Slide classes to be initialized once and passed through a
  cloud dataflow pipeline.
  """

  @abc.abstractmethod
  def get_credentials(self) -> google.auth.credentials.Credentials:
    """Return credentials to use to access DICOM Store."""

  def credential_source_hash(self) -> str:
    """Returns hash value to identify credential source.

    Empty string considered undefined.  Used enable crediental caching across
    multiple credential factory instances that target the same credential
    source. Only should be defined if the acquisition of credential is time
    consuming.
    """
    return ''


def refresh_credentials(
    auth_credentials: google.auth.credentials.Credentials,
) -> google.auth.credentials.Credentials:
  """Refreshs credentials."""
  if not auth_credentials.valid:
    auth_credentials.refresh(google.auth.transport.requests.Request())
  return auth_credentials


def get_default_gcp_project() -> str:
  """Return GCP project current user os runniing in."""
  return google.auth.default(scopes=_SCOPES)[1]


class CredentialFactory(AbstractCredentialFactory):
  """Factory for default or service account credential creation."""

  def __init__(
      self,
      json_param: Optional[
          Union[Mapping[str, Any], str, bytes, os.PathLike[Any]]
      ] = None,
      scopes: Optional[List[str]] = None,
  ) -> None:
    """Credential Factory Constructor.

    Args:
      json_param: Optional parameter that defines location of JSON file, or
        loaded JSON that contains service account credentials which should be
        used for auth.  If undefined, then the default credentials of the
        running environment are used.
      scopes: Credential scopes if undefined defaults to:
        ['https://www.googleapis.com/auth/cloud-platform',
        'https://www.googleapis.com/auth/cloud-healthcare',]
    """
    if not json_param:
      self._json = {}
    elif (
        isinstance(json_param, str)
        or isinstance(json_param, bytes)
        or isinstance(json_param, os.PathLike)
    ):
      # Read JSON from file."""
      with open(json_param, 'rt') as infile:
        self._json = json.load(infile)
    else:
      # Use in memory JSON loaded in memory as python Dict.
      self._json = copy.copy(json_param)
    if not self._json:
      self._credential_source_hash = 'application_default_credentials'
    else:
      self._credential_source_hash = hashlib.sha3_512(
          json.dumps(self._json).encode('utf-8')
      ).hexdigest()
    self._scopes = _SCOPES if scopes is None else copy.copy(scopes)

  def get_credentials(self) -> google.auth.credentials.Credentials:
    """Returns credentials to use to accessing DICOM store."""
    if self._json:
      return refresh_credentials(
          service_account.Credentials.from_service_account_info(
              self._json, scopes=self._scopes
          )
      )
    return refresh_credentials(google.auth.default(scopes=self._scopes)[0])

  def credential_source_hash(self) -> str:
    return self._credential_source_hash


ServiceAccountCredentialFactory = CredentialFactory


class DefaultCredentialFactory(CredentialFactory):
  """Factory for default credential creation."""

  def __init__(self, scopes: Optional[List[str]] = None) -> None:
    super().__init__(scopes=scopes)


class PassThroughCredentials(google.auth.credentials.Credentials):
  """Credentials that do not provide any authentication refresh information.

  These are similar to anonymous credentials in that refreshing is not possible.
  """

  def __init__(self, token: str):
    """Initializes a Pete Credential object with a token."""
    super().__init__()
    self.token = token

  @property
  def expired(self) -> bool:
    """Returns False, assume tokens never expire."""
    return False

  @property
  def valid(self) -> bool:
    """Returns True, assume tokens are always valid."""
    return True

  def refresh(self, request: google.auth.transport.Request) -> None:
    return

  def apply(self, headers: Dict[Any, Any], token: Optional[str] = None) -> None:
    """Apply the token to the authentication header.

    Args:
        headers: The HTTP request headers.
        token: If specified, overrides the current access token.

    Returns:
      Nothing.
    """
    headers['authorization'] = 'Bearer {}'.format(token or self.token)

  def before_request(
      self,
      request: google.auth.transport.Request,
      method: str,
      url: str,
      headers: Dict[Any, Any],
  ) -> None:
    """Performs credential-specific before request logic.

    Calls apply to apply the token to the authentication header.

    Args:
        request: The object used to make HTTP requests.
        method: The request's HTTP method or the RPC method being invoked.
        url: The request's URI or the RPC service's URI.
        headers: The request's headers.

    Returns:
      Nothing.
    """
    self.apply(headers)


class NoAuthCredentials(google.auth.credentials.Credentials):
  """Credentials that do not provide any authentication refresh information.

  These are similar to anonymous credentials in that refreshing is not possible.
  """

  @property
  def expired(self) -> bool:
    """Never expire."""
    return False

  @property
  def valid(self) -> bool:
    """Returns True, always valid."""
    return True

  def refresh(self, request: google.auth.transport.Request) -> None:
    return

  def apply(self, headers: Dict[Any, Any], token: Optional[str] = None) -> None:
    return

  def before_request(
      self,
      request: google.auth.transport.Request,
      method: str,
      url: str,
      headers: Dict[Any, Any],
  ) -> None:
    return


class TokenPassthroughCredentialFactory(AbstractCredentialFactory):
  """Factory for token passthrough credential creation."""

  def __init__(self, bearer_token: str) -> None:
    """Credential Factory Constructor.

    Args:
      bearer_token: The user provided bearer token that allows us to access
        their dicom store.
    """
    self._bearer_token = bearer_token
    self._credential = PassThroughCredentials(self._bearer_token)

  def get_credentials(self) -> google.auth.credentials.Credentials:
    """Returns credentials to use to accessing DICOM store."""
    return self._credential


class GoogleAuthCredentialFactory(AbstractCredentialFactory):
  """Holds credentials can not be pickled."""

  def __init__(self, credentials: google.auth.credentials.Credentials):
    self._auth_credentials = credentials

  def get_credentials(self) -> google.auth.credentials.Credentials:
    """Return credentials to use to access DICOM Store."""
    return self._auth_credentials


class NoAuthCredentialsFactory(AbstractCredentialFactory):
  """Holds credentials can not be pickled."""

  def __init__(self):
    self._auth_credentials = NoAuthCredentials()

  def get_credentials(self) -> google.auth.credentials.Credentials:
    """Return credentials to use to access DICOM Store."""
    return self._auth_credentials
