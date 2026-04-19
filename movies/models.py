from django.db import models


class Genre(models.TextChoices):
    """Géneros disponibles para una película."""
    ACTION = "action", "Acción"
    COMEDY = "comedy", "Comedia"
    DRAMA = "drama", "Drama"
    HORROR = "horror", "Terror"
    SCIFI = "scifi", "Ciencia ficción"
    ANIMATION = "animation", "Animación"
    THRILLER = "thriller", "Suspenso"


class Movie(models.Model):
    """Representa una película en cartelera o catálogo."""

    title = models.CharField(max_length=255, verbose_name="Título")
    synopsis = models.TextField(verbose_name="Sinopsis")
    genre = models.CharField(
        max_length=20,
        choices=Genre.choices,
        verbose_name="Género",
    )
    duration_minutes = models.PositiveIntegerField(verbose_name="Duración (minutos)")
    release_date = models.DateField(verbose_name="Fecha de estreno")
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Calificación",
    )
    is_active = models.BooleanField(default=True, verbose_name="Activa")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ["-release_date"]

    def __str__(self):
        return self.title