# Generated by Django 3.2.13 on 2022-05-06 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workmodel',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Работа'},
        ),
    ]