from rest_framework import serializers
from .models import Genre, Movie  # CAMBIO — importar Genre


# NUEVO — serializer para Genre
class GenreSerializer(serializers.ModelSerializer):
    """Serializer para listar y crear géneros."""

    class Meta:
        model = Genre
        fields = ["id", "name", "slug"]
        read_only_fields = ["id"]


class MovieSerializer(serializers.ModelSerializer):
    """Serializer completo para crear, editar y listar películas."""

    # NUEVO — géneros anidados como lectura
    genres = GenreSerializer(many=True, read_only=True)

    # NUEVO — campo de escritura para asignar géneros por ID
    genre_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        source="genres",
        write_only=True,
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "synopsis",
            "genres",      # NUEVO — lectura (objetos anidados)
            "genre_ids",   # NUEVO — escritura (lista de IDs)
            "duration_minutes",
            "release_date",
            "rating",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class MovieListSerializer(serializers.ModelSerializer):
    """Serializer reducido para listados."""

    # NUEVO — incluir géneros también en el listado
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "genres", "duration_minutes", "release_date", "rating"]