# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0068_remove_realm_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='realmauditlog',
            name='extra_data',
            field=models.TextField(null=True),
        ),
    ]
