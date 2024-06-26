# Generated by Django 5.0.4 on 2024-05-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("review_title", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("publisher", models.CharField(blank=True, max_length=100)),
                ("content", models.TextField()),
                ("summary", models.TextField()),
                ("image", models.ImageField(blank=True, upload_to="")),
                (
                    "is_public",
                    models.BooleanField(
                        default=True,
                        help_text="Does this reivew allow public?",
                        verbose_name="is Public?",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
