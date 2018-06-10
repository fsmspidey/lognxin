# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-10 20:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_field', models.CharField(max_length=255, null=True)),
                ('status_field', models.PositiveIntegerField(null=True)),
                ('date_field', models.DateTimeField(null=True)),
                ('url_field', models.CharField(max_length=255, null=True)),
                ('url_field_method', models.CharField(max_length=10, null=True)),
                ('url_field_uri', models.CharField(max_length=255, null=True)),
                ('url_field_protocol', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=250)),
                ('import_date', models.DateTimeField(default=datetime.datetime.now)),
                ('import_date_finish', models.DateTimeField(null=True)),
                ('tag', models.CharField(max_length=250)),
                ('log_format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.LogFormat')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='load',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Load'),
        ),
    ]
