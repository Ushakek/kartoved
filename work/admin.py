from django.contrib import admin

from notes.models import ModelNotes
from work.forms import WorkForm
from work.models import WorkModel


class NotesInline(admin.TabularInline):
    model = ModelNotes
    can_delete = False
    fields = ('name', 'coordinates', 'description', 'photo', 'user_profile')
    readonly_fields = (
        'name',
        'coordinates',
    )


@admin.register(WorkModel)
class WorkAdmin(admin.ModelAdmin):
    form = WorkForm
    list_display = ['name', 'active', 'executor']
    inlines = (NotesInline,)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'task',
                    'active',
                    'done',
                    'type_work',
                    'polygon',
                    'polyline',
                    'executor',
                ),
            },
        ),
    )
