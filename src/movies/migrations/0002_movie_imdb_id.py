# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
