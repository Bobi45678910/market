from django.db import models
from django.utils import timezone

from apps.chat.models.admins.MessageModelAdmin import MessageModelAdmin


class Message(models.Model):
    ModelAdmin = MessageModelAdmin

    text = models.CharField('Текст', max_length=500)

    user = models.ForeignKey(
        "core.User",
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='messages'
    )

    chat = models.ForeignKey(
        "chat.Chat",
        verbose_name="Чат",
        on_delete=models.CASCADE,
        related_name="messages"
    )

    created_at = models.DateTimeField(verbose_name='Создан', default=timezone.now)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'Сообщения {self.user.email}'
