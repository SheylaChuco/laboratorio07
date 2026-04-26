from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny

from .models import Genre, Movie  # CAMBIO — importar Genre
from .serializers import GenreSerializer, MovieSerializer, MovieListSerializer  # CAMBIO


# NUEVO — ViewSet para Genre
class GenreViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar géneros.

    list:     GET  /genres/
    create:   POST /genres/
    retrieve: GET  /genres/{id}/
    update:   PUT  /genres/{id}/
    destroy:  DELETE /genres/{id}/
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class MovieViewSet(viewsets.ModelViewSet):
    """ViewSet para gestionar películas."""

    queryset = Movie.objects.filter(is_active=True).prefetch_related("genres")  # CAMBIO — prefetch_related para optimizar consultas
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title"]  # CAMBIO — quitamos genre porque ya no es un campo directo
    ordering_fields = ["release_date", "rating", "title"]
    ordering = ["-release_date"]

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer