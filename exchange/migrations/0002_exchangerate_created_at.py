# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangerate',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 20, 14, 59, 20, 269556, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
