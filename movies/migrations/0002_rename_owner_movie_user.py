# Generated by Django 5.0.4 on 2024-04-27 15:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="owner",
            new_name="user",
        ),
    ]