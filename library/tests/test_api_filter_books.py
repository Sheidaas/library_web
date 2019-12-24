from django.test import TestCase


class TestApiFilterBooks(TestCase):

    def test_api_filter_books(self):
        response = self.client.get('/library/get_books/intitle:.+inauthor:.'
                                   + '+inlanguage:.+published_date_from:.+published_date_to:.+')
        self.assertEqual(response.status_code, 200)
