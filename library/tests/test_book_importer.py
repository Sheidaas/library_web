from django.test import TestCase
from library.book_importer.book_importer import BooksImporter
from library.models.book import Book
from library.models.author import Author


class TestBookImporter(TestCase):

    def test_create_url(self):
        keywords = ['Hobbit']
        url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit+'
        self.assertEqual(url, BooksImporter().create_url(keywords))

    def test_create_valid_string(self):
        keywords = ['Hobbit', 'czyli', 'tam']
        valid_string = 'Hobbit+czyli+tam+'
        self.assertEqual(valid_string, BooksImporter().create_valid_string(keywords))

    def test_is_book_in_database(self):
        book = Book()
        book.title = 'Hobbit'
        book.language = 'en'
        book.url_to_cover = ' '
        book.page_count = 100
        book.published_date = '2000-01-01'
        book.isbn = '0'
        self.assertFalse(BooksImporter().is_book_in_database(book.isbn))

        book.save()
        self.assertTrue(BooksImporter().is_book_in_database(book.isbn))

    def test_get_valid_isbn_from_industry_identifiers_list(self):
        industry_identifiers = [{'type': 'ISBN_13', 'identifier': 0}]
        self.assertEqual(0, BooksImporter().get_valid_isbn_from_industry_identifiers_list(industry_identifiers))

    def test_get_valid_url_to_cover_from_image_links_dict(self):
        image_links = {'thumbnail': 'url_to_cover'}
        self.assertEqual('url_to_cover', BooksImporter().get_valid_url_to_cover_from_image_links_dict(image_links))

    def test_get_valid_published_date(self):
        published_date = '1990-11-25'
        self.assertEqual(published_date, BooksImporter().get_valid_published_date(published_date))

        published_date = '2000'
        self.assertEqual('2000-01-01', BooksImporter().get_valid_published_date(published_date))

    def test_get_valid_authors_from_authors_list(self):
        authors_list = ('Maciej Wrzeszcz', 'J. R. R. Tolkien', 'Andrzej Sapkowski')
        authors = BooksImporter.get_valid_authors_from_authors_list(authors_list)
        for index in range(len(authors_list)):
            self.assertIsInstance(authors[index], Author)
        self.assertEqual(3, len(Author.objects.all()))

        # Testing is BooksImporter add to database same authors as previous
        authors_list = ('Maciej Wrzeszcz', 'J. R. R. Tolkien', 'Andrzej Sapkowski')
        authors = BooksImporter.get_valid_authors_from_authors_list(authors_list)
        self.assertEqual(3, len(Author.objects.all()))
