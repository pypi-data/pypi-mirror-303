# Generated by Django 5.0.7 on 2024-07-30 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "lnschema_core",
            "0056_rename_ulabel_ref_is_name_artifactulabel_label_ref_is_name_and_more",
        ),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            UPDATE lnschema_core_artifact
            SET hash = SUBSTR(hash, 1, 22)
            WHERE length(hash) > 22;

            UPDATE lnschema_core_collection
            SET hash = SUBSTR(hash, 1, 22)
            WHERE length(hash) > 22;

            UPDATE lnschema_core_featureset
            SET hash = SUBSTR(hash, 1, 22)
            WHERE length(hash) > 22;
            """,
        ),
        migrations.AlterField(
            model_name="artifactfeatureset",
            name="artifact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="links_feature_set",
                to="lnschema_core.artifact",
            ),
        ),
        migrations.AlterField(
            model_name="artifactfeatureset",
            name="featureset",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="links_artifact",
                to="lnschema_core.featureset",
            ),
        ),
        migrations.AlterField(
            model_name="artifactulabel",
            name="artifact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="links_ulabel",
                to="lnschema_core.artifact",
            ),
        ),
        migrations.AlterField(
            model_name="artifactulabel",
            name="feature",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="links_artifactulabel",
                to="lnschema_core.feature",
            ),
        ),
        migrations.AlterField(
            model_name="artifactulabel",
            name="ulabel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="links_artifact",
                to="lnschema_core.ulabel",
            ),
        ),
        migrations.AlterField(
            model_name="collectionartifact",
            name="artifact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="links_collection",
                to="lnschema_core.artifact",
            ),
        ),
        migrations.AlterField(
            model_name="collectionartifact",
            name="collection",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="links_artifact",
                to="lnschema_core.collection",
            ),
        ),
        migrations.AlterField(
            model_name="collectionfeatureset",
            name="collection",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="links_feature_set",
                to="lnschema_core.collection",
            ),
        ),
        migrations.AlterField(
            model_name="collectionfeatureset",
            name="featureset",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="links_collection",
                to="lnschema_core.featureset",
            ),
        ),
        migrations.AlterField(
            model_name="collectionulabel",
            name="collection",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="links_ulabel",
                to="lnschema_core.collection",
            ),
        ),
        migrations.AlterField(
            model_name="collectionulabel",
            name="feature",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="links_collectionulabel",
                to="lnschema_core.feature",
            ),
        ),
        migrations.AlterField(
            model_name="collectionulabel",
            name="ulabel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="links_collection",
                to="lnschema_core.ulabel",
            ),
        ),
        migrations.RemoveField(
            model_name="transform",
            name="latest_report",
        ),
        migrations.RenameField(
            model_name="artifact",
            old_name="input_of",
            new_name="input_of_runs",
        ),
        migrations.RenameField(
            model_name="collection",
            old_name="input_of",
            new_name="input_of_runs",
        ),
        migrations.RenameField(
            model_name="collection",
            old_name="unordered_artifacts",
            new_name="artifacts",
        ),
        migrations.RenameField(
            model_name="collection",
            old_name="artifact",
            new_name="meta_artifact",
        ),
        migrations.AlterField(
            model_name="artifact",
            name="type",
            field=models.CharField(
                choices=[("dataset", "dataset"), ("model", "model")],
                db_index=True,
                default=None,
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="artifact",
            name="accessor",
            field=models.CharField(
                db_column="accessor",
                db_index=True,
                default=None,
                max_length=64,
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="artifact",
            old_name="accessor",
            new_name="_accessor",
        ),
        migrations.AlterField(
            model_name="feature",
            name="name",
            field=models.CharField(
                db_index=True, default=None, max_length=150, unique=True
            ),
        ),
        migrations.RenameField(
            model_name="transform",
            old_name="source_code",
            new_name="_source_code_artifact",
        ),
        migrations.AlterField(
            model_name="transform",
            name="_source_code_artifact",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="_source_code_of",
                to="lnschema_core.artifact",
            ),
        ),
        migrations.AlterField(
            model_name="artifact",
            name="type",
            field=models.CharField(
                db_index=True, default=None, max_length=20, null=True
            ),
        ),
        migrations.AlterField(
            model_name="transform",
            name="type",
            field=models.CharField(db_index=True, default="pipeline", max_length=20),
        ),
        migrations.RenameField(
            model_name="artifact",
            old_name="feature_values",
            new_name="_feature_values",
        ),
        migrations.RenameField(
            model_name="artifact",
            old_name="hash_type",
            new_name="_hash_type",
        ),
        migrations.RenameField(
            model_name="artifact",
            old_name="key_is_virtual",
            new_name="_key_is_virtual",
        ),
        migrations.RenameField(
            model_name="artifact",
            old_name="param_values",
            new_name="_param_values",
        ),
        migrations.RenameField(
            model_name="run",
            old_name="param_values",
            new_name="_param_values",
        ),
        migrations.RenameField(
            model_name="artifact",
            old_name="previous_runs",
            new_name="_previous_runs",
        ),
        migrations.RenameField(
            model_name="collection",
            old_name="previous_runs",
            new_name="_previous_runs",
        ),
        migrations.RenameField(
            model_name="feature",
            old_name="previous_runs",
            new_name="_previous_runs",
        ),
        migrations.RenameField(
            model_name="param",
            old_name="previous_runs",
            new_name="_previous_runs",
        ),
        migrations.RenameField(
            model_name="storage",
            old_name="previous_runs",
            new_name="_previous_runs",
        ),
        migrations.RenameField(
            model_name="ulabel",
            old_name="previous_runs",
            new_name="_previous_runs",
        ),
        migrations.AlterField(
            model_name="artifact",
            name="_hash_type",
            field=models.CharField(
                db_column="hash_type",
                db_index=True,
                default=None,
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="artifact",
            name="_key_is_virtual",
            field=models.BooleanField(db_column="key_is_virtual"),
        ),
        migrations.AlterField(
            model_name="artifact",
            name="hash",
            field=models.CharField(
                db_index=True, default=None, max_length=22, null=True
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="hash",
            field=models.CharField(
                db_index=True, default=None, max_length=22, null=True
            ),
        ),
        migrations.AlterField(
            model_name="featureset",
            name="hash",
            field=models.CharField(
                db_index=True, default=None, max_length=22, null=True, unique=True
            ),
        ),
        migrations.AddField(
            model_name="transform",
            name="hash",
            field=models.CharField(
                db_index=True, default=None, max_length=22, null=True
            ),
        ),
        migrations.AddField(
            model_name="transform",
            name="source_code",
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="run",
            name="parent",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="lnschema_core.run",
            ),
        ),
        migrations.RenameField(
            model_name="transform",
            old_name="parents",
            new_name="predecessors",
        ),
        migrations.AlterField(
            model_name="transform",
            name="predecessors",
            field=models.ManyToManyField(
                related_name="successors", to="lnschema_core.transform"
            ),
        ),
    ]
