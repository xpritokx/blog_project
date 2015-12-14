# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('summary', models.TextField(blank=True, default='')),
                ('content', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
