from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # Convert month from name to number
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    context = {
        'name': 'Ever',
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
    }
    return render(request, 'events/home.html', context)

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/list.html', {'event_list': event_list})

def add_venue(request):
    submitted = False

    if request.method == 'POST':
        form = VenueForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})

def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venues.html', {'venue_list': venue_list})