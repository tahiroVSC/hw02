# Generated by Django 5.0 on 2023-12-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='mentor_fon',
            field=models.ImageField(default=1, upload_to='Fon image'),
            preserve_default=False,
        ),
    ]