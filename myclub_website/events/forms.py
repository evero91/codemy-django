from django.db.models import fields
from django import forms
from django.forms import ModelForm
from .models import Venue

# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email',) # '__all__'
        # labels = {
        #     'name': 'Enter You Venue Here',
        #     'address': '',
        #     'zip_code': '',
        #     'web': '',
        #     'email': '',
        # }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'web': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }
