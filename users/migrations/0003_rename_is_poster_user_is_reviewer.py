# Generated by Django 5.0.4 on 2024-04-27 15:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_avatar"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_poster",
            new_name="is_reviewer",
        ),
    ]