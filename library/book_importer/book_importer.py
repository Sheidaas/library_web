from ..models.book import Book
from ..models.author import Author
from django.core.exceptions import ObjectDoesNotExist


class BooksImporter:


    def create_url(self, keywords: list):
        valid_string = self.create_valid_string(keywords)
        url = 'https://www.googleapis.com/books/v1/volumes?q='
        url += valid_string
        return url

    def create_books(self, items_list: list):
        for item in items_list:
            try:
                book_isbn = self.get_valid_isbn_from_industry_identifiers_list(item['volumeInfo']['industryIdentifiers'])
                if not self.is_book_in_database(book_isbn):
                    book = Book()
                    book.page_count = item['volumeInfo']['pageCount']
                    book.title = item['volumeInfo']['title']
                    book.language = item['volumeInfo']['language']
                    book.isbn = book_isbn
                    book.url_to_cover = self.get_valid_url_to_cover_from_image_links_dict(item['volumeInfo']['imageLinks'])
                    book.published_date = self.get_valid_published_date(item['volumeInfo']['publishedDate'])
                    book.save()
                    for author in self.get_valid_authors_from_authors_list(item['volumeInfo']['authors']):
                        book.authors.add(author)
            except KeyError:
                pass

    @staticmethod
    def is_book_in_database(book_isbn):
        try:
            Book.objects.get(isbn=book_isbn)
            return True
        except ObjectDoesNotExist:
            return False

    @staticmethod
    def create_valid_string(strings_list: list):
        new_string = ''
        for word in strings_list:
            new_string += word + '+'
        return new_string

    @staticmethod
    def get_valid_authors_from_authors_list(authors_list: list):
        authors = []
        for author_full_name in authors_list:
            try:
                old_author = Author.objects.get(full_name=author_full_name)
                authors.append(old_author)
            except ObjectDoesNotExist:
                new_author = Author()
                new_author.full_name = author_full_name
                new_author.save()
                authors.append(new_author)
        return authors

    @staticmethod
    def get_valid_isbn_from_industry_identifiers_list(industry_identifiers: list):
        for identifier in industry_identifiers:
            if identifier['type'] == 'ISBN_13':
                return identifier['identifier']
        raise KeyError

    @staticmethod
    def get_valid_url_to_cover_from_image_links_dict(image_links: dict):
        return image_links['thumbnail']

    @staticmethod
    def get_valid_published_date(published_date: str):
        _date = published_date.split('-')
        if len(_date) == 3:
            return published_date
        elif len(_date) == 2:
            return published_date + '-01'
        return published_date + '-01-01'

    """
    def create_url(_filter: dict) -> str:
        url = 'https://www.googleapis.com/books/v1/volumes?q='

        if _filter['keywords']:
            url += self.create_valid_string(_filter['keywords'])

        if _filter['title']:
            url += 'intitle:' + self.create_valid_string(_filter['title'])

        if _filter['author']:
            _url = 'inauthor:'
            for author_full_name in _filter['author']:
                _url += self.create_valid_string(author_full_name) + '+'
            url += _url

        return url
    """
