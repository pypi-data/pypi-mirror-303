# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import http.client

import requests

from urllib.parse import urljoin, urlparse

__all__ = [
    'KeystoneAuthenticationBackend'
]

LOG = logging.getLogger(__name__)


class KeystoneAuthenticationBackend(object):
    """
    Backend which reads authentication information from keystone

    Note: This backend depends on the "requests" library.
    """

    def __init__(self, keystone_url, keystone_version=2):
        """
        :param keystone_url: Url of the Keystone server to authenticate against.
        :type keystone_url: ``str``
        :param keystone_version: Keystone version to authenticate against (default to 2).
        :type keystone_version: ``int``
        """
        url = urlparse(keystone_url)
        if url.path != '' or url.query != '' or url.fragment != '':
            raise Exception("The Keystone url {} does not seem to be correct.\n"
                            "Please only set the scheme+url+port "
                            "(e.x.: http://example.com:5000)".format(keystone_url))
        self._keystone_url = keystone_url
        self._keystone_version = keystone_version

    def authenticate(self, username, password):
        if self._keystone_version == 2:
            creds = self._get_v2_creds(username=username, password=password)
            login_url = urljoin(self._keystone_url, 'v2.0/tokens')
        elif self._keystone_version == 3:
            creds = self._get_v3_creds(username=username, password=password)
            login_url = urljoin(self._keystone_url, 'v3/auth/tokens')
        else:
            raise Exception("Keystone version {} not supported".format(self._keystone_version))

        try:
            login = requests.post(login_url, json=creds)
        except Exception as e:
            LOG.debug('Authentication for user "{}" failed: {}'.format(username, str(e)))
            return False

        if login.status_code in [http.client.OK, http.client.CREATED]:
            LOG.debug('Authentication for user "{}" successful'.format(username))
            return True
        else:
            LOG.debug('Authentication for user "{}" failed: {}'.format(username, login.content))
            return False

    def get_user(self, username):
        pass

    def _get_v2_creds(self, username, password):
        creds = {
            "auth": {
                "passwordCredentials": {
                    "username": username,
                    "password": password
                }
            }
        }
        return creds

    def _get_v3_creds(self, username, password):
        creds = {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "name": username,
                            "domain": {
                                "id": "default"
                            },
                            "password": password
                        }
                    }
                }
            }
        }
        return creds
