# Generated by Django 5.0 on 2023-12-06 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cigar', '0002_cigar_gauge_cigar_length'),
        ('scores', '0002_scores_cigar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='cigar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cigar.cigar'),
        ),
    ]
