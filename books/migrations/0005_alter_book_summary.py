# Generated by Django 5.0.4 on 2024-05-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_book_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="summary",
            field=models.TextField(blank=True, null=True),
        ),
    ]