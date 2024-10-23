# Copyright 2024 Google LLC
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

from unittest import mock

from absl.testing import absltest
from ez_wsi_dicomweb import credential_factory
import google.auth
import requests


class DicomwebCredientalFactoryTest(absltest.TestCase):

  def test_no_auth_credentials(self):
    headers = {}
    token = 'abc'

    fc = credential_factory.NoAuthCredentialsFactory()
    cred = fc.get_credentials()

    cred.refresh(requests.Request())
    cred.before_request(requests.Request(), 'get', 'abc', headers)
    self.assertEqual(headers, {})
    self.assertFalse(cred.expired)
    self.assertTrue(cred.valid)
    cred.apply(headers, token)
    self.assertEqual(headers, {})

  def test_no_auth_credentials_factory_undefined_hash(self):
    fc = credential_factory.NoAuthCredentialsFactory()
    self.assertEqual(fc.credential_source_hash(), '')

  def test_token_pass_through_factory_undefined_hash(self):
    fc = credential_factory.TokenPassthroughCredentialFactory('abc')
    self.assertEqual(fc.credential_source_hash(), '')

  def test_token_pass_through_apply(self):
    headers = {}
    token = 'abc'

    fc = credential_factory.TokenPassthroughCredentialFactory(token)
    cred = fc.get_credentials()

    self.assertFalse(cred.expired)
    self.assertTrue(cred.valid)
    cred.apply(headers, token)
    self.assertEqual(headers, {'authorization': 'Bearer abc'})

  def test_token_pass_through_before_request(self):
    headers = {}
    token = 'efg'

    fc = credential_factory.TokenPassthroughCredentialFactory(token)
    cred = fc.get_credentials()

    self.assertFalse(cred.expired)
    self.assertTrue(cred.valid)
    cred.before_request(requests.Request(), 'get', 'abc', headers)
    self.assertEqual(headers, {'authorization': 'Bearer efg'})

  def test_token_pass_through_refresh_nop(self):
    fc = credential_factory.TokenPassthroughCredentialFactory('efg')
    cred = fc.get_credentials()
    self.assertEqual(cred.token, 'efg')
    cred.refresh(requests.Request())
    self.assertEqual(cred.token, 'efg')

  def test_google_auth_factory_undefined_hash(self):
    fc = credential_factory.GoogleAuthCredentialFactory(
        mock.create_autospec(google.auth.credentials.Credentials, instance=True)
    )
    self.assertEqual(fc.credential_source_hash(), '')

  def test_default_factory_hash(self):
    fc = credential_factory.DefaultCredentialFactory()
    self.assertEqual(
        fc.credential_source_hash(), 'application_default_credentials'
    )

  def test_service_account_factory_hash(self):
    fc = credential_factory.ServiceAccountCredentialFactory({'ABC': 123})
    self.assertEqual(
        fc.credential_source_hash(),
        'e8a42b4cba471539197281b21310ffcabf8f96a3f9db422c01f4c75cf1a84e6835eeb4e59a919e7a6f470fa42724bc5bf66bef43b2d67d08dc4f10072d560b3d',
    )

  def test_core_credential_default_factory_hash(self):
    fc = credential_factory.CredentialFactory()
    self.assertEqual(
        fc.credential_source_hash(), 'application_default_credentials'
    )

  def test_core_credential_service_account_factory_hash(self):
    fc = credential_factory.CredentialFactory({'ABC': 123})
    self.assertEqual(
        fc.credential_source_hash(),
        'e8a42b4cba471539197281b21310ffcabf8f96a3f9db422c01f4c75cf1a84e6835eeb4e59a919e7a6f470fa42724bc5bf66bef43b2d67d08dc4f10072d560b3d',
    )


if __name__ == '__main__':
  absltest.main()
