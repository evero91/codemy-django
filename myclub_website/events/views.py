from django.shortcuts import redirect, render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

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
    event_list = Event.objects.all().order_by('event_date', 'name')
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
    venue_list = Venue.objects.all().order_by('name') # ? random
    return render(request, 'events/venues.html', {'venue_list': venue_list})

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})

@require_http_methods(["POST"])
def search_venues(request):
    # venue = Venue.objects.get(pk=venue_id)
    search = request.POST['search']
    venues = Venue.objects.filter(name__contains=search)
    return render(request, 'events/search_venues.html', {'search': search, 'venues': venues})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)

    if form.is_valid():
        form.save()
        return redirect('list-venues')

    return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})

def add_event(request):
    submitted = False

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect('listevents')

    return render(request, 'events/update_event.html', {'event': event, 'form': form})

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('listevents')

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')
