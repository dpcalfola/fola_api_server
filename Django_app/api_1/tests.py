from django.test import TestCase
from django.urls import reverse


class ResponseTests(TestCase):

    def test_api_1_endpoint_returns_hello_rest_api_message(self):
        """
        Test that the /api_1/ endpoint returns expected message.
        """
        response = self.client.get('/api-1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello, REST API!'})

    def test_api_1_get_integer_returns_expected_message_with_input_number(self):
        """
        Test that the /api_1/<int>/ endpoint returns expected message with input number.
        """
        number = 873
        url = reverse('api-1', kwargs={'number': number})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'message': f'Get a number: {number}',
            'number': number
        })
