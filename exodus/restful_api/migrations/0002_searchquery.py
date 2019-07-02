# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-12 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('query', models.CharField(max_length=500)),
                ('limit', models.PositiveIntegerField()),
            ],
        ),
    ]
