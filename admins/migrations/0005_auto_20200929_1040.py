# Generated by Django 3.0.7 on 2020-09-29 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_events'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]
