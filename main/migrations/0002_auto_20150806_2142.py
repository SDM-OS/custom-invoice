# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='service_type',
            field=models.PositiveIntegerField(default=None, choices=[(0, b'Cleaning'), (1, b'Washing'), (2, b'Servicing')]),
        ),
    ]
