# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import datetime
from django.utils.timezone import utc


def remove_unused_currencies(apps, schema_editor):
    ExchangeRate = apps.get_model("exchange", "ExchangeRate")
    currencies = settings.CURRENCY_CHOICES_DICT.keys()
    for rate in ExchangeRate.objects.all():
        if rate.source.code not in currencies or rate.target.code not in currencies:
            rate.delete()


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
        migrations.RunPython(remove_unused_currencies)
    ]
