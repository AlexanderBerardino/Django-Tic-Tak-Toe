from django.contrib import admin
from .models import Game, Move
admin.site.register(Game)
admin.site.register(Move)


class GameAdmin(admin.ModelAdmin):
    list_display = ...
