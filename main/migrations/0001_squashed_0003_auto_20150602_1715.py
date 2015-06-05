# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'main', '0001_initial'), (b'main', '0002_auto_20150601_1812'), (b'main', '0003_auto_20150602_1715')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('model_no', models.CharField(max_length=100)),
                ('registration_no', models.CharField(max_length=200)),
                ('attendee', models.ForeignKey(to='main.Attender')),
                ('service_type', models.PositiveIntegerField(default=0, choices=[(0, b'A'), (1, b'B'), (2, b'C')])),
            ],
        ),
        migrations.CreateModel(
            name='Attender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Spare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]
