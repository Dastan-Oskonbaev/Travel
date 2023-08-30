# Generated by Django 4.2.4 on 2023-08-30 16:02

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='place',
            name='boundary',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, verbose_name='Boundary'),
        ),
        migrations.AlterField(
            model_name='region',
            name='boundary',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, verbose_name='Boundary'),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Location'),
        ),
    ]