# Generated by Django 3.0.7 on 2020-09-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hope', '0003_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
