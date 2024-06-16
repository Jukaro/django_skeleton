from django.contrib import admin
from game.models import Match, Player, Tournament

# Register your models here.
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Tournament)
