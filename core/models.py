from django.contrib.auth.models import User
from django.db import models

from core.custom import fields
from users.models import UserProfile


class UserRegistrationRequest(models.Model):
    username = models.CharField('Имя', max_length=30)
    first_name = models.CharField('Имя', max_length=64, blank=True, null=True)
    second_name = models.CharField('Фамилия', max_length=64, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField('Телефон', max_length=12)
    password = fields.CharFieldStripped('Пароль', max_length=255)

    class Meta:
        verbose_name = 'Запрос на регистрацию'
        verbose_name_plural = 'Запросы на регистрацию'

    @property
    def userfullname(self):
        return f'{self.first_name} {self.second_name}'

    def register(self):
        user = User(
            username=self.username,
            email=self.email,
        )
        user.set_password(self.password)
        user.save()
        user_profile = UserProfile(
            user=user,
            first_name=self.first_name,
            second_name=self.second_name,
            phone=self.phone,
        )
        user_profile.save()
        self.used = True
        self.save()
        self.delete()
        return user

    def __str__(self):
        return self.userfullname if self.userfullname else self.username
