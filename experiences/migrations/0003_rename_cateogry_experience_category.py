# Generated by Django 4.1.5 on 2023-02-03 04:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("experiences", "0002_experience_cateogry"),
    ]

    operations = [
        migrations.RenameField(
            model_name="experience",
            old_name="cateogry",
            new_name="category",
        ),
    ]
