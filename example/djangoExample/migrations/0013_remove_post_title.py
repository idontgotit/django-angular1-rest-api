# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoExample', '0012_auto_20170518_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
