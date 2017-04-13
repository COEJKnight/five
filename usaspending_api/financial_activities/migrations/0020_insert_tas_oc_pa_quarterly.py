# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-04 20:13
from __future__ import unicode_literals

from django.db import migrations

from usaspending_api.financial_activities.models import (
    TasProgramActivityObjectClassQuarterly)


def insert_quarterly_records(apps, schema_editor):
    """Insert quarterly File B totals for existing submissions."""
    TasProgramActivityObjectClassQuarterly.insert_quarterly_numbers()


def remove_quarterly_records(apps, schema_editor):
    """Delete quarterly File B totals for existing submissions."""
    TasProgramActivityObjectClassQuarterly.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('financial_activities', '0019_auto_20170404_1753'),
    ]

    operations = [
        migrations.RunPython(insert_quarterly_records, remove_quarterly_records),
    ]
