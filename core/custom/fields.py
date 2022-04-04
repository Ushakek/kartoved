from django.db import models


class CharFieldStripped(models.CharField):
    def to_python(self, value):
        value = super(CharFieldStripped, self).to_python(value)
        return value.strip() if value is not None else value
