# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150602_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='end_date',
            field=models.DateTimeField(default=None, blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='start_date',
            field=models.DateTimeField(default=None, blank=True),
        ),
    ]
