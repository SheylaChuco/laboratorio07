from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Serializer completo para crear, editar y listar películas."""

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "synopsis",
            "genre",
            "duration_minutes",
            "release_date",
            "rating",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class MovieListSerializer(serializers.ModelSerializer):
    """Serializer reducido para listados (mejor rendimiento)."""

    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "duration_minutes", "release_date", "rating"]