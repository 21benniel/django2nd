# Generated by Django 3.0.6 on 2020-06-20 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0002_auto_20200620_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='vaccination',
            new_name='vaccinations',
        ),
    ]
