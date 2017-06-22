# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_no', models.CharField(db_index=True, max_length=256, null=True, verbose_name='Number')),
                ('city_data_not_found', models.BooleanField(default=False)),
                ('city', models.CharField(db_index=True, max_length=256, verbose_name='City')),
                ('name', models.CharField(default='', max_length=256)),
                ('dba', models.CharField(default='', max_length=256)),
                ('phone', models.CharField(default='', max_length=256)),
                ('carrier_type', models.CharField(default='', max_length=256)),
                ('active_trucks', models.IntegerField(default=0)),
                ('mailing_address', models.CharField(default='', max_length=256)),
                ('effective_date', models.CharField(default='', max_length=256)),
                ('checked_manually', models.BooleanField(default=False)),
                ('record_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='DifferentDataModel',
            fields=[
                ('datamodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.DataModel')),
            ],
            bases=('data.datamodel',),
        ),
    ]
