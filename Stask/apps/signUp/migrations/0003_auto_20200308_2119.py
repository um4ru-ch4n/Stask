# Generated by Django 3.0.3 on 2020-03-08 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signUp', '0002_auto_20200308_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(default='user', max_length=50, verbose_name='Тип пользователя'),
        ),
    ]
