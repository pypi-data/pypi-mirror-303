# Generated by Django 5.0.6 on 2024-05-18 21:44

import django.db.models.deletion
from django.db import migrations, models

import lnschema_core.models


class Migration(migrations.Migration):
    dependencies = [
        ("lnschema_core", "0050_artifactfeatureset_feature_ref_is_semantic_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeatureSetFeature",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "featureset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="lnschema_core.featureset",
                    ),
                ),
                (
                    "feature",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.feature",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, lnschema_core.models.LinkORM),
        ),
        migrations.RunSQL(
            """
            INSERT INTO lnschema_core_featuresetfeature (featureset_id, feature_id)
            SELECT featureset_id, feature_id
            FROM lnschema_core_feature_feature_sets;
            """
        ),
        migrations.RemoveField(
            model_name="feature",
            name="feature_sets",
        ),
        migrations.AddField(
            model_name="feature",
            name="feature_sets",
            field=models.ManyToManyField(
                related_name="features",
                through="lnschema_core.FeatureSetFeature",
                to="lnschema_core.featureset",
            ),
        ),
        migrations.RenameField(
            model_name="artifactfeatureset",
            old_name="feature_set",
            new_name="featureset",
        ),
        migrations.RenameField(
            model_name="collectionfeatureset",
            old_name="feature_set",
            new_name="featureset",
        ),
    ]
