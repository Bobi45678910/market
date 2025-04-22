from django.db import models

from apps.core.models.admins.AreaModelAdmin import AreaModelAdmin
from config.constants import NULLABLE


class Area(models.Model):
    ModelAdmin = AreaModelAdmin

    name = models.CharField("Название", max_length=100)
    slug = models.CharField("Slug", max_length=100, **NULLABLE)

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

    def __str__(self):
        return self.name
    
