from django.db import models
from djeym.models import Placemark

from users.models import UserProfile
from utils.helpers import generate_upload_name
from work.models import WorkModel


class ModelNotes(models.Model):
    """Модель записок/заметок"""

    name = models.CharField(verbose_name='Название', max_length=200)
    coordinates = models.CharField(
        verbose_name='Координаты', blank=True, max_length=200
    )

    description = models.TextField(verbose_name='Описание')

    photo = models.ImageField(
        verbose_name='Фотографии объекта',
        upload_to=generate_upload_name,
        null=True,
        blank=True,
    )

    user_profile = models.ForeignKey(
        to=UserProfile,
        on_delete=models.DO_NOTHING,
        related_name='notes',
        verbose_name='Пользователь',
    )
    work = models.ForeignKey(
        to=WorkModel,
        on_delete=models.DO_NOTHING,
        related_name='work_notes',
        verbose_name='Работа',
        null=True,
        blank=True,
    )
    marker = models.ForeignKey(
        to=Placemark,
        on_delete=models.DO_NOTHING,
        related_name='marker_notes',
        verbose_name='Маркер на карте',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.coordinates

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
