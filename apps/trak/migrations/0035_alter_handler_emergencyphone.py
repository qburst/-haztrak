# Generated by Django 4.0.4 on 2022-04-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0034_alter_manifest_designatedfacility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handler',
            name='emergencyPhone',
            field=models.JSONField(null=True),
        ),
    ]
