# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0028_auto_20161024_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfdaprogram',
            name='archived_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cfdaprogram',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]