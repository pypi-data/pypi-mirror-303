# Generated by Django 5.2 on 2024-08-27 10:54

import bionty.ids
import django.db.models.deletion
import lnschema_core.ids
import lnschema_core.models
import lnschema_core.users
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("bionty", "0037_alter_cellline_source_alter_cellmarker_source_and_more"),
        ("lnschema_core", "0063_populate_latest_field"),
    ]

    operations = [
        migrations.CreateModel(
            name="Biosample",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_12, max_length=12, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "batch",
                    models.CharField(
                        db_index=True, default=None, max_length=60, null=True
                    ),
                ),
                ("description", models.TextField(default=None, null=True)),
                (
                    "_previous_runs",
                    models.ManyToManyField(related_name="+", to="lnschema_core.run"),
                ),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="biosamples", to="lnschema_core.artifact"
                    ),
                ),
                (
                    "cell_types",
                    models.ManyToManyField(
                        related_name="biosamples", to="bionty.celltype"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "diseases",
                    models.ManyToManyField(
                        related_name="biosamples", to="bionty.disease"
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.run",
                    ),
                ),
                (
                    "tissues",
                    models.ManyToManyField(
                        related_name="biosamples", to="bionty.tissue"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.CanValidate, models.Model),
        ),
        migrations.CreateModel(
            name="Medication",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=bionty.ids.ontology, max_length=8, unique=True
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=256)),
                (
                    "ontology_id",
                    models.CharField(
                        db_index=True, default=None, max_length=32, null=True
                    ),
                ),
                (
                    "chembl_id",
                    models.CharField(
                        db_index=True, default=None, max_length=32, null=True
                    ),
                ),
                (
                    "abbr",
                    models.CharField(
                        db_index=True,
                        default=None,
                        max_length=32,
                        null=True,
                        unique=True,
                    ),
                ),
                ("synonyms", models.TextField(default=None, null=True)),
                ("description", models.TextField(default=None, null=True)),
                (
                    "_previous_runs",
                    models.ManyToManyField(related_name="+", to="lnschema_core.run"),
                ),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="medications", to="lnschema_core.artifact"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "parents",
                    models.ManyToManyField(
                        related_name="children", to="clinicore.medication"
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.run",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="bionty.source",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("name", "ontology_id")},
            },
            bases=(
                models.Model,
                lnschema_core.models.HasParents,
                lnschema_core.models.CanValidate,
            ),
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_12, max_length=12, unique=True
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                ("age", models.IntegerField(db_index=True, default=None, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                            ("unknown", "Unknown"),
                        ],
                        db_index=True,
                        default=None,
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(db_index=True, default=None, null=True),
                ),
                (
                    "deceased",
                    models.BooleanField(db_index=True, default=None, null=True),
                ),
                (
                    "deceased_date",
                    models.DateField(db_index=True, default=None, null=True),
                ),
                (
                    "_previous_runs",
                    models.ManyToManyField(related_name="+", to="lnschema_core.run"),
                ),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="patients", to="lnschema_core.artifact"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "ethnicity",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="bionty.ethnicity",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.run",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.CanValidate, models.Model),
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_8, max_length=8, unique=True
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                ("description", models.TextField(default=None, null=True)),
                (
                    "_previous_runs",
                    models.ManyToManyField(related_name="+", to="lnschema_core.run"),
                ),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="projects", to="lnschema_core.artifact"
                    ),
                ),
                (
                    "collections",
                    models.ManyToManyField(
                        related_name="projects", to="lnschema_core.collection"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.run",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.CanValidate, models.Model),
        ),
        migrations.CreateModel(
            name="Treatment",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_12, max_length=12, unique=True
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in-progress", "In Progress"),
                            ("completed", "Completed"),
                            ("entered-in-error", "Entered in Error"),
                            ("stopped", "Stopped"),
                            ("on-hold", "On Hold"),
                            ("unknown", "Unknown"),
                            ("not-done", "Not Done"),
                        ],
                        default=None,
                        max_length=16,
                        null=True,
                    ),
                ),
                ("dosage", models.FloatField(default=None, null=True)),
                (
                    "dosage_unit",
                    models.CharField(default=None, max_length=32, null=True),
                ),
                (
                    "administered_datetime",
                    models.DateTimeField(default=None, null=True),
                ),
                ("duration", models.DurationField(default=None, null=True)),
                ("route", models.CharField(default=None, max_length=32, null=True)),
                ("site", models.CharField(default=None, max_length=32, null=True)),
                (
                    "_previous_runs",
                    models.ManyToManyField(related_name="+", to="lnschema_core.run"),
                ),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="treatments", to="lnschema_core.artifact"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "medication",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="clinicore.medication",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.run",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.CanValidate, models.Model),
        ),
    ]
