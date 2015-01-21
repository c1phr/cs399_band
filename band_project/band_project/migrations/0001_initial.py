# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from band_project.models import Tour_Dates
import datetime

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
    ]
