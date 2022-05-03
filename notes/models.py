from django.db import models
from users.models import UserProfile
from utils.helpers import generate_upload_name


class ModelNotes(models.Model):
    """Модель записок/заметок"""
    coordinates = models.CharField(verbose_name='Координаты',
                                   blank=True,
                                   max_length=200)

    description = models.TextField(verbose_name='Описание')

    photo = models.ImageField(verbose_name='Фотографии объекта',
                              upload_to=generate_upload_name)

    user_profile = models.ForeignKey(to=UserProfile,
                                     on_delete=models.DO_NOTHING,
                                     related_name='notes',
                                     verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

