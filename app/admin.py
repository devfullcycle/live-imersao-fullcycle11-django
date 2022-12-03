from django.contrib import admin
from .models import Player, Team, MyTeam, Match, Action

class PlayerAdmin(admin.ModelAdmin):
    list_per_page: int = 15
    search_fields = ('name',)

class ActionInline(admin.TabularInline):
    model = Action

class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_date', 'show_match')
    list_filter = ('match_date', 'team_a', 'team_b')
    search_fields = ('team_a__name', 'team_b__name') # lookups
    inlines = [ActionInline]
    
    def show_match(self, obj: Match):
        return f'{obj.team_a} {obj.team_a_goal} x {obj.team_b_goal} {obj.team_b}'
    
    show_match.short_description = 'Jogo'

admin.site.register(Player, PlayerAdmin)
admin.site.register(Team)
admin.site.register(MyTeam)
admin.site.register(Match, MatchAdmin)
admin.site.register(Action)
# Register your models here.

# lista []
# tupla ()
# dicionário {'key': 'value', 'key1': 'value1'}
