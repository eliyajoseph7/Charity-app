# Generated by Django 3.0.7 on 2020-09-29 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0006_event_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Events',
        ),
    ]