from django.contrib import admin
from notes.models import ModelNotes


@admin.register(ModelNotes)
class NotesAdmin(admin.ModelAdmin):
    pass
