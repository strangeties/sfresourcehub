from .models import Resource
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class AddResourceForm(forms.Form):
    resource_name = forms.CharField(max_length=100, required=True)
    org_name = forms.CharField(max_length=100, required=True)
    category = forms.ChoiceField(choices=Resource.CATEGORIES)
    hours = forms.TimeField(required=True)
    phone = forms.CharField(max_length=20)
    
    address = forms.CharField(max_length=100, required=True)
    street = forms.CharField(max_length=100, required=True, disabled=True)
    city = forms.CharField(max_length=100, required=True, disabled=True)
    state = forms.CharField(max_length=100, required=True, disabled=True)
    long = forms.DecimalField(max_digits=12, decimal_places=6, required=True, disabled=True)
    lat = forms.DecimalField(max_digits=12, decimal_places=6, required=True, disabled=True)

    url = forms.URLField(max_length=100)
    notes = forms.CharField(max_length=250)
