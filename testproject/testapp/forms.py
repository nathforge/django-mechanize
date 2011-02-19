from django import forms


class TestForm(forms.Form):
    upload = forms.FileField()
    text = forms.CharField()
