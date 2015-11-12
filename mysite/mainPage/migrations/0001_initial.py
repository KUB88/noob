# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='already_download',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('title_link', models.TextField()),
                ('download_link', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='spiderGet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('title_link', models.TextField()),
                ('download_link', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
