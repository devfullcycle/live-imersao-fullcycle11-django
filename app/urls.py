from .views import show_players
from django.urls import path

urlpatterns = [
    path('show_players', show_players),
]