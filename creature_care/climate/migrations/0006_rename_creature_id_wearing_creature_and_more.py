# Generated by Django 4.1.6 on 2023-02-20 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climate', '0005_rename_creature_id_profile_creature_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wearing',
            old_name='creature_id',
            new_name='creature',
        ),
        migrations.RenameField(
            model_name='wearing',
            old_name='item_id',
            new_name='item',
        ),
        migrations.AlterField(
            model_name='creature',
            name='last_food_refill',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 16, 53, 37, 632760, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='last_litter_refill',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 16, 53, 37, 632760, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='last_thirst_refill',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 16, 53, 37, 632760, tzinfo=datetime.timezone.utc)),
        ),
    ]
