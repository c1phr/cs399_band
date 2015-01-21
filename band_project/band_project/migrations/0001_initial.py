# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from band_project.models import Tour_Dates
import datetime


def add_dates(apps, schema_editor):
    today = datetime.datetime.now()

    date1 = Tour_Dates(date=today + datetime.timedelta(days=7), city="Flagstaff, AZ", special_guest="None")
    date1.save()

    date2 = Tour_Dates(date=today + datetime.timedelta(days=9), city="Phoenix, AZ", special_guest="The Heatwaves")
    date2.save()

    date3 = Tour_Dates(date=today + datetime.timedelta(days=11), city="Tucson, AZ", special_guest="None")
    date3.save()

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour_Dates',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('city', models.CharField(max_length=50)),
                ('special_guest', models.CharField(max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),

        migrations.RunPython(add_dates),
    ]
