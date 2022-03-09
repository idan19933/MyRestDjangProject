# Generated by Django 4.0.2 on 2022-02-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='workers',
            name='slug',
            field=models.SlugField(default='default_slug'),
        ),
    ]
