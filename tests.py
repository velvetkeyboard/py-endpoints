import unittest
from endpoints.lib import Endpoint
from endpoints.credentials import Credential
from endpoints.methods import GET
from endpoints.exceptions import HttpMethodIsNotSupported


class EndpointTestCase(unittest.TestCase):

    def test_get_url(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'

        class FooBarEndpoint(FooEndpoint):
            path = '/bar'

        bar = FooBarEndpoint()
        self.assertEqual(bar.get_url(), 'http://foo/bar')

    def test_get_url_appended_slash(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo/'

        class FooBarEndpoint(FooEndpoint):
            path = '/bar'

        bar = FooBarEndpoint()
        self.assertEqual(bar.get_url(), 'http://foo/bar')

    def test_get_url_missing_slash(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'

        bar = FooBarEndpoint()
        self.assertEqual(bar.get_url(), 'http://foo/bar')

    def test_query_params_merging(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'
            query_params = {'hello': 1}

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'

            def get_query_params(self):
                return super().get_query_params({
                    'world': 2,
                    })

        bar = FooBarEndpoint()
        self.assertDictEqual(bar.get_query_params(), {'hello': 1, 'world': 2})

    def test_headers_merging(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'
            headers = {'hello': 1}

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'

            def get_headers(self):
                return super().get_headers({
                    'world': 2,
                    })

        bar = FooBarEndpoint()
        self.assertDictEqual(bar.get_headers(), {'hello': 1, 'world': 2})

    def test_unsupported_methods(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'
            methods = [
                GET,
                ]

        c = Credential()
        with self.assertRaises(HttpMethodIsNotSupported):
            FooBarEndpoint(c).post()

    def test_credentials_headers(self):
        class TokenCredential(Credential):
            headers = {
                'Authorization': 'Bearer FooBar',
                }

        class FooEndpoint(Endpoint):
            domain = 'http://foo'
            headers = {
                'Content-Type': 'application/json',
                }

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'

        c = TokenCredential()
        bar = FooBarEndpoint(c)
        headers = {
            'Authorization': 'Bearer FooBar',
            'Content-Type': 'application/json',
            }
        self.assertDictEqual(bar.get_headers(), headers)

    def test_credentials_query_params(self):
        class TokenCredential(Credential):
            query_params = {
                'token': 'FooBar',
                }

        class FooEndpoint(Endpoint):
            domain = 'http://foo'
            query_params = {
                'format': 'json',
                }

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'

        c = TokenCredential()
        bar = FooBarEndpoint(c)
        query_params = {
            'token': 'FooBar',
            'format': 'json',
            }
        self.assertDictEqual(bar.get_query_params(), query_params)
