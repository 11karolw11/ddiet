# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddiet', '0002_auto_20160730_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='carbs',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='fat',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='protein',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]