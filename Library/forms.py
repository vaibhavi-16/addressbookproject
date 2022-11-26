from django.core import validators
from django import forms
from .models import Address

class AddressBook(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'city', 'state', 'mbno']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'mbno':forms.TextInput(attrs={'class':'form-control'}),
            
        }
