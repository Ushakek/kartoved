# Generated by Django 3.2.13 on 2022-05-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelnotes',
            name='name',
            field=models.CharField(default='test', max_length=200, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
