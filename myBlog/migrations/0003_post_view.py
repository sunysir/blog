# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-15 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0002_auto_20180715_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
