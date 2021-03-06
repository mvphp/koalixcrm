# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-07 19:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0025_auto_20180413_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='dateofcreation',
            new_name='date_of_creation',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lastmodification',
            new_name='last_modification',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lastmodifiedby',
            new_name='last_modified_by',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='defaultCustomerBillingCycle',
            new_name='default_customer_billing_cycle',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='ismemberof',
            new_name='is_member_of',
        ),
    ]
