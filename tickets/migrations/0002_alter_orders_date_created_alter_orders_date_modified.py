# Generated by Django 4.1.4 on 2022-12-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
