# Generated by Django 5.0 on 2023-12-16 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0025_alter_teacher_teach_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='teahc_image',
            new_name='teach_image',
        ),
    ]