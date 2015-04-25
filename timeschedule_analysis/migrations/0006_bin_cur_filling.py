# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeschedule_analysis', '0005_auto_20150425_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='cur_filling',
            field=models.IntegerField(null=True),
        ),
    ]
