# Generated by Django 5.0.1 on 2024-01-25 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_jobs_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='categories',
        ),
    ]