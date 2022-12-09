from django.db import models


class StudyCenter(models.Model):
    user = models.OneToOneField(
        verbose_name='Пользователь',
        to='accounts.Account',
        related_name='study_center',
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )
    study_center_name = models.CharField(
        verbose_name='Название учебного центра',
        max_length=200,
        null=True,
        blank=True
    )
    contact_person = models.CharField(
        verbose_name='Контактное лицо',
        max_length=200,
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.study_center_name} {self.contact_person} {self.user.username}'
