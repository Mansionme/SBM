# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2021-04-09 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='major_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
