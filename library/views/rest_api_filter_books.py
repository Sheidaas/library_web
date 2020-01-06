from django.shortcuts import render
from json import dumps
from .list_of_books import filter_books


def render_filter_books_data(request, title, authors, language, date_from, date_to):
    # Is that could be better with django.form.Form ?
    # TODO: better printing book data
    get_data = {
        'title': title,
        'authors': authors,
        'language': language,
        'published_from': date_from,
        'published_to': date_to
    }
    _filter = create_filter(get_data)
    books = filter_books(_filter)
    return render(request, 'api_filter_books/api_filter_books.html', {'data': dumps(create_data(books), indent=4)})


def create_filter(get_data: dict):
    _filter = {}
    if get_data['title'] != '.':
        _filter['title'] = get_data['title']
    else:
        _filter['title'] = ''

    if get_data['authors'] != '.':
        full_names_list = create_authors_full_names(get_data['authors'])
        _filter['authors'] = full_names_list
    else:
        _filter['authors'] = ['']

    if get_data['language'] != '.':
        _filter['language'] = get_data['language']
    else:
        _filter['language'] = ''

    _filter['published_date'] = {}
    if get_data['published_from'] != '.' or get_data['published_to'] != '.':
        _filter['published_date'] = {
            'from': get_data['published_from'],
            'to': get_data['published_to']
        }
    return _filter


def create_data(books):
    data = []
    for book in books:
        data.append(book.to_dict())
    return data


def create_authors_full_names(raw_authors_names):
    full_names_list = []
    authors_names = raw_authors_names.split('-')
    for name in authors_names:
        full_name = ' '.join(name.split('+'))
        full_names_list.append(full_name)
    return full_names_list
