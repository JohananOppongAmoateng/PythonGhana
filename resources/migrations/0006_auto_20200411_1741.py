# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-04-11 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_video_video_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='video_speaker',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
