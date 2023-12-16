# Generated by Django 5.0 on 2023-12-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_about_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zvanie', models.CharField(max_length=255, verbose_name='Звание')),
                ('mentor_name', models.CharField(max_length=255, verbose_name='Имя ментора')),
                ('about_mentor', models.TextField(verbose_name='Информация о менторе')),
                ('quote', models.TextField(verbose_name='Цитата ментора')),
                ('mentor_image', models.ImageField(upload_to='Mentor image')),
                ('twitter', models.URLField(verbose_name='twitter')),
                ('facebook', models.URLField(verbose_name='facebook')),
                ('skype', models.URLField(verbose_name='skype')),
                ('instagram', models.URLField(verbose_name='instagram')),
                ('linkedin', models.URLField(verbose_name='linkedin')),
                ('youtube', models.URLField(verbose_name='youtube')),
            ],
            options={
                'verbose_name': 'Инфорамация обо мне1',
                'verbose_name_plural': 'Настройка информации1',
            },
        ),
    ]