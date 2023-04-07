import unittest
import requests
import responses
import coverage
from client import Client

class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start code coverage measurement
        cls.cov = coverage.Coverage()
        cls.cov.start()

    @classmethod
    def tearDownClass(cls):
        # Stop code coverage measurement and generate report
        cls.cov.stop()
        cls.cov.save()
        cls.cov.report()

    @responses.activate
    def test_set_rate(self):
        # Set up mock response from server
        responses.add(responses.POST, 'http://localhost:5000/set_rate',
                      json={'rate': 0.85, 'message': 'Rate for USD/EUR is set to 0.85.'})

        # Create client and make request
        client = Client('http://localhost:5000')
        response = client.set_rate('USD/EUR', 0.85)

        # Check response content
        self.assertEqual(response, {'rate': 0.85, 'message': 'Rate for USD/EUR is set to 0.85.'})

        # Check that the request was sent with the correct data
        self.assertEqual(len(responses.calls), 1)
        request_data = responses.calls[0].request.json()
        self.assertEqual(request_data, {'currency_pair': 'USD/EUR', 'rate': 0.85})

    @responses.activate
    def test_get_rate(self):
        # Set up mock response from server
        responses.add(responses.GET, 'http://localhost:5000/get_rate?currency_pair=USD/EUR',
                      json={'rate': 0.85, 'message': 'Rate for USD/EUR is 0.85.'})

        # Create client and make request
        client = Client('http://localhost:5000')
        response = client.get_rate('USD/EUR')

        # Check response content
        self.assertEqual(response, {'rate': 0.85, 'message': 'Rate for USD/EUR is 0.85.'})

        # Check that the request was sent with the correct query string parameter
        self.assertEqual(len(responses.calls), 1)
        request_url = responses.calls[0].request.url
        self.assertEqual(request_url, 'http://localhost:5000/get_rate?currency_pair=USD/EUR')

if __name__ == '__main__':
    unittest.main()
