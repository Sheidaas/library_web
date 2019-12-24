from django.test import TestCase


class TestImportFromValue(TestCase):

    def test_import_from_value(self):
        response = self.client.get('/library/google_book_searcher')
        self.assertEqual(response.status_code, 200)

        # Test is google book searcher correctly import raw data to models
        response = self.client.post('/library/google_book_searcher', data={'keywords': 'hobbit'})
        self.assertEqual(response.status_code, 302)




