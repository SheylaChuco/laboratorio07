from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "genre", "duration_minutes", "release_date", "is_active"]
    list_filter = ["genre", "is_active"]
    search_fields = ["title"]
    ordering = ["-release_date"]