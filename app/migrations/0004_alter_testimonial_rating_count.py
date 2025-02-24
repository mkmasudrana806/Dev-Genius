# Generated by Django 5.0 on 2024-01-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_testimonial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testimonial",
            name="rating_count",
            field=models.IntegerField(
                choices=[(1, "One"), (2, "Two"), (3, "Three"), (4, "Four"), (5, "Five")]
            ),
        ),
    ]
