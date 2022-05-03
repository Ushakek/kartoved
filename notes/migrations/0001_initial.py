# Generated by Django 4.0.4 on 2022-05-03 16:08

from django.db import migrations, models
import django.db.models.deletion
import utils.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_userprofile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.CharField(blank=True, max_length=200, verbose_name='Координаты')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to=utils.helpers.generate_upload_name, verbose_name='Фотографии объекта')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='notes', to='users.userprofile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
            },
        ),
    ]
