# Generated by Django 5.0.1 on 2024-02-02 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0020_jobs_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='location',
        ),
    ]
