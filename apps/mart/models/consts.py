from django.db import models


class AdTypeChoices(models.IntegerChoices):
    new = 0, 'Новый'
    used = 1, 'Б/У'


class ReviewTypeChoices(models.IntegerChoices):
    successfully = 0, 'Сделка состоялась'
    not_successfully = 1, 'Сделка не состоялась'
