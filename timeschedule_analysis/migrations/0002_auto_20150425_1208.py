# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeschedule_analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_id', models.IntegerField(unique=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_id', models.IntegerField(unique=True)),
                ('date', models.DateField()),
                ('volume_old', models.IntegerField()),
                ('volume_new', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='bin',
            old_name='location',
            new_name='address',
        ),
        migrations.AddField(
            model_name='bin',
            name='bin_id',
            field=models.IntegerField(default='1', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bin',
            name='volume',
            field=models.IntegerField(default='3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bin',
            name='x_coordiante',
            field=models.FloatField(default='4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bin',
            name='y_coordinate',
            field=models.FloatField(default='5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='bin',
            field=models.ForeignKey(to='timeschedule_analysis.Bin'),
        ),
        migrations.AddField(
            model_name='bin',
            name='city',
            field=models.ForeignKey(default='2', to='timeschedule_analysis.City'),
            preserve_default=False,
        ),
    ]
