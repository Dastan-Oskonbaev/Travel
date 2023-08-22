# Generated by Django 4.2.4 on 2023-08-22 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('rating', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Rating')),
                ('object_id', models.PositiveIntegerField(verbose_name='Object id')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='contenttypes.contenttype', verbose_name='Content type')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]