# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_activities', '0007_financialaccountsbyprogramactivityobjectclass_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='deobligations_recoveries_refund_pri_program_object_class_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='drv_obligations_incurred_by_program_object_class',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='drv_obligations_undelivered_orders_unpaid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='gross_outlay_amount_by_program_object_class_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='gross_outlay_amount_by_program_object_class_fyb',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='gross_outlays_delivered_orders_paid_total_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='gross_outlays_delivered_orders_paid_total_fyb',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='gross_outlays_undelivered_orders_prepaid_total_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='gross_outlays_undelivered_orders_prepaid_total_fyb',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='obligations_delivered_orders_unpaid_total_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='obligations_delivered_orders_unpaid_total_fyb',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='obligations_incurred_by_program_object_class_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='obligations_undelivered_orders_unpaid_total_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='obligations_undelivered_orders_unpaid_total_fyb',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl480100_undelivered_orders_obligations_unpaid_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl480100_undelivered_orders_obligations_unpaid_fyb',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl480200_undelivered_orders_oblig_prepaid_advanced_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl480200_undelivered_orders_oblig_prepaid_advanced_fyb',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl483100_undelivered_orders_oblig_transferred_unpaid_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl483200_undeliv_orders_oblig_transferred_prepaid_adv_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl487100_down_adj_pri_unpaid_undel_orders_oblig_recov_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl487200_down_adj_pri_ppaid_undel_orders_oblig_refund_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl488100_upward_adjust_pri_undeliv_order_oblig_unpaid_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl488200_up_adjust_pri_undeliv_order_oblig_ppaid_adv_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl490100_delivered_orders_obligations_unpaid_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl490100_delivered_orders_obligations_unpaid_fyb',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl490200_delivered_orders_obligations_paid_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl490800_authority_outlayed_not_yet_disbursed_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl490800_authority_outlayed_not_yet_disbursed_fyb',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl493100_delivered_orders_oblig_transferred_unpaid_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl497100_down_adj_pri_unpaid_deliv_orders_oblig_recov_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl497200_down_adj_pri_paid_deliv_orders_oblig_refund_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl498100_upward_adjust_pri_deliv_orders_oblig_unpaid_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyprogramactivityobjectclass',
            name='ussgl498200_upward_adjust_pri_deliv_orders_oblig_paid_cpe',
            field=models.DecimalField(decimal_places=2, max_digits=21),
        ),
    ]