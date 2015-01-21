# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models, migrations
from band_project.models import Tour_Dates

# Add default data
def add_dates(apps, schema_editor):
    today = datetime.datetime.now()

    date1 = Tour_Dates(date=today + datetime.timedelta(days=7), city="Flagstaff, AZ", coords_x=-111.6311, coords_y=35.1992, special_guest="None")
    date1.save()

    date2 = Tour_Dates(date=today + datetime.timedelta(days=9), city="Phoenix, AZ", coords_x=-112.0667, coords_y=33.4500, special_guest="The Heatwaves")
    date2.save()

    date3 = Tour_Dates(date=today + datetime.timedelta(days=11), city="Tucson, AZ", coords_x=-110.9264, coords_y=32.2217, special_guest="None")
    date3.save()

class Migration(migrations.Migration):

    dependencies = [
        ('band_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour_dates',
            name='coords_x',
            field=models.DecimalField(max_digits=8, default=10.1, decimal_places=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour_dates',
            name='coords_y',
            field=models.DecimalField(max_digits=8, default=10.2, decimal_places=4),
            preserve_default=False,
        ),
        migrations.RunPython(add_dates),
    ]
