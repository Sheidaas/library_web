from django.test import TestCase


class TestForDevs(TestCase):
    def test_render_for_devs(self):
        response = self.client.get('/library/for_devs')
        self.assertEqual(response.status_code, 200)
