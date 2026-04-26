from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GenreViewSet, MovieViewSet  # CAMBIO — importar GenreViewSet

router = DefaultRouter()
router.register(r"genres", GenreViewSet, basename="genre")  # NUEVO
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("", include(router.urls)),
]
