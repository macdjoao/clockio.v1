# Generated by Django 4.2 on 2023-07-27 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clock',
            name='slug',
        ),
    ]