from ..forms.google_book_searcher_form import GoogleBookSearcherForm
from ..book_importer.book_importer import BooksImporter
from django.shortcuts import render, redirect
from requests import get as requests_get
import json


def render_import_from_volume(request):
    if request.POST:
        form = GoogleBookSearcherForm(data=request.POST)
        if form.is_valid():
            book_importer = BooksImporter()

            # Getting search url
            url = book_importer.create_url(keywords=form.create_filter_dict())

            # Getting raw data
            raw_data = requests_get(url)

            # Clean data
            cleaned_data = json.loads(raw_data.content)

            # Validate and create entries in database
            book_importer.create_books(cleaned_data['items'])

            return redirect(to='render_list_of_books')

        context = {'form': GoogleBookSearcherForm(data=request.POST)}
        return render(request, 'import_from_value/import_from_value.html', context)

    context = {'form': GoogleBookSearcherForm()}
    return render(request, 'import_from_value/import_from_value.html', context)


