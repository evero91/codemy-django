from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # name es a quien le hace referencia url en las paginas {% url 'home' %} o en el view redirect('home')
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('events/', views.all_events, name='listevents'),
    path('add_venue/', views.add_venue, name='add-venue'),
    path('list_venues/', views.list_venues, name='list-venues'),
    path('show_venue/<int:venue_id>', views.show_venue, name='show-venue'),
    path('search_venues/', views.search_venues, name='search-venues'),
    path('update_venue/<int:venue_id>', views.update_venue, name='update-venue'),
    path('add_event/', views.add_event, name='add-event'),
    path('update_event/<int:event_id>', views.update_event, name='update-event'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete-event'),
    path('delete_venue/<int:venue_id>', views.delete_venue, name='delete-venue'),
]