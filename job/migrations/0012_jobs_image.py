# Generated by Django 5.0.1 on 2024-01-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_alter_jobs_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='image',
            field=models.ImageField(default=1, upload_to='jobs_images/'),
            preserve_default=False,
        ),
    ]
