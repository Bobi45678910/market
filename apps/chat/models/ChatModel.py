from django.db import models
from django.utils import timezone

from apps.chat.models.admins.ChatModelAdmin import ChatModelAdmin


class Chat(models.Model):
    ModelAdmin = ChatModelAdmin

    ad = models.ForeignKey(
        "mart.Ad",
        verbose_name='Объявление',
        on_delete=models.CASCADE,
        related_name='chats'
    )

    from_user = models.ForeignKey(
        "core.User",
        verbose_name='Отправитель',
        on_delete=models.CASCADE,
        related_name='chat_from'
    )

    to_user = models.ForeignKey(
        "core.User",
        verbose_name='Получатель',
        on_delete=models.CASCADE,
        related_name='chat_to'
    )

    created_at = models.DateTimeField(verbose_name='Создан', default=timezone.now)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return f'Чат между {self.from_user.email} и {self.to_user.email}'
