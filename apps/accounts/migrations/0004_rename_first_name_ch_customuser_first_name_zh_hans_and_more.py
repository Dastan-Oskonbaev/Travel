# Generated by Django 4.2.4 on 2023-08-31 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_first_name_ar_customuser_first_name_ch_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='first_name_ch',
            new_name='first_name_zh_hans',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='last_name_ch',
            new_name='last_name_zh_hans',
        ),
    ]
