# Generated by Django 5.0.4 on 2024-05-07 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("gptSummary", "0001_initial"),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gptsummarymodel",
            name="movie",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="gptSummary",
                to="movies.movie",
            ),
        ),
    ]
