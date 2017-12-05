# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-01 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0004_auto_20171129_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalentity',
            name='recipient_unique_id',
            field=models.TextField(blank=True, db_index=True, default='', null=True, verbose_name='DUNS Number'),
        ),
    ]