# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-10 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_remove_data_code_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='url_field_protocol',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='url_field_uri',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
