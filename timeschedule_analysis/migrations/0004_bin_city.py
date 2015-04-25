# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeschedule_analysis', '0003_auto_20150425_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='city',
            field=models.ForeignKey(default=1, to='timeschedule_analysis.City'),
            preserve_default=False,
        ),
    ]
