from django.shortcuts import render
from .models import Player
# Create your views here.

#@login_required(login_url='/login/')
def show_players(request):
    players = Player.objects.all()
    return render(request, 'app/players.html', {'players': players})
