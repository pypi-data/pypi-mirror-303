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

import os
import sys

import unittest

from st2auth_flat_file_backend.flat_file import FlatFileAuthenticationBackend

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class FlatFileAuthenticationBackendTestCase(unittest.TestCase):
    def test_authenticate_httpasswd_file_without_comments(self):
        file_path = os.path.join(BASE_DIR, '../fixtures/htpasswd_test')
        backend = FlatFileAuthenticationBackend(file_path=file_path)

        # Inexistent user
        self.assertFalse(backend.authenticate(username='doesntexist', password='bar'))

        # Invalid password
        self.assertFalse(backend.authenticate(username='test1', password='bar'))

        # Valid password (md5 hash)
        self.assertTrue(backend.authenticate(username='test1', password='testpassword'))

        # Valid password (sha hash - insecure)
        self.assertTrue(backend.authenticate(username='test3', password='testpassword'))

        # Valid password (crypt - insecure)
        self.assertTrue(backend.authenticate(username='test4', password='testpassword'))

    def test_authenticate_httpasswd_file_with_comments(self):
        file_path = os.path.join(BASE_DIR, '../fixtures/htpasswd_test_with_comments')
        backend = FlatFileAuthenticationBackend(file_path=file_path)

        # Inexistent user
        self.assertFalse(backend.authenticate(username='doesntexist', password='bar'))

        # Invalid password
        self.assertFalse(backend.authenticate(username='test1', password='bar'))

        # Valid password (md5 hash)
        self.assertTrue(backend.authenticate(username='test1', password='testpassword'))

        # Valid password (sha hash - insecure)
        self.assertTrue(backend.authenticate(username='test3', password='testpassword'))

        # Valid password (crypt - insecure)
        self.assertTrue(backend.authenticate(username='test4', password='testpassword'))

    def test_authenticate_httpasswd_file_doesnt_exist(self):
        file_path = os.path.join(BASE_DIR, '../fixtures/htpasswd_doesnt_exist')
        backend = FlatFileAuthenticationBackend(file_path=file_path)

        self.assertRaises(IOError, backend.authenticate, username='doesntexist', password='bar')

if __name__ == '__main__':
    sys.exit(unittest.main())
