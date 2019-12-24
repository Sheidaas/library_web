from django import forms


class GoogleBookSearcherForm(forms.forms.Form):
    keywords = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'tolkien hobbit'}))

    def create_filter_dict(self):
        return self.cleaned_data['keywords'].split(';')
