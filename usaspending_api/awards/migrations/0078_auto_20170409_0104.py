# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-09 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0077_auto_20170405_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='action_type_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionassistance',
            name='business_funds_indicator_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionassistance',
            name='correction_late_delete_indicator_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionassistance',
            name='record_type_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='commercial_item_acquisition_procedures_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='contingency_humanitarian_or_peacekeeping_operation_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='contract_bundling_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='contract_financing_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='cost_accounting_standards_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='cost_or_pricing_data_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='davis_bacon_act_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='epa_designated_product_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='evaluated_preference_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='extent_competed_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='fair_opportunity_limited_sources_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='fed_biz_opps_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='foreign_funding_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='idv_type_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='information_technology_commercial_item_category_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='interagency_contracting_authority_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='multiple_or_single_award_idv_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='national_interest_action_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='performance_based_service_acquisition_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='place_of_manufacture_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='recovered_materials_sustainability_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='research_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='sea_transportation_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='service_contract_act_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='solicitation_procedures_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='subcontracting_plan_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='type_of_idc_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='type_set_aside_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactioncontract',
            name='national_interest_action',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
