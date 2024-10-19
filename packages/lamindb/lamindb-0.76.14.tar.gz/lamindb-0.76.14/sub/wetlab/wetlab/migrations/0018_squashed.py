# Generated by Django 5.0.6 on 2024-05-16 09:02

import django.db.migrations.operations.special
import django.db.models.deletion
import django.utils.timezone
import lnschema_core.ids
import lnschema_core.users
from django.db import migrations, models

# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# wetlab.migrations.0013_


class Migration(migrations.Migration):
    replaces = [
        ("wetlab", "0001_initial_squashed_0012"),
        ("wetlab", "0013_import_legacy_data"),
        ("wetlab", "0014_rename_species_biosample_organism"),
        ("wetlab", "0015_rename_files_biosample_artifacts_and_more"),
        ("wetlab", "0016_rename_datasets_biosample_collections_and_more"),
        ("wetlab", "0017_remove_biosample_artifacts"),
        ("wetlab", "0018_well_created_at_well_created_by_well_updated_at"),
    ]

    dependencies = [
        ("bionty", "0028_squashed"),
    ]

    operations = [
        migrations.CreateModel(
            name="Biosample",
            fields=[
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
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "cell_lines",
                    models.ManyToManyField(
                        related_name="biosamples", to="bionty.cellline"
                    ),
                ),
                (
                    "cell_types",
                    models.ManyToManyField(
                        related_name="biosamples", to="bionty.celltype"
                    ),
                ),
                (
                    "collections",
                    models.ManyToManyField(
                        related_name="biosamples", to="lnschema_core.collection"
                    ),
                ),
                (
                    "diseases",
                    models.ManyToManyField(
                        related_name="biosamples", to="bionty.disease"
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
            bases=(models.Model, lnschema_core.models.CanValidate),
        ),
        migrations.CreateModel(
            name="ExperimentType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_4, max_length=4, unique=True
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                ("description", models.TextField(default=None, null=True)),
                (
                    "ontology_id",
                    models.CharField(
                        db_index=True, default=None, max_length=32, null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_experiment_types",
                        to="lnschema_core.user",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, lnschema_core.models.CanValidate),
        ),
        migrations.CreateModel(
            name="Experiment",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_8, max_length=8, unique=True
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                ("description", models.TextField(default=None, null=True)),
                ("date", models.DateField(db_index=True, default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="experiments", to="lnschema_core.artifact"
                    ),
                ),
                (
                    "collections",
                    models.ManyToManyField(
                        related_name="experiments", to="lnschema_core.collection"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_experiments",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "experiment_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="experiments",
                        to="wetlab.experimenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, lnschema_core.models.CanValidate),
        ),
        migrations.CreateModel(
            name="Techsample",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_12, max_length=12, unique=True
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                ("batch", models.CharField(db_index=True, default=None, max_length=60)),
                ("description", models.TextField(default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "biosamples",
                    models.ManyToManyField(
                        related_name="techsamples", to="wetlab.biosample"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_techsamples",
                        to="lnschema_core.user",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, lnschema_core.models.CanValidate),
        ),
        migrations.CreateModel(
            name="TreatmentTarget",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_8, max_length=8, unique=True
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=60)),
                ("description", models.TextField(default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="treatment_targets", to="lnschema_core.artifact"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_treatment_targets",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "genes",
                    models.ManyToManyField(
                        related_name="treatment_targets", to="bionty.gene"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, lnschema_core.models.CanValidate),
        ),
        migrations.CreateModel(
            name="Treatment",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_12, max_length=12, unique=True
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[("genetic", "genetic"), ("chemical", "chemical")],
                        db_index=True,
                        max_length=20,
                    ),
                ),
                (
                    "system",
                    models.CharField(
                        choices=[
                            ("CRISPR Cas9", "CRISPR_Cas9"),
                            ("CRISPRi", "CRISPRi"),
                            ("CRISPRa", "CRISPRa"),
                            ("shRNA", "shRNA"),
                            ("siRNA", "siRNA"),
                            ("transgene", "transgene"),
                            ("transient transfection", "transient_transfection"),
                        ],
                        db_index=True,
                        default=None,
                        max_length=20,
                    ),
                ),
                ("description", models.TextField(default=None, null=True)),
                ("sequence", models.TextField(db_index=True, default=None, null=True)),
                (
                    "on_target_score",
                    models.FloatField(db_index=True, default=None, null=True),
                ),
                (
                    "off_target_score",
                    models.FloatField(db_index=True, default=None, null=True),
                ),
                (
                    "ontology_id",
                    models.CharField(
                        db_index=True, default=None, max_length=32, null=True
                    ),
                ),
                (
                    "pubchem_id",
                    models.CharField(
                        db_index=True, default=None, max_length=32, null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="treatments", to="lnschema_core.artifact"
                    ),
                ),
                (
                    "collections",
                    models.ManyToManyField(
                        related_name="treatments", to="lnschema_core.collection"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_treatments",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "targets",
                    models.ManyToManyField(
                        related_name="treatments", to="wetlab.treatmenttarget"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, lnschema_core.models.CanValidate),
        ),
        migrations.CreateModel(
            name="Well",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_4, max_length=4, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        default=None,
                        max_length=32,
                        null=True,
                        unique=True,
                    ),
                ),
                ("row", models.CharField(default=None, max_length=4)),
                ("column", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="wells", to="lnschema_core.artifact"
                    ),
                ),
                (
                    "collections",
                    models.ManyToManyField(
                        related_name="wells", to="lnschema_core.collection"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_wells",
                        to="lnschema_core.user",
                    ),
                ),
            ],
            options={
                "unique_together": {("row", "column")},
            },
            bases=(models.Model, lnschema_core.models.CanValidate),
        ),
    ]
