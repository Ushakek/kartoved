# Generated by Django 3.2.13 on 2022-05-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_workmodel_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workmodel',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Работа выполнена?'),
        ),
    ]