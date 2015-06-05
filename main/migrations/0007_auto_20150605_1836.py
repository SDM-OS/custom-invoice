# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150602_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lubes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=100)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Npn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=100)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='attender',
            name='user',
        ),
        migrations.AddField(
            model_name='spare',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
