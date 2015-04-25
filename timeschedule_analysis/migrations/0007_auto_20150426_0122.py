# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeschedule_analysis', '0006_bin_cur_filling'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bin',
            old_name='x_coordiante',
            new_name='x_coordinate',
        ),
    ]
