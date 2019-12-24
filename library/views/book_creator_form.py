from django.template import loader
from django.http import HttpResponse
from ..forms.book import BookForm


def render_book_creator_form(request):
    template = loader.get_template('book_creator_form/book_creator_form.html')
    if request.POST:
        form = BookForm(data=request.POST, auto_id=True)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return HttpResponse(template.render(context, request))
    context = {'form': BookForm(auto_id=True)}
    return HttpResponse(template.render(context, request))
