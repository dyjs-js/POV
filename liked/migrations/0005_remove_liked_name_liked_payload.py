# Generated by Django 5.0.4 on 2024-04-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("liked", "0004_remove_liked_books_remove_liked_movies_liked_books_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="liked",
            name="name",
        ),
        migrations.AddField(
            model_name="liked",
            name="payload",
            field=models.TextField(blank=True, null=True),
        ),
    ]