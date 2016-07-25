# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('article', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('tag', models.CharField(max_length=150)),
            ],
        ),
    ]