# Generated by Django 4.1.5 on 2023-02-22 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climate', '0006_rename_creature_id_wearing_creature_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationBin',
            fields=[
                ('location_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LocationFountain',
            fields=[
                ('location_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='creature',
            name='last_food_refill',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 18, 5, 22, 473363, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='last_litter_refill',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 18, 5, 22, 473363, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='last_thirst_refill',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 18, 5, 22, 473363, tzinfo=datetime.timezone.utc)),
        ),
    ]