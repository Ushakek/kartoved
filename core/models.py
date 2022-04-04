from django.db import models
from django.contrib.auth.models import User

from core.custom import fields
from users.models import UserProfile


class UserRegistrationRequest(models.Model):
    username = models.CharField('Имя', max_length=30)
    userfullname = fields.CharFieldStripped('ФИО', max_length=64)
    email = models.EmailField()
    phone = models.CharField('Телефон', max_length=12)
    password = fields.CharFieldStripped('Пароль', max_length=255)

    class Meta:
        verbose_name = 'Запрос на регистрацию'
        verbose_name_plural = 'Запросы на регистрацию'

    def register(self):
        user = User(
            username=self.username,
            email=self.email,
        )
        user.set_password(self.password)
        user.save()
        user_profile = UserProfile(
            user=user,
            full_name=self.userfullname,
            phone=self.phone,
        )
        user_profile.save()
        self.used = True
        self.save()
        self.delete()
        return user

    def __str__(self):
        return self.userfullname if self.userfullname else self.username


# class UserRegistrationCode(models.Model):
#     request = models.ForeignKey(UserRegistrationRequest,
#                                 models.CASCADE,
#                                 verbose_name='Запрос на регистрацию')
#     date = models.DateTimeField('Дата')
#     code = models.IntegerField('Код')
#     sent = models.BooleanField('Отправлено', default=False)
#     used = models.BooleanField('Использовано', default=False)
#
#     class Meta:
#         verbose_name = 'Код для регистрации'
#         verbose_name_plural = 'Коды для регистрации'
#
#     def __str__(self):
#         return f'{self.request}'
