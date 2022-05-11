from django import forms

from work.models import WorkModel


class WorkForm(forms.ModelForm):
    """Форма валидации создания работы"""

    def clean(self):
        cleaned_data = super(WorkForm, self).clean()
        polyline, polygon, type_ = (
            cleaned_data['polyline'],
            cleaned_data['polygon'],
            cleaned_data['type_work'],
        )
        if type_ == WorkModel.POLYGON:
            if polyline is not None:
                raise forms.ValidationError(
                    'Был выбран тип "Территория". Поле "Маршрут работ" должно остаться пустым.'
                )
        if type_ == WorkModel.POLYLINE:
            if polygon is not None:
                raise forms.ValidationError(
                    'Был выбран тип "Маршрут". Поле "Территория работ" должно остаться пустым.'
                )
        return cleaned_data

    # def clean_type_work(self):

    #     if polyline is not None and polygon is not None:
    #         raise forms.ValidationError('Выберите только 1 тип')

    class Meta:
        model = WorkModel
        fields = (
            'name',
            'task',
            'active',
            'polygon',
            'polyline',
            'type_work',
            'executor',
            'execution',
        )
