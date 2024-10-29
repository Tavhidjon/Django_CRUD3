from django import forms
from .models import Car, Company

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['image', 'name', 'product_date', 'company']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['image', 'name']


