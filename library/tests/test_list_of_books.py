from django.test import TestCase
from library.models.book import Book
from library.models.author import Author
from library.views.list_of_books import filter_books


class TestListOfBooks(TestCase):

    def setUp(self):
        super().setUp()
        book = Book()
        book.title = 'Hobbit'
        book.language = 'en'
        book.url_to_cover = ' '
        book.page_count = 100
        book.published_date = '2000-01-01'

        author = Author()
        author.full_name = 'J. R. R. Tolkien'
        author.save()

        book.save()
        book.authors.add(author)

    def test_render_list_of_books(self):

        response = self.client.get('/library/list_of_books')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/library/list_of_books', data={})
        self.assertEqual(response.status_code, 200)

    def test_filter_books(self):
        _filter = {'title': 'H', 'authors': [''], 'language': '', 'published_date': {}}
        books = filter_books(_filter)
        self.assertTrue(books)
        self.assertEqual(books[0].title, 'Hobbit')
        self.assertEqual(books[0].published_date.strftime('%Y-%m-%d'), '2000-01-01')

        _filter = {'title': 'H', 'authors': [''], 'language': 'pl', 'published_date': {}}
        books = filter_books(_filter)
        self.assertFalse(books)
