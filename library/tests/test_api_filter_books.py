from django.test import TestCase
from library.views.rest_api_filter_books import create_authors_full_names


class TestApiFilterBooks(TestCase):

    def test_api_filter_books(self):
        response = self.client.get('/library/get_books/intitle:.,inauthor:.'
                                   + ',inlanguage:.,published_date_from:.,published_date_to:.,')
        self.assertEqual(response.status_code, 200)

    def test_create_authors_full_names(self):
        string = 'J.+R.+R.+Tolkien-J.+K.+Rowling'
        valid_strings_list = ['J. R. R. Tolkien', 'J. K. Rowling']
        self.assertEqual(valid_strings_list, create_authors_full_names(string))

