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
                ('user_type', models.IntegerField(max_length=1, choices=[(0, 'Ordinary'), (1, 'SuperHero')], null=True)),
                ('bio', models.CharField(max_length=200, blank=True, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('origin', models.CharField(max_length=100, blank=True, null=True)),
                ('address', models.CharField(max_length=200, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
