# Generated by Django 5.0.1 on 2024-01-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_jobs_vacancy_jobs_description_jobs_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_type',
            field=models.CharField(choices=[('Full TTime', 'Full Time'), ('Part TTime', 'Part Time')], default='', max_length=15),
        ),
    ]