# Generated by Django 5.0.1 on 2024-02-29 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0025_alter_jobs_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='location',
            field=models.CharField(help_text='Enter the location text', max_length=255),
        ),
    ]