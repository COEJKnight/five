# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-18 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0008_delete_cfdaprogram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfda',
            name='program_number',
            field=models.TextField(unique=True),
        ),
    ]