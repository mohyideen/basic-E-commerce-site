# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 04:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20161215_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postssubmit',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 15, 4, 8, 11, 462284, tzinfo=utc)),
        ),
    ]
