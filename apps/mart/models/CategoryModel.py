from django.db import models

from apps.mart.models.admins.CategoryModelAdmin import CategoryModelAdmin
from config.constants import NULLABLE


class Category(models.Model):
    ModelAdmin = CategoryModelAdmin

    name = models.CharField('Название', max_length=100)
    slug = models.CharField("Slug", max_length=100, **NULLABLE)
    parent = models.ForeignKey('self', related_name='childrens', on_delete=models.PROTECT, **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
