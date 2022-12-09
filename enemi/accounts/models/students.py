from django.core.exceptions import ValidationError
from django.db import models

from django.core.validators import BaseValidator, MinValueValidator
from django.utils.deconstruct import deconstructible


class Student(models.Model):
    user = models.OneToOneField(
        verbose_name='Пользователь',
        to='accounts.Account',
        related_name='student',
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.user} '
