# Generated by Django 4.0.3 on 2022-04-22 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.CharField(max_length=230)),
            ],
        ),
    ]