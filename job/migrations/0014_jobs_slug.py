# Generated by Django 5.0.1 on 2024-01-27 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_alter_categories_options_alter_jobs_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='slug',
            field=models.SlugField(default=1, verbose_name='blank=true, null = true'),
            preserve_default=False,
        ),
    ]
