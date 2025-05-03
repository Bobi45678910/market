from django.db import models
from django.utils import timezone

from apps.mart.models.admins.AdModelAdmin import AdModelAdmin
from apps.mart.models.consts import AdTypeChoices
from config.constants import NULLABLE


class Ad(models.Model):
    ModelAdmin = AdModelAdmin

    name = models.CharField('Название', max_length=100)
    category = models.ForeignKey(
        "mart.Category",
        verbose_name='Категория',
        on_delete=models.CASCADE,
        related_name='ads'
    )

    city = models.ForeignKey(
        "core.City",
        verbose_name='Город',
        on_delete=models.CASCADE,
        related_name='ads'
    )

    user = models.ForeignKey(
        "core.User",
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='ads'
    )

    despcription = models.CharField('Описание', max_length=300)
    type = models.PositiveSmallIntegerField('Тип', choices=AdTypeChoices.choices)
    parameters = models.JSONField(**NULLABLE)
    price = models.IntegerField('Цена')
    created_at = models.DateTimeField(verbose_name='Создано', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='Изменено', default=timezone.now)
    is_active = models.BooleanField('Активное', default=True)
    is_sold = models.BooleanField('Продано', default=False)
    sold_at = models.DateTimeField(verbose_name='Дата продажи', default=timezone.now)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name
