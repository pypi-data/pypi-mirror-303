# Generated by Django 5.1.1 on 2024-10-02 23:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lnschema_core", "0066_alter_artifact__feature_values_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="featurevalue",
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name="paramvalue",
            unique_together=set(),
        ),
    ]
