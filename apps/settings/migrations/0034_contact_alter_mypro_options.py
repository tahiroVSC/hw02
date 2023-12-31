# Generated by Django 5.0 on 2023-12-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0033_mytpoject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='ваш емаил')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.AlterModelOptions(
            name='mypro',
            options={'verbose_name': 'Мои успехи', 'verbose_name_plural': 'Мои успехи'},
        ),
    ]
