# Generated by Django 4.1.5 on 2023-02-07 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0004_room_cateogry"),
        (
            "experiences",
            "0004_alter_experience_category_alter_experience_host_and_more",
        ),
        ("medias", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="experiences.experience",
            ),
        ),
        migrations.AlterField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="rooms.room",
            ),
        ),
        migrations.AlterField(
            model_name="video",
            name="experience",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos",
                to="experiences.experience",
            ),
        ),
    ]
