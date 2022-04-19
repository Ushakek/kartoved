import re

from django import forms
from django.contrib.auth.models import User

from core.models import UserRegistrationRequest
from users.models import UserProfile


class UserRegistrationRequestForm(forms.ModelForm):
    """Форма валидации пользователя при регистрации"""

    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = UserRegistrationRequest
        fields = ('phone', 'username', 'userfullname', 'email')

    @staticmethod
    def validate_phone(phone):
        """Проверка валидности номера телефона"""
        if re.match(r'^\+7\d{10}$', phone) is None:
            raise forms.ValidationError(
                'Введите корректный номер телефона', 'phone_format_error'
            )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        self.validate_phone(username)
        if User.objects.filter(username=username):
            raise forms.ValidationError(
                'Пользователь с таким номером телефона уже зарегистрирован',
                'username_exist',
            )
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email):
            raise forms.ValidationError(
                'Пользователь с таким почтовым адресом уже зарегистрирован',
                'username_exist',
            )
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        self.validate_phone(phone)
        if UserProfile.objects.filter(phone=phone):
            raise forms.ValidationError(
                'Пользователь с таким номером телефона уже зарегистрирован.',
                'phone_exist',
            )
        return phone

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Оба пароля должны совпадать', 'code="password_mismatch"'
            )
        return password2

    def save(self, commit=True):
        (
            registration_request,
            created,
        ) = UserRegistrationRequest.objects.update_or_create(
            dict(
                username=self.cleaned_data['username'],
                userfullname=self.cleaned_data['userfullname'],
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password1'],
            ),
            phone=self.cleaned_data['phone'],
        )
        return registration_request
