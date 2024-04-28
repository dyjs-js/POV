# Generated by Django 5.0.4 on 2024-04-27 15:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_rename_owner_movie_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="movie",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]