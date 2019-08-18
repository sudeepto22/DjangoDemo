from django.contrib import admin

# Register your models here.
from gamesapi.models.game_model import Game

admin.site.register(Game)
