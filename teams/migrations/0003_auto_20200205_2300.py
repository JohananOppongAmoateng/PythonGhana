# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-02-05 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20200205_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(blank=True, default='', help_text='Position of the team eg. CEO', max_length=200),
        ),
    ]
