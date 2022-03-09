from django import forms

class indexform(forms.Form):
    file = forms.FileField(label=False)