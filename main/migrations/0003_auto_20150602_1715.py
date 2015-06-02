# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20150601_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Spare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='service_type',
            field=models.PositiveIntegerField(default=0, choices=[(0, b'A'), (1, b'B'), (2, b'C')]),
        ),
        migrations.AlterField(
            model_name='job',
            name='attendee',
            field=models.ForeignKey(to='main.Attender'),
        ),
    ]
