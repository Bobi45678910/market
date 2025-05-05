from django.db import models
from django.utils import timezone

from apps.dashboard.models.admins.FavoriteModelAdmin import FavoriteModelAdmin


class Favorite(models.Model):
    ModelAdmin = FavoriteModelAdmin

    user = models.ForeignKey(
        "core.User",
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='favorites'
    )

    ad = models.ForeignKey(
        "mart.Ad",
        verbose_name='Объявление',
        on_delete=models.CASCADE,
        related_name='favorites'
    )

    created_at = models.DateTimeField(verbose_name='Создан', default=timezone.now)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return self.ad.name
