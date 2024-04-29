# Generated by Django 5.0.4 on 2024-04-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("liked", "0001_initial"),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="liked",
            name="movies",
            field=models.ManyToManyField(related_name="liked", to="movies.movie"),
        ),
    ]
