# Generated by Django 4.1.5 on 2023-02-07 08:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0005_alter_room_amenities_alter_room_cateogry_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room",
            old_name="cateogry",
            new_name="category",
        ),
    ]
