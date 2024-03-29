# Generated by Django 5.0.1 on 2024-01-29 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_apply_job'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apply_job',
            options={'verbose_name_plural': 'Apply Job'},
        ),
        migrations.AddField(
            model_name='jobs',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Job_Owner'),
            preserve_default=False,
        ),
    ]
