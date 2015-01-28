# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('user_type', models.IntegerField(choices=[(0, 'Ordinary'), (1, 'SuperHero')], max_length=1)),
                ('bio', models.CharField(max_length=200, null=True, blank=True)),
                ('origin', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
