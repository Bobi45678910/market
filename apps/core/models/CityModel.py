from django.db import models

from apps.core.models.admins.CityModelAdmin import CityModelAdmin
from config.constants import NULLABLE


class City(models.Model):
    ModelAdmin = CityModelAdmin

    name = models.CharField("Название", max_length=100)
    slug = models.CharField("Slug", max_length=100, **NULLABLE)
    area = models.ForeignKey(
        "core.Area",
        verbose_name='Область',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='cities'
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name
