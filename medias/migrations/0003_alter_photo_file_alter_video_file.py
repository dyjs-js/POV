# Generated by Django 5.0.4 on 2024-04-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medias", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="file",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="video",
            name="file",
            field=models.URLField(),
        ),
    ]