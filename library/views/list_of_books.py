from django.http import HttpResponse
from django.db.models import Q, QuerySet
from django.shortcuts import render
from ..models.book import Book
from ..forms.search import SearchForm
from functools import reduce
from operator import and_, or_


def render_list_of_books(request) -> HttpResponse:
    if request.POST:
        form = SearchForm(data=request.POST, auto_id=True)
        if form.is_valid():
            _filter = form.create_filter_dict()
            context = {'form': SearchForm(data=request.POST, auto_id=True),
                       'books_list': filter_books(_filter)}
            return render(request, 'list_of_books/list_of_books.html', context)

        context = {'form': SearchForm(data=request.POST, auto_id=True)}
        return render(request, 'list_of_books/list_of_books.html', context)

    context = {'form': SearchForm(auto_id=True)}
    return render(request, 'list_of_books/list_of_books.html', context)


def filter_books(_filter: dict) -> QuerySet:
    if _filter:
        argument_list = []
        for key in _filter:
            if key == 'authors':
                if _filter['authors']:
                    author_argument_list = reduce(or_, [Q(**{'authors__full_name__icontains': author_name})
                                            for author_name in _filter['authors']])
            if key == 'title':
                if _filter['title']:
                    argument_list.append(Q(**{'title__icontains': _filter['title']}))

            if key == 'language':
                if _filter['language']:
                    argument_list.append(Q(**{'language__icontains': _filter['language']}))

            if key == 'published_date':
                if _filter['published_date']:
                    if _filter['published_date']['from']:
                        argument_list.append(Q(**{'published_date__gte': _filter['published_date']['from']}))
                    if _filter['published_date']['to']:
                        argument_list.append(Q(**{'published_date__lte': _filter['published_date']['to']}))

        if argument_list or author_argument_list:
            query = None
            if argument_list:
                query = reduce(and_, argument_list)
            if query:
                filtered_books = Book.objects.filter(query, author_argument_list)
            else:
                filtered_books = Book.objects.filter(author_argument_list)
            if filtered_books:
                return filtered_books
            return Book.objects.none()
        return Book.objects.all()
    return Book.objects.all()
