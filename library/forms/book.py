from django import forms
from ..models.book import Book
from .validators.date_validator import validate_date_format
from .validators.isbn_validator import validate_isbn
from .validators.validate_page_count import validate_page_count
from .validators.validate_is_this_url import validate_is_this_url
import datetime


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Hobbit'}))
    language = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'en'}))
    url_to_cover = forms.CharField(validators=[validate_is_this_url], widget=forms.TextInput(attrs={'placeholder': 'https://link_to_cover.com'}))
    published_date = forms.CharField(validators=[validate_date_format], widget=forms.TextInput(attrs={'placeholder': '1999-02-04'}))
    isbn = forms.CharField(validators=[validate_isbn], widget=forms.TextInput(attrs={'placeholder': '0000000000000 13 digits'}))
    page_count = forms.CharField(widget=forms.NumberInput(attrs={'type': 'number', 'placeholder': 100}), validators=[validate_page_count])

    class Meta:
        model = Book
        fields = ['title', 'url_to_cover', 'published_date',
                  'language', 'isbn', 'authors', 'page_count']
