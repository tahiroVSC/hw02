# Generated by Django 5.0 on 2023-12-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0022_remove_teacher_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='month',
            field=models.CharField(default=1, max_length=155, verbose_name='Месяц который он обучал'),
            preserve_default=False,
        ),
    ]
