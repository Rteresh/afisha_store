from django import forms
from concert.models import Concert


class SearchForm(forms.Form):
    query = forms.CharField()