from django.db import models
from djeym.models import Polygon, Polyline

from notes.models import ModelNotes
from users.models import UserProfile

__all__ = ['WorkModel']


class WorkModel(models.Model):
    POLYGON = 'polygon'
    POLYLINE = 'polyline'
    TYPE_ROUTE_CHOICE = (
        (POLYGON, 'Территория'),
        (POLYLINE, 'Маршрут'),
    )
    name = models.CharField(verbose_name='Название работы', max_length=100)
    task = models.TextField(verbose_name='Задание на работу')
    active = models.BooleanField(verbose_name='Работа активна?', default=True)
    type_work = models.CharField(
        verbose_name='Тип работ', choices=TYPE_ROUTE_CHOICE, max_length=50
    )

    polygon = models.ForeignKey(
        to=Polygon,
        on_delete=models.CASCADE,
        related_name='work_polygon',
        verbose_name='Территория работ',
        blank=True,
    )
    polyline = models.ForeignKey(
        to=Polyline,
        on_delete=models.CASCADE,
        related_name='work_polyline',
        verbose_name='Маршрут работ',
        blank=True,
    )
    executor = models.ForeignKey(
        to=UserProfile,
        limit_choices_to={
            'available_for_work': True,
            'user_status': UserProfile.WORKER,
        },
        on_delete=models.DO_NOTHING,
        related_name='worker',
        verbose_name='Исполнитель',
    )
    execution = models.ManyToManyField(
        to=ModelNotes,
        verbose_name='Исполнение',
        blank=True,
    )

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Работа'
