# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-14 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_option_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='option_text',
            field=models.CharField(max_length=255),
        ),
    ]
