from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    WORKER = 'WORKER'
    MANAGER = 'MANAGER'

    STATUS_CHOICES = (
        (WORKER, 'Рабочий'),
        (MANAGER, 'Управляющий'),
    )

    GENDER_CHOICES = (
        ("MALE", "Мужской"),
        ("FEMALE", "Женский"),
        ("UNKNOWN", "Неизвестен"),
        ("GEOLOG", "Геолог"),
    )

    user = models.OneToOneField(
        User,
        models.CASCADE,
        related_name='profile',
        verbose_name='ИМя пользователя (логин)',
    )
    user_status = models.CharField(
        'Статус пользователя',
        choices=STATUS_CHOICES,
        default=WORKER,
        max_length=100,
    )
    full_name = models.CharField(
        'Полное имя',
        max_length=64,
        blank=True,
        default='',
    )
    available_for_work = models.BooleanField(
        'Доступен для работы',
        default=True,
    )
    phone = models.CharField(
        'Телефон',
        max_length=12,
    )
    birthday = models.DateField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        'Зарегистрирован',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        'Обновления',
        auto_now=True,
    )
    test_user = models.BooleanField(
        'Тестовый пользователь',
        default=False,
    )
    show_all_works = models.BooleanField(
        'Показывать все вакансии',
        default=False,
    )
    mobile_os = models.CharField(
        'Пользовательская ОС',
        max_length=100,
        default="",
        blank=True,
        null=True,
    )
    mobile_model = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    @property
    def email(self) -> str:
        return self.user.email

    def user_profile_json(self) -> dict:
        return {
            'id': self.user.id,
            'username': self.user.username,
            'full_name': self.full_name,
            'phone': self.phone,
            'birthday': self.birthday,
            'email': self.email,
        }

    def __str__(self):
        return self.phone
