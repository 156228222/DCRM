# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-17 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0032_auto_20170217_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='resources_alias',
            field=models.CharField(default=b'/', help_text='You can specify alias for resources path in Nginx or other HTTP servers, which is necessary for CDN speedup.', max_length=255, verbose_name='Resources Alias'),
        ),
    ]