# Generated by Django 5.0.3 on 2025-04-30 19:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0003_alter_ad_is_sold_alter_ad_sold_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0, verbose_name='Рейтинг')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Сделка состоялась'), (1, 'Сделка не состоялась')], verbose_name='Тип')),
                ('text', models.CharField(max_length=300, verbose_name='Отзыв')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создан')),
                ('is_verify', models.BooleanField(default=False, verbose_name='Проверен')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='mart.ad', verbose_name='Объявление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
