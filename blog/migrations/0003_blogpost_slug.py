# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-22 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='this is my slug'),
        ),
    ]
