# Generated by Django 4.0.3 on 2022-04-22 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agroengineer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='agroengineer',
            new_name='Agroengineer',
        ),
    ]
