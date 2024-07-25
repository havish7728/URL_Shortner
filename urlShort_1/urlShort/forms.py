from django import forms
class Url(forms.Form):
    url = forms.URLField(label="Enter URL",required=True)