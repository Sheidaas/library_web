from django.urls import path
from .views.book_creator_form import render_book_creator_form
from .views.list_of_books import render_list_of_books
from .views.import_from_volume import render_import_from_volume
from .views.rest_api_filter_books import render_filter_books_data
from .views.for_devs import render_for_devs
from .views.index import render_index


urlpatterns = [
    path('index', render_index, name='index'),
    path('book_creator_form', render_book_creator_form, name='render_book_creator_form'),
    path('list_of_books', render_list_of_books, name='render_list_of_books'),
    path('google_book_searcher', render_import_from_volume, name='render_import_from_value'),
    path('for_devs', render_for_devs, name='render_for_devs'),
    path('get_books/intitle:<str:title>,inauthor:<str:authors>,'
         + 'inlanguage:<str:language>,published_date_from:<str:date_from>,'
         + 'published_date_to:<str:date_to>,', render_filter_books_data, name='render_filter_books_data')
]
