# Generated by Django 5.0 on 2023-12-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_slide_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='about_us',
            field=models.CharField(default=1, max_length=255, verbose_name='Строка о вас'),
            preserve_default=False,
        ),
    ]