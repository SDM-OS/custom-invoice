# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150605_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='end_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='start_date',
        ),
    ]
