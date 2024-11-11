# Generated by Django 5.1.2 on 2024-11-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmissionEvents",
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
                ("re_name", models.TextField()),
                ("physical_location", models.TextField()),
                ("start_date_time", models.TextField()),
                ("end_date_time", models.TextField()),
                ("contaminant", models.TextField()),
                (
                    "estimated_quantity",
                    models.DecimalField(decimal_places=5, max_digits=10),
                ),
                (
                    "emissions_limit",
                    models.DecimalField(decimal_places=5, max_digits=10),
                ),
                ("limit_units", models.TextField()),
                ("hours_elapsed", models.DecimalField(decimal_places=5, max_digits=10)),
                (
                    "emissions_rate",
                    models.DecimalField(decimal_places=5, max_digits=10),
                ),
                ("flag", models.IntegerField()),
            ],
        ),
    ]