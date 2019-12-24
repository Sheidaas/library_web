from django.test import TestCase


class TestIndex(TestCase):
    def test_render_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/library/index')
        self.assertEqual(response.status_code, 200)
