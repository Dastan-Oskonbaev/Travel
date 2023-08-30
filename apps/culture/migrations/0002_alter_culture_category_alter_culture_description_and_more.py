# Generated by Django 4.2.4 on 2023-08-30 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culture',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cultures', to='culture.culturecategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='culture/<django.db.models.fields.CharField>', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='culturecategory',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='culturecategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='culture_category/<django.db.models.fields.CharField>', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='culturecategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]