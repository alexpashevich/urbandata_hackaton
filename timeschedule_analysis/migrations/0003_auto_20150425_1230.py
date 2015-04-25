# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeschedule_analysis', '0002_auto_20150425_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bin',
            name='bin_id',
        ),
        migrations.RemoveField(
            model_name='bin',
            name='city',
        ),
        migrations.RemoveField(
            model_name='city',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='sample_id',
        ),
    ]
