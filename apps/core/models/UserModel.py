from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.managers.UserManager import UserManager
from config.constants import NULLABLE


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField("Номер телфона", max_length=20, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
