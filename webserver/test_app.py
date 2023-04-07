import json
import unittest
from unittest import TestCase
from app import app


class TestAPI(TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_set_rate_success(self):
        response = self.client.post('/set_rate', data=json.dumps({'currency_pair': 'USD/EUR', 'rate': 0.85}),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Rate for USD/EUR is set to 0.85.')
        self.assertEqual(data['rate'], 0.85)

    def test_set_rate_missing_currency_pair(self):
        response = self.client.post('/set_rate', data=json.dumps({'rate': 0.85}), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'currency_pair parameter is missing.')

    def test_set_rate_missing_rate(self):
        response = self.client.post('/set_rate', data=json.dumps({'currency_pair': 'USD/EUR'}),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'rate parameter is missing.')

    def test_get_rate_success(self):
        self.client.post('/set_rate', data=json.dumps({'currency_pair': 'USD/EUR', 'rate': 0.85}),
                          content_type='application/json')
        response = self.client.get('/get_rate?currency_pair=USD/EUR')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Rate for USD/EUR is 0.85.')
        self.assertEqual(data['rate'], 0.85)

    def test_get_rate_missing_currency_pair(self):
        response = self.client.get('/get_rate')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'currency_pair parameter is missing.')

    def test_get_rate_not_found(self):
        response = self.client.get('/get_rate?currency_pair=USD/EUR')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'No rate set for USD/EUR yet.')


if __name__ == '__main__':
    unittest.main()
