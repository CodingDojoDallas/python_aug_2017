# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 12:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
