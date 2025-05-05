from django.db import models
from django.utils import timezone

from apps.dashboard.models.admins.HistoryViewModelAdmin import (
    HistoryViewModelAdmin,
)


class HistoryView(models.Model):
    ModelAdmin = HistoryViewModelAdmin

    user = models.ForeignKey(
        "core.User",
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='history_view'
    )

    ad = models.ForeignKey(
        "mart.Ad",
        verbose_name='Объявление',
        on_delete=models.CASCADE,
        related_name='history_view'
    )

    created_at = models.DateTimeField(verbose_name='Просмотрено', default=timezone.now)

    class Meta:
        verbose_name = 'История просмотра'
        verbose_name_plural = 'Истории просмотра'

    def __str__(self):
        return self.ad.name
