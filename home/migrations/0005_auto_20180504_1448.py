# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-04 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180504_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='AN',
            new_name='ARTICLE_ID',
        ),
    ]
