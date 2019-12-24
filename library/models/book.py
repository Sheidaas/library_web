from django.db import models
from .author import Author


class Book(models.Model):
    page_count = models.IntegerField()
    url_to_cover = models.TextField()
    published_date = models.DateTimeField()
    language = models.CharField(max_length=6)
    title = models.CharField(max_length=40)
    isbn = models.CharField(max_length=13)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    def to_dict(self):
        _dict = {
            'title': self.title,
            'language': self.language,
            'url_to_cover': self.url_to_cover,
            'authors': [author.full_name for author in self.authors.all()],
            'published_date': self.published_date.strftime('%m-%d-%Y'),
            'page_count': self.page_count,
            'isbn': self.isbn
        }
        return _dict
