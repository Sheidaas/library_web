from django import forms
from .validators.date_validator import validate_date_format


class SearchForm(forms.forms.Form):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Hobbit'}))
    authors = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'J. R. R. Tolkien'}))
    language = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'en'}))
    published_from = forms.CharField(validators=[validate_date_format], required=False, widget=forms.TextInput(attrs={'placeholder': '1768-11-13'}))
    published_to = forms.CharField(validators=[validate_date_format], required=False, widget=forms.TextInput(attrs={'placeholder': '2019-05-24'}))

    def create_filter_dict(self):
        _filter = {}
        _filter['title'] = self.cleaned_data['title']
        _filter['authors'] = self.cleaned_data['authors'].split(',')
        _filter['language'] = self.cleaned_data['language']
        _filter['published_date'] = {}
        if self.cleaned_data['published_from'] or self.cleaned_data['published_to']:
            _filter['published_date'] = {
                'from': self.cleaned_data['published_from'],
                'to': self.cleaned_data['published_to']
            }
        return _filter
