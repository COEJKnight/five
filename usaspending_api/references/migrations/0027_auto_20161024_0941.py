# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0026_auto_20161021_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='cfdaprogram',
            name='appeals',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cfdaprogram',
            name='renewals',
            field=models.TextField(blank=True, null=True),
        ),
    ]