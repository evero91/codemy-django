from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # name es a quien le hace referencia url en la pagina en sí {% url 'home' %}
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('events/', views.all_events, name='listevents'),
    path('add_venue/', views.add_venue, name='add-venue'),
    path('list_venues/', views.list_venues, name='list-venues'),
]