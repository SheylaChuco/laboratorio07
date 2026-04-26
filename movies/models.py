from django.db import models


# NUEVO — Genre como entidad independiente
class Genre(models.Model):
    """Representa un género cinematográfico."""

    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Representa una película en cartelera o catálogo."""

    title = models.CharField(max_length=255, verbose_name="Título")
    synopsis = models.TextField(verbose_name="Sinopsis")

    # CAMBIO — reemplaza el CharField genre por relación ManyToMany
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
        verbose_name="Géneros",
        blank=True,
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