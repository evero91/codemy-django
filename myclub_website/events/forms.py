from django import forms
from django.forms import ModelForm
from .models import Venue, Event

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

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees',)
        labels = {'event_date': 'Event Date (YYYY-MM-DD HH:MM:SS)'}

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            'venue': forms.Select(attrs={'class':'form-select'}),
            'manager': forms.Select(attrs={'class':'form-select'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control'}),
        }