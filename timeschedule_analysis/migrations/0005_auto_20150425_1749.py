# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeschedule_analysis', '0004_bin_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='bin',
            name='city',
            field=models.ForeignKey(to='timeschedule_analysis.City', null=True),
        ),
        migrations.AlterField(
            model_name='bin',
            name='volume',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bin',
            name='x_coordiante',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='bin',
            name='y_coordinate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='bin',
            field=models.ForeignKey(to='timeschedule_analysis.Bin', null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='volume_new',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='volume_old',
            field=models.IntegerField(null=True),
        ),
    ]
