from django.contrib import admin
from .models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "duration_minutes", "release_date", "is_active"]
    list_filter = ["genres", "is_active"]
    search_fields = ["title"]
    ordering = ["-release_date"]
    filter_horizontal = ["genres"]