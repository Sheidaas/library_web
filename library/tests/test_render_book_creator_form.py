from django.test import TestCase


class TestBookCreatorForm(TestCase):

    def test_render_book_creator_form(self):
        response = self.client.get('/library/book_creator_form')
        self.assertEqual(response.status_code, 200)
        
