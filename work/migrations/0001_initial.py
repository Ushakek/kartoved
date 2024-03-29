# Generated by Django 3.2.13 on 2022-05-06 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notes', '0001_initial'),
        ('users', '0002_alter_userprofile_options'),
        ('djeym', '0002_auto_20220504_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название работы')),
                ('task', models.TextField(verbose_name='Задание на работу')),
                ('active', models.BooleanField(default=True, verbose_name='Работа активна?')),
                ('type_work', models.CharField(choices=[('polygon', 'Территория'), ('polyline', 'Маршрут')], max_length=50, verbose_name='Тип работ')),
                ('execution', models.ManyToManyField(blank=True, to='notes.ModelNotes', verbose_name='Исполнение')),
                ('executor', models.ForeignKey(limit_choices_to={'available_for_work': True, 'user_status': 'WORKER'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='worker', to='users.userprofile', verbose_name='Исполнитель')),
                ('polygon', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_polygon', to='djeym.polygon', verbose_name='Территория работ')),
                ('polyline', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_polyline', to='djeym.polyline', verbose_name='Маршрут работ')),
            ],
        ),
    ]
