# Generated by Django 5.0.1 on 2024-01-25 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.category'),
            preserve_default=False,
        ),
    ]
