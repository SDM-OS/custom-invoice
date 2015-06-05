# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150605_1836'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lubes',
            new_name='Lube',
        ),
    ]
