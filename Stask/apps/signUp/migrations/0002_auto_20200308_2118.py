# Generated by Django 3.0.3 on 2020-03-08 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signUp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_email',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default=0, max_length=50, verbose_name='Тип пользователя'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserLogPass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=50, verbose_name='Email пользователя')),
                ('user_password', models.CharField(max_length=200, verbose_name='Пароль пользователя')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signUp.User')),
            ],
        ),
    ]
