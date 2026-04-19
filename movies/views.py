from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny

from .models import Movie
from .serializers import MovieSerializer, MovieListSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(is_active=True)
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "genre"]
    ordering_fields = ["release_date", "rating", "title"]
    ordering = ["-release_date"]

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer