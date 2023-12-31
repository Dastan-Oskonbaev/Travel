# Generated by Django 4.2.4 on 2023-08-31 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_attractions_description_ar_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attractions',
            old_name='description_ch',
            new_name='description_zh_hans',
        ),
        migrations.RenameField(
            model_name='attractions',
            old_name='name_ch',
            new_name='name_zh_hans',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='address_ch',
            new_name='address_zh_hans',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='name_ch',
            new_name='name_zh_hans',
        ),
        migrations.RenameField(
            model_name='eventscategory',
            old_name='name_ch',
            new_name='name_zh_hans',
        ),
        migrations.RenameField(
            model_name='hotels',
            old_name='address_ch',
            new_name='address_zh_hans',
        ),
        migrations.RenameField(
            model_name='hotels',
            old_name='description_ch',
            new_name='description_zh_hans',
        ),
        migrations.RenameField(
            model_name='hotels',
            old_name='name_ch',
            new_name='name_zh_hans',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_ch',
            new_name='description_zh_hans',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='name_ch',
            new_name='name_zh_hans',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='description_ch',
            new_name='description_zh_hans',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='name_ch',
            new_name='name_zh_hans',
        ),
        migrations.RenameField(
            model_name='restaurants',
            old_name='address_ch',
            new_name='address_zh_hans',
        ),
        migrations.RenameField(
            model_name='restaurants',
            old_name='description_ch',
            new_name='description_zh_hans',
        ),
        migrations.RenameField(
            model_name='restaurants',
            old_name='name_ch',
            new_name='name_zh_hans',
        ),
        migrations.RenameField(
            model_name='restaurants',
            old_name='specialized_menu_ch',
            new_name='specialized_menu_zh_hans',
        ),
        migrations.RenameField(
            model_name='whattotry',
            old_name='description_ch',
            new_name='description_zh_hans',
        ),
        migrations.RenameField(
            model_name='whattotry',
            old_name='name_ch',
            new_name='name_zh_hans',
        ),
    ]
