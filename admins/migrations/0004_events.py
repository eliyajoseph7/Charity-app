# Generated by Django 3.0.7 on 2020-09-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_auto_20200925_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('short_description', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'coming'), ('completed', 'completed'), ('postponed', 'postponed')], default='pending', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
