from django.contrib import admin

from work.forms import WorkForm
from work.models import WorkModel


@admin.register(WorkModel)
class WorkAdmin(admin.ModelAdmin):
    form = WorkForm
    list_display = ['name', 'active', 'executor']
    filter_horizontal = ['execution']

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'task',
                    'active',
                    'type_work',
                    'polygon',
                    'polyline',
                    'executor',
                    'execution',
                ),
            },
        ),
    )
