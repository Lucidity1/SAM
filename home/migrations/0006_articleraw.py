# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-04 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180504_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleRaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ARTICLE_ID', models.CharField(max_length=128, unique=True)),
                ('CONTENT', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'ArticleRaws',
            },
        ),
    ]