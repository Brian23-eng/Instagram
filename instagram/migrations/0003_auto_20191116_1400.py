# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-16 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20191116_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ('-posted',)},
        ),
    ]