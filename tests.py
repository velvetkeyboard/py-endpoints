import unittest
from endpoints.lib import Endpoint


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
