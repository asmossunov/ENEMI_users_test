from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import TextChoices
from accounts.managers import UserManager


class UserCategoryChoices(TextChoices):
    STUDY_CENTER = 'study_center', 'Учебный центр'
    STUDENT = 'student', 'Ученик'
    TUTOR = 'tutor', 'Репетитор'
    PARENTS = 'parents', 'Родители'


class Account(AbstractUser):
    type = models.CharField(
        verbose_name='Тип пользователя',
        choices=UserCategoryChoices.choices,
        max_length=100,
        null=False,
        blank=False,
    )
    father_name = models.CharField(
        verbose_name='Отчество',
        max_length=200,
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=False
    )
    phone = PhoneNumberField(
        unique=True,
        null=False,
        blank=False
    )
    avatar = models.ImageField(
        null=False,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар',
        default='default_avatar/default-user.png'
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False, null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


