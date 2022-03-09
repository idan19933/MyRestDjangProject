# Generated by Django 4.0.2 on 2022-02-24 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_rename_first_name_workers_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workers',
            name='manager_id',
        ),
        migrations.AddField(
            model_name='workers',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workers.workers'),
        ),
    ]
