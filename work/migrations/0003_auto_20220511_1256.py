# Generated by Django 3.2.13 on 2022-05-11 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djeym', '0002_auto_20220504_1940'),
        ('work', '0002_alter_workmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workmodel',
            name='polygon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_polygon', to='djeym.polygon', verbose_name='Территория работ'),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='polyline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_polyline', to='djeym.polyline', verbose_name='Маршрут работ'),
        ),
    ]