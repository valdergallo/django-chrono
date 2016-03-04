# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='_ChronoDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(db_index=True, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='_ChronoTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField(db_index=True, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChronoDateTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chrono_date', models.ForeignKey(to='chrono._ChronoDate')),
                ('chrono_time', models.ForeignKey(to='chrono._ChronoTime')),
            ],
        ),
    ]
