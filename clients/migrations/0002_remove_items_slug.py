# Generated by Django 4.0.3 on 2022-03-30 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='slug',
        ),
    ]
