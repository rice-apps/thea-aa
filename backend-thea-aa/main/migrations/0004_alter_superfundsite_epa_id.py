# Generated by Django 5.1.2 on 2024-11-23 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_superfundsite"),
    ]

    operations = [
        migrations.AlterField(
            model_name="superfundsite",
            name="epa_id",
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
