# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-09 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='status_field',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='url_field',
            field=models.CharField(max_length=255, null=True),
        ),
    ]