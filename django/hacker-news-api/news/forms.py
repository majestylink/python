from django import forms


class NewsSearchForm(forms.Form):
    name = forms.CharField(max_length=255)
