# Generated by Django 5.1.2 on 2025-02-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_superfundsite'),
    ]

    operations = [
        migrations.AddField(
            model_name='emissionevents',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emissionevents',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='superfundsite',
            name='epa_id',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
