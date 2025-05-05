from django.db import models
from django.utils import timezone

from apps.mart.models.admins.ReviewModelAdmin import ReviewModelAdmin
from apps.mart.models.consts import ReviewTypeChoices


class Review(models.Model):
    ModelAdmin = ReviewModelAdmin

    user = models.ForeignKey(
        "core.User",
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    ad = models.ForeignKey(
        "mart.Ad",
        verbose_name='Объявление',
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    rating = models.FloatField('Рейтинг', default=0)
    type = models.PositiveSmallIntegerField('Тип', choices=ReviewTypeChoices.choices)
    text = models.CharField('Отзыв', max_length=300)
    created_at = models.DateTimeField(verbose_name='Создан', default=timezone.now)
    is_verify = models.BooleanField('Проверен', default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв о товаре {self.ad.name}'
