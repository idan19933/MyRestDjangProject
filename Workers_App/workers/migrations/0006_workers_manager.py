# Generated by Django 4.0.2 on 2022-02-24 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0005_remove_workers_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workers.workers'),
        ),
    ]
