# Generated by Django 4.0.3 on 2022-04-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Price',
            field=models.CharField(max_length=30),
        ),
    ]
