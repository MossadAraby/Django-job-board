# Generated by Django 5.0.1 on 2024-01-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_jobs_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_type',
            field=models.CharField(choices=[('Full TTime', 'Full Time'), ('Part TTime', 'Part Time')], max_length=15),
        ),
    ]
