from django.contrib import admin
from .models import Games, GamesGenre


class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')


admin.site.register(Games, GamesAdmin)
